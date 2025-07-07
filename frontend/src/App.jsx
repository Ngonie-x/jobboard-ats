import './App.css';
import { createBrowserRouter, RouterProvider } from 'react-router-dom';
import LoginPage from './pages/LoginPage';
import HomePage from './pages/HomePage';
import JobDetailPage from './pages/JobDetailPage';
import { loader as jobLoader } from './pages/JobDetailPage';
import PrivateRoute from './components/PrivateRoute';
import Root from './pages/Root';

const router = createBrowserRouter([
  {
    path: '/login',
    element: <LoginPage />,
  },
  {
    path: '/',
    element: <Root />,
    children: [
      {
        index: true,
        element: <PrivateRoute><HomePage /></PrivateRoute>
      },
      {
        path: 'jobs/:id',
        element: <PrivateRoute><JobDetailPage /></PrivateRoute>,
        loader: jobLoader
      }
    ]
  }
]);

function App() {
  return <RouterProvider router={router} />;
}

export default App;