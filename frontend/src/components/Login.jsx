import { useState, useContext } from "react";
import { AuthContext } from "../context/AuthContext";
import { useNavigate } from "react-router-dom";


export default function Login(){
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');


    const {login} = useContext(AuthContext);
    const navigate = useNavigate();

    const handleSubmit = async (e)=>{
        e.preventDefault();
        await login(email, password);
        navigate('/home');
    }


    return (
        <form onSubmit={handleSubmit}>
            <h2>Login</h2>
            <div>
                <label htmlFor="email">Email</label>
                <input type="email" name="email" id="email" value={email} onChange={(e)=>setEmail(e.target.value)} />
            </div>
            <div>
                <label htmlFor="password">Password</label>
                <input type="password" name="password" id="password" value={password} onChange={(e)=>setPassword(e.target.value)} />
            </div>
            <button type="submit">Login</button>
        </form>
    )
}
