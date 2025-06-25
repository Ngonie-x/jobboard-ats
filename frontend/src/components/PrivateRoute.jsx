import { useContext } from "react";
import { Navigate } from "react-router-dom";
import { AuthContext } from "../context/AuthContext";

export default function PrivateRoute({children}){
    const {auth} = useContext(AuthContext);

    if (auth.isLoading){
        return <div>Loading</div>
    }

    return auth.isAuthenticated ? children : <Navigate to='/login'/>
}