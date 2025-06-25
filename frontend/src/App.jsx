import './App.css'
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom'
import LoginPage from './pages/LoginPage';
import HomePage from './pages/HomePage';
import PrivateRoute from './components/PrivateRoute';


function App() {

  return (
    <Router>
      <Routes>
        <Route path='/login' element={<LoginPage/>} />
        <Route path='/home' element={<PrivateRoute><HomePage/></PrivateRoute>} />
        <Route path="/" element={<LoginPage />} />
      </Routes>
      
    </Router>
  )
}

export default App
