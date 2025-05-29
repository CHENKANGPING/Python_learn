from django.http import JsonResponse, HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password
from django.views.decorators.http import require_http_methods
from django.core.exceptions import ValidationError
from django.utils import timezone
from django.db.models import F

from polls.models import Subject, Teacher, User
from .utils import gen_random_code, Captcha


def show_subjects(request):
    """显示所有学科"""
    subjects = Subject.objects.all().order_by('no')
    return render(request, 'subjects.html', {'subjects': subjects})


def show_teachers(request):
    """显示教师列表"""
    try:
        sno = int(request.GET.get('sno', 0))
        teachers = []
        subject = None
        if sno:
            subject = Subject.objects.only('name').get(no=sno)
            teachers = Teacher.objects.filter(subject=subject).order_by('no')
        return render(request, 'teachers.html', {
            'subject': subject,
            'teachers': teachers
        })
    except (ValueError, Subject.DoesNotExist):
        return redirect('/')


@require_http_methods(['POST'])
def praise_or_criticize(request: HttpRequest) -> HttpResponse:
    """好评或差评"""
    if not request.session.get('userid'):
        return JsonResponse({'code': 20002, 'mesg': '请先登录'})
    
    try:
        tno = int(request.GET.get('tno'))
        teacher = Teacher.objects.get(no=tno)
        
        # 使用F()表达式来避免并发问题
        if request.path.startswith('/praise/'):
            teacher.good_count = F('good_count') + 1
            count = teacher.good_count
        else:
            teacher.bad_count = F('bad_count') + 1
            count = teacher.bad_count
            
        teacher.save()
        # 重新获取更新后的值
        teacher.refresh_from_db()
        count = teacher.good_count if request.path.startswith('/praise/') else teacher.bad_count
        
        data = {'code': 20000, 'mesg': '投票成功', 'count': count}
    except (ValueError, Teacher.DoesNotExist):
        data = {'code': 20001, 'mesg': '投票失败'}
    return JsonResponse(data)


@require_http_methods(['GET', 'POST'])
def login(request: HttpRequest) -> HttpResponse:
    """用户登录"""
    hint = ''
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        captcha = request.POST.get('captcha')
        
        if not all([username, password, captcha]):
            hint = '请填写完整的登录信息'
        elif captcha.lower() != request.session.get('captcha', '').lower():
            hint = '验证码错误'
        else:
            try:
                user = User.objects.get(username=username, is_active=True)
                if check_password(password, user.password):
                    request.session['userid'] = user.no
                    request.session['username'] = user.username
                    user.last_visit = timezone.now()
                    user.save(update_fields=['last_visit'])
                    return redirect('/')
                else:
                    hint = '用户名或密码错误'
            except User.DoesNotExist:
                hint = '用户名或密码错误'
    
    return render(request, 'login.html', {'hint': hint})


def get_captcha(request: HttpRequest) -> HttpResponse:
    """生成验证码"""
    captcha_text = gen_random_code()
    request.session['captcha'] = captcha_text
    image_data = Captcha.instance().generate(captcha_text)
    return HttpResponse(image_data, content_type='image/png')


def logout(request):
    """注销"""
    request.session.flush()
    return redirect('/')

# Create your views here.
