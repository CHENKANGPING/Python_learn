import http from './http';

const login = (email,password) =>{
    const path = '/auth/login';
    return http.post(path,{email,password});
}

const resetPwd = (oldpwd,newpwd,newpwd2) => {
    const path = '/auth/resetpassword';
    return http.post(path,{oldpwd,newpwd,newpwd2});
}

export default {
    login,
    resetPwd
}
