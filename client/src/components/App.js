import React from 'react';
import { useState, useContext, useEffect } from 'react';
import Home from './Home';
import Header from './Header';
import NavBar from './NavBar';
import Inventory from './Inventory';
import Documents from './Documents';
import Senarios from './Scenarios';
import NotFound from './NotFound';
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
                <Header className='root' />
                {user ? <NavBar /> : ''}
                <Switch>
                    <Route exact path="/">
                        <Home />
                    </Route>
                    <Route exact path="/home">
                        <Home />
                    </Route>
                    <Route exact path="/inventory">
                        <Inventory />
                    </Route>
                    <Route exact path="/medicaldocs">
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