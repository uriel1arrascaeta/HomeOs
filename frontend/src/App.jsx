import { Routes, Route } from 'react-router-dom';
import './App.css';
import PostList from './pages/PostList.jsx';
import RootPage from './pages/RootPage.jsx'; // Importamos nuestro nuevo componente "decisor"
import PostDetail from './pages/PostDetail.jsx';
import Register from './pages/Register.jsx';
import Login from './pages/Login.jsx';
import CreatePost from './pages/CreatePost.jsx';
import ScheduleAppointment from './pages/ScheduleAppointment.jsx';
import EditPost from './pages/EditPost.jsx';
import EditProfilePage from './pages/EditProfilePage.jsx';
import AdminDashboard from './pages/AdminDashboard.jsx';
import SellerProfile from './pages/SellerProfile.jsx';

function App() {
  return (
    // Contenedor principal de la aplicación.
    <div className="app-container">
      <main>
        {/* El componente 'Routes' envuelve todas las definiciones de rutas. */}
        <Routes>
          {/* Cada 'Route' mapea una URL ('path') a un componente específico ('element'). */}
          
          {/* Ruta para la página de inicio. */}
          <Route path="/" element={<RootPage />} /> {/* Ahora la ruta raíz usa RootPage */}
          {/* Rutas para el registro e inicio de sesión. */}
          <Route path="/register" element={<Register />} />
          <Route path="/login" element={<Login />} />
          {/* Ruta para la página de agendar citas. */}
          <Route path="/schedule" element={<ScheduleAppointment />} />
          {/* Ruta para editar un post. ':slug' es un parámetro dinámico. */}
          <Route path="/edit-post/:slug" element={<EditPost />} />
          {/* Ruta para editar el perfil del usuario. */}
            <Route path="/edit-profile" element={<EditProfilePage />} />
          {/* Ruta para el panel de control del administrador. */}
            <Route path="/admin-dashboard" element={<AdminDashboard />} />
          {/* Ruta para crear un nuevo post. */}
          <Route path="/create-post" element={<CreatePost />} />
          {/* Ruta para el perfil del usuario (corredor o comprador). */}
          <Route path="/profile" element={<SellerProfile />} />
          {/* Ruta para el blog (lista de posts). */}
          <Route path="/blog" element={<PostList />} />
          {/* Ruta para ver el detalle de un post específico. */}
          <Route path="/post/:slug" element={<PostDetail />} />
        </Routes>
      </main>
    </div>
  );
}

export default App;
