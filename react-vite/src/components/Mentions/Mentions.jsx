// src/components/Mentions.jsx
import React, { useState, useEffect } from 'react';
import axios from 'axios';
import './Mentions.css';

const Mentions = () => {
  const [mentions, setMentions] = useState([]);

  useEffect(() => {
    axios.get('/api/linkedin/mentions')
      .then(response => setMentions(response.data))
      .catch(error => console.error(error));
  }, []);

  return (
    <div>
      <h2>Mentions</h2>
      <ul>
        {mentions.map(mention => (
          <li key={mention.id}>{mention.content}</li>
        ))}
      </ul>
    </div>
  );
};

export default Mentions;
