import { createContext, useState, useEffect } from "react";
import axios from 'axios';



const AuthContext = createContext();

const AuthProvider = ({children})=>{
    const [auth, setAuth] = useState({
        token: localStorage.getItem("token"),
        refreshToken: localStorage.getItem("refreshToken"),
        isAuthenticated: null,
        isLoading: true
    });

    const login = async (email, password)=>{
        try{
            const response = await axios.post('http://127.0.0.1:8000/api/token/', {email, password});
            
            const {refresh, access} = response.data;
            localStorage.setItem('token', access);
            localStorage.setItem('refreshToken', refresh);
            setAuth({
                token: access,
                refreshToken: refresh,
                isAuthenticated: true,
                isLoading: false
            })
        }catch(error){
            console.error("Login failed: ", error);
            setAuth({
                ...auth,
                isAuthenticated: false,
                isLoading: false
            })
        }
    }


    const logout = () =>{
        localStorage.removeItem('token');
        localStorage.removeItem('refreshToken');
        setAuth({
            token: null,
            refreshToken: null,
            isAuthenticated: false,
            isLoading: false
        })
    }



    // effect will run on load to check authentication status
    useEffect(()=>{
        const token = localStorage.getItem('token');
        if (token){
            setAuth({
                ...auth,
                isAuthenticated: true,
                isLoading: false
            })
        }else{
            setAuth({...auth,
            isAuthenticated: false,
            isLoading: false})
        }
    }, []);

    return (
        <AuthContext.Provider value={{auth, login, logout}}>
            {!auth.isLoading && children}
        </AuthContext.Provider>
    )
}


export {AuthContext, AuthProvider}