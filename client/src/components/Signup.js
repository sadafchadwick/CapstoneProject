import React, { useContext } from 'react';
import { useState } from 'react';
import { useHistory } from 'react-router-dom';
import { UserContext } from './UseContext';
import 'bootstrap/dist/css/bootstrap.min.css';
import '../styling/index.css'


function Signup() {

    const history = useHistory()

    const [userName, setUserName] = useState('')
    const [name, setName] = useState('')
    const [password, setPassword] = useState('')

    const { setUser } = useContext(UserContext)

    function handleSubmit(e) {
        e.preventDefault();
        const formObj = {
            'name': name,
            'username': userName,
            'password': password
        }

        fetch('/users', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(formObj)
        })
            .then(r => {
                if (r.ok) {
                    r.json()
                        .then(data => {
                            history.push('/home')
                            setUser(data)
                        })
                }
                else {
                    r.json()
                        .then(data => {
                            console.log(data)
                        })
                }
            })
    }

    return (
        <div className="auth-wrapper">
            <form onSubmit={handleSubmit}>
                <input
                    placeholder='Name'
                    type="text"
                    id="name"
                    value={name}
                    onChange={(e) => setName(e.target.value)}
                />

                <input
                    placeholder='Username'
                    type="text"
                    id="userName"
                    value={userName}
                    onChange={(e) => setUserName(e.target.value)}
                />

                <input
                    placeholder='Password'
                    type="password"
                    id="password"
                    value={password}
                    onChange={(e) => setPassword(e.target.value)}
                />

                <button type="submit">Signup</button>
            </form>
        </div>
    )
}

export default Signup