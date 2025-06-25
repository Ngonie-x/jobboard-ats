import { useContext } from 'react';
import { AuthContext } from '../context/AuthContext';
import Home from '../components/Home';

const HomePage = () => {
    const { logout } = useContext(AuthContext);

    return (
        <>
            <div>
                <h1>Job List</h1>
                <button onClick={logout}>Logout</button>
            </div>
            <Home/>
        </>
        
    );
};

export default HomePage;