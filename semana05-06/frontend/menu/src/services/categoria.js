import axios from 'axios'

const api = axios.create({baseURL:'http://127.0.0.1:5000'})

export async function listarCategorias (){
    const request = await api.get('/categorias')
    return request.data
}