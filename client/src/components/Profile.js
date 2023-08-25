import React, { useContext } from 'react'
import { UserContext } from './UseContext'

function Title() {
    const { user, setUser } = useContext(UserContext)
    const handleLogOut = (e) => {
        setUser(null)
    }
    const handleDelete = (e) => {
        if (window.confirm('Are you sure you want to delete this user?')) {
            fetch(`/users/${user.id}`, {
                method: 'DELETE',
            })
                .then(response => {
                    if (response.ok) {
                        // Handle successful deletion, e.g., show a success message
                        console.log('Your account was deleted successfully.');
                        // Perform any additional actions after deletion if needed
                    } else {
                        // Handle error, e.g., show an error message
                        console.error('Error deleting user.');
                    }
                })
                .catch(error => {
                    console.error('Error:', error);
                });
        }
    };



    return (
        <div>
            <h1>Staying Alive</h1>
            <button onClick={handleDelete}>Delete Your Profile</button>
            {user ?
                <div>
                    <h4>Welcome Back, {user.name}!</h4>
                    <button onClick={handleLogOut}>Sign Out</button>
                </div>
                : ''
            }
        </div>

    )
}

export default Title