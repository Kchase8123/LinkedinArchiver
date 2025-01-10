// src/components/Accounts.jsx
import React, { useState, useEffect } from 'react';
import axios from 'axios';
import './Accounts.css';

const Accounts = () => {
  const [accounts, setAccounts] = useState([]);

  useEffect(() => {
    axios.get('/api/linkedin/accounts')
      .then(response => setAccounts(response.data))
      .catch(error => console.error(error));
  }, []);

  return (
    <div>
      <h2>LinkedIn Accounts</h2>
      <ul>
        {accounts.map(account => (
          <li key={account.id}>{account.profile_url} - {account.job_title}</li>
        ))}
      </ul>
    </div>
  );
};

export default Accounts;
