import React, { useContext, useState, useEffect } from 'react';
import { UserContext } from './UseContext';
import Login from './Login';
import Signup from './Signup';
import Button from 'react-bootstrap/Button';

function Home() {
    const { user, setUser } = useContext(UserContext)
    const [loginSignup, setLoginSignup] = useState(true)

    const handleLoginSignup = (e) => {
        setLoginSignup(!loginSignup)
    }

    const handleLogOut = (e) => {
        fetch('/logout', {
            method: 'DELETE',
        })
        .then(()=>setUser(null))
    }

    return (
        <div>
        <h1>Ready, Set, Survive</h1>
        <h3>....be prepared for every catastrophe!</h3>
            {user ?
                <div>
                    <h3>Welcome Back, {user.name}!</h3>
                    <h4>User Name: {user.username}</h4>
                    <button onClick={handleLogOut}>Sign Out</button>
                </div>
                :
                <div>
                    {loginSignup ?
                        <div>
                            <h1>Login in below!</h1>
                            <Login setUser={setUser} />
                            <Button variant='outline-warning' onClick={handleLoginSignup}>Click here to Sign Up!</Button>
                        </div>
                        :
                        <div>
                        <h1>Sign up today!</h1>
                            <Signup setUser={setUser} />
                            <Button variant='outline-warning' onClick={handleLoginSignup}>Click here to Login!</Button>
                        </div>
                    }
                </div>
            }
        </div>
    )
}

export default Home