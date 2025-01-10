// src/components/Comments.jsx
import React, { useState, useEffect } from 'react';
import axios from 'axios';
import './Comments.css';

const Comments = () => {
  const [comments, setComments] = useState([]);

  useEffect(() => {
    axios.get('/api/linkedin/comments')
      .then(response => setComments(response.data))
      .catch(error => console.error(error));
  }, []);

  return (
    <div>
      <h2>Comments</h2>
      <ul>
        {comments.map(comment => (
          <li key={comment.id}>{comment.content}</li>
        ))}
      </ul>
    </div>
  );
};

export default Comments;
