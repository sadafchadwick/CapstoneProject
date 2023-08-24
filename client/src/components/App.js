import { BrowserRouter as Router, Switch, Route, Routes, Navigate } from 'react-router-dom'
import Header from './Header'
import NavBar from './NavBar'
import Profile from './Profile'
import Inventory from './Inventory'
import Documents from './Documents'
import Authentication from './Authentication';
import React from 'react';

import '../styling/app.css'; 



function App() {
  return (
    <Router>
      <Header />
      <NavBar />
      <Routes>
        <Route path="/" element={<Navigate to="/auth" />} />
        <Route path="/authentication" element={<Authentication />} />
        <Route path="/*" element={<AuthenticatedRoutes />} />
      </Routes>
  </Router>
  );
}

function AuthenticatedRoutes() {

  return (
    <>
      <div className="app-background"></div>
      {<NavBar />}
      <Routes>
        <Route path="/profile/:userId" element={<Profile />} />
        <Route path="/profile/:userId/inventory" element={<Inventory />} />
        <Route path="/profile/:userId/medicaldocs" element={<Documents />} />
        {/* Add more routes here */}
      </Routes>
    </>
  );
}
{/* <Navigate to="/auth" /> */}


export default App;