import React from 'react';
// import { useState } from 'react';
import Home from './Home';
import Header from './Header';
import NavBar from './NavBar';
import Inventory from './Inventory';
import Documents from './Documents';
import Senarios from './Senarios';
import NotFound from './NotFound';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import { UserProvider } from './UseContext';
import 'bootstrap/dist/css/bootstrap.min.css';

function App() {
    //here for useContext
    // const [user, setUser] = useState(null)

    return (
        <Router>
            <Header className='root'/>
            <UserProvider>
                <NavBar />
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
                    <Route exact path="/senarios">
                        <Senarios />
                    </Route>
                    <Route path="*">
                        <NotFound />
                    </Route>
                </Switch>
            </UserProvider>
        </Router>
    )
}

export default App