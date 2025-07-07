import { useContext } from "react";
import { AuthContext } from "../context/AuthContext";


export default function MainNavigation(){
    const { logout } = useContext(AuthContext);
    return(
        <>
            <h1>Job List</h1>
            <button onClick={logout}>Logout</button>
        </>
    )
}