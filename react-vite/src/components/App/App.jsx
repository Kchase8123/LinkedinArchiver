// src/components/App.jsx
import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import Navigation from '../Navigation/Navigation';
import Login from '../Login/Login';
import Dashboard from '../Dashboard/Dashboard';
import Accounts from '../Accounts/Accounts';
import Transfers from '../Transfers/Transfers';
import Comments from '../Comments/Comments';
import Mentions from '../Mentions/Mentions';
import Profile from '../Profile/Profile';
import PrivateRoute from '../../router/PrivateRoute';
import { AuthProvider } from '../../context/AuthContext';
import './App.css';

const App = () => {
  return (
    <AuthProvider>
      <Router>
        <Navigation />
        <Switch>
          <Route path="/login" component={Login} />
          <PrivateRoute path="/dashboard" component={Dashboard} />
          <PrivateRoute path="/accounts" component={Accounts} />
          <PrivateRoute path="/transfers" component={Transfers} />
          <PrivateRoute path="/comments" component={Comments} />
          <PrivateRoute path="/mentions" component={Mentions} />
          <PrivateRoute path="/profile" component={Profile} />
          <Route path="/" component={Login} />
        </Switch>
      </Router>
    </AuthProvider>
  );
};

export default App;
