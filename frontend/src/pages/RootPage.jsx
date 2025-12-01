// c:\Users\hurie\OneDrive\Escritorio\HomeOs\frontend\src\pages\RootPage.jsx

import React from 'react';
import { useAuth } from '../AuthContext';
import LandingPage from './LandingPage';
import HomePage from './HomePage';

// Este componente actúa como un interruptor.
// Decide qué página mostrar en la ruta raíz ("/")
export default function RootPage() {
  const { isLoggedIn } = useAuth();

  // Si el usuario ha iniciado sesión, muestra la página con las propiedades.
  // Si no, muestra la página de marketing.
  return isLoggedIn ? <HomePage /> : <LandingPage />;
}
