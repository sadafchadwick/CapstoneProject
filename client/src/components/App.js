import React from 'react';
import { useState, useContext, useEffect } from 'react';
import Home from './Home';
import NavBar from './NavBar';
import Inventory from './Inventory';
import Documents from './Documents';
import Senarios from './Scenarios';
import NotFound from './NotFound';
import Profile from './Profile'
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import { UserContext, UserProvider } from './UseContext';
import 'bootstrap/dist/css/bootstrap.min.css';


function App() {
    //here for useContext
    const { user, setUser } = useContext(UserContext)
    
    useEffect(()=>{
        fetch ('/check_session')
        .then(r=>{
            if (r.ok){
                r.json() .then(userObj=>setUser(userObj))
            }
        })
    },[setUser])

    console.log(user)
    return (
        <Router>
                {user ? <NavBar /> : ''}
                <Switch>
                    <Route exact path="/home">
                        <Home />
                    </Route>
                    <Route exact path="/profile">
                        <Profile />
                    </Route>
                    <Route exact path="/inventory">
                        <Inventory />
                    </Route>
                    <Route exact path="/documents">
                        <Documents />
                    </Route>
                    <Route exact path="/scenarios">
                        <Senarios />
                    </Route>
                    <Route path="*">
                        <NotFound />
                    </Route>
                </Switch>
        </Router>
    )
}



export default App