import React, { useState } from 'react';
// import { Link, Navigate } from 'react-router-dom';
import '../styling/authentication.css';
import { useNavigate } from 'react-router-dom';

const Authentication = ({ isSignup }) => {
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const [loggedIn, setLoggedIn] = useState(false);
    // const [isSignupMode, setIsSignupMode] = useState(false);
    const [errorMessage, setErrorMessage] = useState('');
    const [signupSuccess, setSignupSuccess] = useState(false);
    const navigate = useNavigate();

    // const handleModeToggle = () => {
    //     setIsSignupMode(!isSignupMode);
    //     setErrorMessage('');
    //     setSignupSuccess(false);
    // };

    const handleLogin = async () => {
        try {
            const response = await fetch('http://localhost:5555/login', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ username, password }),
            });

            if (response.status === 200) {
                const data = await response.json();
                navigate(`/profile/${username.id}`); // Use data.user_id here
            } else {
                setErrorMessage('Invalid username or password.');
            }
        } catch (error) {
            console.error('Login error:', error);
        }
    };

    const handleSignup = async () => {
        if (username.length < 5 || password.length < 5) {
            setErrorMessage('Username and password must be at least 5 characters.');
            return;
        }

        try {
            const response = await fetch('http://localhost:5555/signup', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ username, password }),
            });

            if (response.status === 201) {
                setSignupSuccess(true);
                setErrorMessage('');
            } else {
                setErrorMessage('Username already exists. Please choose a different username.');
            }
        } catch (error) {
            console.error('Signup error:', error);
        }
    };

    if (loggedIn) {
        navigate(`/profile/${username.id}`); // Use data.user_id here
        return null;
    }

    return (
        <div className="container">
            {/* ... (rest of your code) */}
        </div>
    );
};

export default Authentication;
