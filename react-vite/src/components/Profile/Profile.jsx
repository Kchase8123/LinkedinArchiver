// src/components/Profile.jsx
import React, { useState, useEffect } from 'react';
import axios from 'axios';
import './Profile.css';

const Profile = () => {
  const [profile, setProfile] = useState(null);

  useEffect(() => {
    axios.get('/api/linkedin/profile')
      .then(response => setProfile(response.data))
      .catch(error => console.error(error));
  }, []);

  return (
    <div>
      <h2>LinkedIn Profile</h2>
      {profile && (
        <div>
          <p>Name: {profile.localizedFirstName} {profile.localizedLastName}</p>
          <p>Headline: {profile.headline}</p>
        </div>
      )}
    </div>
  );
};

export default Profile;
