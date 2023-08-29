import React from 'react';
import { useContext, useEffect } from 'react';
import Home from './Home';
import NavBar from './NavBar';
import Item from './Item';
import Documents from './Documents';
import Senarios from './Scenarios';
import NotFound from './NotFound';
import Profile from './Profile';
import Inventory from './Inventory'
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import { UserContext } from './UseContext';
import 'bootstrap/dist/css/bootstrap.min.css';


function App() {
    const { user, setUser } = useContext(UserContext)

    useEffect(() => {
        fetch('/check_session')
            .then(r => {
                if (r.ok) {
                    r.json().then(userObj => setUser(userObj))
                }
            })
    }, [setUser])


    console.log(user)
    return (
        <Router>
            {user ? <NavBar /> : ''}
            <Switch>
                <Route exact path="/">
                    <Home />
                </Route>
                <Route exact path="/home">
                    <Home />
                </Route>
                <Route exact path="/login">
                    <Profile />
                </Route>
                <Route exact path="/profile">
                    <Profile />
                </Route>
                <Route exact path="/items">
                    <Item />
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