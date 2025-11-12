import {apiService} from "./api.service";
import {urls} from "../constants/urls";

const pizzaService = {
    getAll(params){
        return apiService.get(urls.pizzas, {params})
    },
    create(data){
        return apiService.post(urls.pizzas, data)
    }
}

export {
    pizzaService
}