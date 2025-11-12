import {apiService} from "./api.service";
import {urls} from "../constants/urls";

const authService = {
    async login(user) {
        const {data: {access}} = await apiService.post(urls.auth.login, user);
        localStorage.setItem('access', access)
    },

    getSocketToken() {
        return apiService.get(urls.auth.socket)
    }

}

export {
    authService
}