// frontend/src/pages/HomePage/HomePage.js
import React, { useState, useEffect } from 'react';
import PropertyCard from '../components/property/PropertyCards';
import './HomePage.css';
import Navbar from '../components/navbar'; // Importamos el Navbar
import Footer from '../components/footer'; // Importamos el Footer

// URL de la API, igual que en tus otros archivos.
const API_URL = import.meta.env.VITE_API_URL || 'http://127.0.0.1:8000/api/v1/blog';

const HomePage = () => {
  // Estados para guardar los posts, el estado de carga y los errores.
  const [posts, setPosts] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  // useEffect se ejecuta cuando el componente se monta (carga por primera vez).
  useEffect(() => {
    const fetchPosts = async () => {
      try {
        // Hacemos la petición a la API para obtener todos los posts.
        const response = await fetch(`${API_URL}/posts/`);
        if (!response.ok) {
          throw new Error('No se pudieron cargar las propiedades.');
        }
        const data = await response.json();
        setPosts(data); // Guardamos los posts en nuestro estado.
      } catch (err) {
        setError(err.message);
      } finally {
        setLoading(false); // Dejamos de cargar, ya sea con éxito o con error.
      }
    };

    fetchPosts();
  }, []); // El array vacío asegura que esto se ejecute solo una vez.

  // Dividimos los posts en dos secciones para el ejemplo.
  // En un futuro, tu API podría devolver directamente 'destacados' y 'recomendados'.
  const featuredProperties = posts.slice(0, 3);
  const recommendedProperties = posts.slice(3, 8);

  return (
    <div className="bg-white antialiased">
      <Navbar /> {/* Añadimos el Navbar al principio */}
      <div className="home-page">
        <section className="property-section">
          <h2 className="section-title">Propiedades Destacadas</h2>
          {loading && <p>Cargando propiedades...</p>}
          {error && <p className="text-red-500">{error}</p>}
          <div className="cards-container">
            {featuredProperties.map(prop => (
              <PropertyCard
                key={prop.id}
                // Mapeamos los datos de la API a las props del componente
                imageUrl={prop.image} // Tu API devuelve 'image'
                price={prop.price || '$ Consultar'} // Usamos un valor por defecto si no hay precio
                address={prop.title} // Usamos el título como dirección por ahora
              />
            ))}
          </div>
        </section>

        <section className="property-section">
          <h2 className="section-title">Propiedades Recomendadas</h2>
          <div className="cards-container">
            {recommendedProperties.map(prop => (
              <PropertyCard
                key={prop.id}
                imageUrl={prop.image}
                price={prop.price || '$ Consultar'}
                address={prop.title}
              />
            ))}
          </div>
        </section>
      </div>
      <Footer /> {/* Añadimos el Footer al final */}
    </div>
  );
};

export default HomePage;
