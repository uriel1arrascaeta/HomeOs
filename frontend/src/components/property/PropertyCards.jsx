// frontend/src/components/property/PropertyCard.js
import React from 'react';
import './PropertyCards.css'; // <-- ¡AÑADE ESTA LÍNEA!

const PropertyCard = ({ imageUrl, price, address }) => {
  return (
    <div className="property-card">
      <img src={imageUrl} alt={`Propiedad en ${address}`} className="property-card-image" />
      <div className="property-card-body">
        <h3 className="property-card-price">{price}</h3>
        <p className="property-card-address">{address}</p>
      </div>
    </div>
  );
};

export default PropertyCard;
