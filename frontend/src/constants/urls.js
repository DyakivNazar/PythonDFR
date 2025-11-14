const baseURL = '/api'

const auth = '/auth'
const pizzas = '/pizzas'

const urls = {
    auth: {
        login: auth,
        socket: `${auth}/socket`,
        refresh: `${auth}/refresh`
    },
    pizzas
}

export {
    baseURL,
    urls
}