import axios from "axios";
import {baseURL, urls} from "../constants/urls";

const apiService = axios.create({baseURL})

apiService.interceptors.request.use(req=>{
    const token = localStorage.getItem('access');

    if (token){
        req.headers.Authorization = `Bearer ${token}`
    }

    return req
})

apiService.interceptors.response.use(
    response => response,
    async error => {
        const originalRequest = error.config;

        // Якщо access token протух і це перша спроба оновлення
        if (error.response?.status === 401 && !originalRequest._retry) {
            originalRequest._retry = true;

            const refresh = localStorage.getItem('refresh');
            if (!refresh) {
                // Користувач не залогінений
                return Promise.reject(error);
            }

            try {
                // Отримуємо новий access
                const {data} = await axios.post(urls.auth.refresh, {refresh});

                localStorage.setItem('access', data.access);
                if (data.refresh) {
                    localStorage.setItem('refresh', data.refresh);
                }

                // Підставляємо новий токен у оригінальний запит
                originalRequest.headers.Authorization = `Bearer ${data.access}`;

                return apiService(originalRequest);
            } catch (e) {
                // Refresh теж протух → логуємо користувача
                localStorage.removeItem('access');
                localStorage.removeItem('refresh');
                window.location.href = '/login';
            }
        }

        return Promise.reject(error);
    }
);


export {
    apiService
}