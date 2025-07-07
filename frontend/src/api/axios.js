import axios from "axios";

const api = axios.create({
    baseURL: 'http://127.0.0.1:8000'
});


api.interceptors.request.use(
    (config)=>{
        const token = localStorage.getItem('token');
        if (token){
            config.headers['Authorization'] = `Bearer ${token}`;
        }
        return config;
    },
    (error)=>{
        return Promise.reject(error);
    }
)



// Response interceptor to handle token refresh
api.interceptors.response.use(
    (response) => response,
    async (error) => {
        const originalRequest = error.config;
        if (error.response.status === 401 && !originalRequest._retry) {
            originalRequest._retry = true;
            try {
                const refreshToken = localStorage.getItem('refreshToken');
                const response = await api.post('/api/token/refresh/', {
                    refresh: refreshToken,
                });
                const { access } = response.data;
                localStorage.setItem('token', access);
                api.defaults.headers.common['Authorization'] = `Bearer ${access}`;
                return api(originalRequest);
            } catch (refreshError) {
                // Handle refresh token failure (e.g., redirect to login)
                console.error('Token refresh failed:', refreshError);
                // Here you would likely call the logout function from your AuthContext
                return Promise.reject(refreshError);
            }
        }
        return Promise.reject(error);
    }
);


export const fetchJobs = async ()=>{
    try{
        const response = await api.get('/api/jobs/');
        return response.data
    }catch(error){
        console.log("Failed to fetch jobs: ", error)
    }
}


export const fetchJob = async (id) =>{
    try{
        const response = await api.get(`api/jobs/${id}/`);
        return response.data;
    }catch(error){
        console.log("Failed to fetch job:", error);
    }
}


export default api;