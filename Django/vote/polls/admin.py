from django.contrib import admin
from polls.models import Subject, Teacher

class SubjectAdmin(admin.ModelAdmin):
    list_display = ('no', 'name', 'intro', 'is_hot')
    search_fields = ('name',)
    ordering = ('no',)

class TeacherAdmin(admin.ModelAdmin):
    list_display = ('no', 'name', 'sex', 'birth', 'good_count', 'bad_count', 'subject')
    search_fields = ('name',)
    ordering = ('no',)

admin.site.register(Subject, SubjectAdmin)
admin.site.register(Teacher, TeacherAdmin)

# Register your models here.
