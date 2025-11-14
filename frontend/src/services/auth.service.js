import {apiService} from "./api.service";
import {urls} from "../constants/urls";

const authService = {
    async login(user) {
        const {data: {access, refresh}} = await apiService.post(urls.auth.login, user);
        localStorage.setItem('access', access)
        localStorage.setItem('refresh', refresh)
    },

    getSocketToken() {
        return apiService.get(urls.auth.socket)
    }


}

export {
    authService
}