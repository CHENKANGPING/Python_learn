<script setup name="login">
import login_img from '@/assets/image/login.jpg'
import { reactive } from 'vue';
import { useAuthStore } from '@/stores/auth';
import { useRouter } from 'vue-router';
import authHttp from '@/api/authHttp';
import { ElMessage } from 'element-plus';

const authStore = useAuthStore();
const router = useRouter();

let form = reactive({
    email: '',
    password: ''
})

const onSubmit = async () => {
    let pwdRgx = /^[0-9a-zA-Z]{6,20}/
    let emailRgx = /^[a-zA-Z0-9_-]+@[a-zA-Z0-9_-]+(.[a-zA-Z0-9]+)+/
    if(!(emailRgx.test(form.email))){
        // alert('邮箱格式错误');
        ElMessage.info('邮箱格式错误');
        return;
    }
    if(!(pwdRgx.test(form.password))){
        // alert('密码格式错误');
        ElMessage.info('密码格式错误');
        return;
    }
    // axios
    // promise
    // 第一个版本，直接使用axios
    // axios.post("http://127.0.0.1:8000/auth/login",{
    //     email: form.email,
    //     password: form.password
    // }).then(res => {
    //     // then:代表成功的情况（在这里，代表返回的状态码200）
    //     let data = res.data;
    //     let token = data.token;
    //     let user = data.user;
    //     authStore.setUerToken(user,token);
    //     // 登陆成功，跳转到OA系统的首页
    //     router.push({name:"frame"});
    // }).catch((err) =>{
    //     // catch:代表失败的情况（在这里，代表返回的状态码不是200）
    //     let detail = err.response.data.detail
    //     alert(detail)
    // })
    
    // 第二个版本，对axios进行了一层封装
    // authHttp.login(form.email,form.password).then(res => {
    //      let data = res.data;
    //     let token = data.token;
    //     let user = data.user;
    //     authStore.setUerToken(user,token);
    //     // 登陆成功，跳转到OA系统的首页
    //     router.push({name:"frame"});
    // }).catch((err) =>{
    //     // catch:代表失败的情况（在这里，代表返回的状态码不是200）
    //     let detail = err.response.data.detail
    //     alert(detail)
    // })

    // 第三个版本，改成了异步调用的方式
    try{
        let data = await authHttp.login(form.email,form.password);
        let token = data.token;
        let user = data.user;
        authStore.setUerToken(user,token);
        // 登陆成功，跳转到OA系统的首页
        router.push({name:"frame"});
    }catch(detail){
        // alert(detail)
        ElMessage.error(detail)
    }
}

</script>

<template>
    <div class="dowebok">
        <div class="container-login100">
            <div class="wrap-login100">
                <div class="login100-pic js-tilt" data-tilt>
                    <img :src="login_img" alt="IMG" />
                </div>

                <div class="login100-form validate-form">
                    <span class="login100-form-title"> 员工登陆 </span>

                    <div class="wrap-input100 validate-input">
                        <input class="input100" type="text" name="email" placeholder="邮箱" v-model="form.email" />
                        <span class="focus-input100"></span>
                        <span class="symbol-input100">
                            <i class="iconfont icon-fa-envelope" aria-hidden="true"></i>
                        </span>
                    </div>

                    <div class="wrap-input100 validate-input">
                        <input class="input100" type="password" name="password" placeholder="密码" v-model="form.password" />
                        <span class="focus-input100"></span>
                        <span class="symbol-input100">
                            <i class="iconfont icon-fa-lock" aria-hidden="true"></i>
                        </span>
                    </div>

                    <div class="container-login100-form-btn">
                        <button class="login100-form-btn" @click="onSubmit">
                            登陆
                        </button>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<style scoped src="@/assets/css/login.css"></style>
<style scoped src="@/assets/iconfont/iconfont.css"></style>
