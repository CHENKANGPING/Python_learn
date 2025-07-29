import axios from 'axios';

class Http {
    constructor() {
        this.instance = axios.create({
            baseURL: import.meta.env.VITE_BASE_URL,
            timeout: 10000,
        });
    }

    post(path, data) {
        // path: /auth/login
        // url: http://127.0.0.1:8000/auth/login
        return this.instance.post(path, data);
    }

    get(path,params) {
        return this.instance.get(path,{params});
    }
}
export default new Http();