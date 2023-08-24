import React, { useContext, useState, useEffect } from 'react';
import { UserContext } from './UseContext';
import Login from './Login';
import Signup from './Signup';
import Button from 'react-bootstrap/Button';
// import EditUser from './EditUser';

function Home() {
    const { user, setUser } = useContext(UserContext)
    const [loginSignup, setLoginSignup] = useState(true)
    // const [editUser, setEditUser] = useState(false)

    const handleLoginSignup = (e) => {
        setLoginSignup(!loginSignup)
    }

    const handleLogOut = (e) => {
        setUser(null)
    }
    
    // const handleEdit = (e) => {
    //     console.log('edit name')
    //     setEditUser(true)
    // }

    return (
        <div>
            <h2>SIGN UP OR LOGIN IN!</h2>
            {user ? 
                <div>
                    <h3>Welcome Back, {user.name}!</h3>
                    {/* <h4>User ID: {user.id}</h4> */}
                    <h4>User Name: {user.user_name}</h4>
                    {/* {editUser ?
                        <div>
                            <EditUser setEditUser={setEditUser}/>
                        </div>
                        :
                        <div>
                            <button onClick={handleEdit}>Edit User</button>
                        </div>
                    } */}
                    <button onClick={handleLogOut}>Sign Out</button>
                </div>
                : 
                <div>
                    {loginSignup ?
                        <div>
                            <h4>Please Login</h4>
                            <Login setUser={setUser} />
                            <Button variant='outline-warning' onClick={handleLoginSignup}>Click here to Sign Up!</Button>
                        </div>
                        :
                        <div>
                            <h4>Please Sign Up</h4>
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