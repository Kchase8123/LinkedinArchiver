// src/components/Transfers.jsx
import React, { useState, useEffect } from 'react';
import axios from 'axios';
import './Transfers.css';

const Transfers = () => {
  const [transfers, setTransfers] = useState([]);

  useEffect(() => {
    axios.get('/api/linkedin/transfers')
      .then(response => setTransfers(response.data))
      .catch(error => console.error(error));
  }, []);

  return (
    <div>
      <h2>Data Transfers</h2>
      <ul>
        {transfers.map(transfer => (
          <li key={transfer.id}>{transfer.status}</li>
        ))}
      </ul>
    </div>
  );
};

export default Transfers;
