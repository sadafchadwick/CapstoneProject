import React, { useContext, useState } from 'react'
import { useHistory } from 'react-router-dom'
import { UserContext } from './UseContext'

function Profile() {
    const { user, setUser } = useContext(UserContext)
    const [newName, setNewName] = useState('')
    const [newUsername, setNewUsername] = useState('')
    const [newPassword, setNewPassword] = useState('')
    const history = useHistory()

    const handleLogOut = (e) => {
        setUser(null)
        history.push('/login')
        window.confirm('Logged out successfully')
    }

    const handleNameChange = event => {
        setNewName(event.target.value);
    };

    const handleUpdateName = async () => {
        if (newName.trim() === '') return;
        try {
            const response = await fetch(`/users/${user.id}`, {
                method: 'PATCH',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ name: newName }),
            });

            if (response.ok) {
                setUser(prevUser => ({ ...prevUser, name: newName }));
                setNewName('');
                window.confirm('Name updated successfully')
            } else {
                console.error('Failed to update name');
                window.confirm('Failed to update name')
            }
        } catch (error) {
            console.error('Error updating name:', error);
            window.confirm('Error updating name:', error)
        }
    };

    const handleUsernameChange = event => {
        setNewUsername(event.target.value);
    };

    const handleUpdateUsername = async () => {
        if (newUsername.trim() === '') return;
        try {
            const response = await fetch(`/users/${user.id}`, {
                method: 'PATCH',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ username: newUsername }),
            });

            if (response.ok) {
                setUser(prevUser => ({ ...prevUser, username: newUsername }));
                setNewUsername('');
                window.confirm('Username updated successfully')
            } else {
                console.error('Failed to update username')
                window.confirm('Failed to update username');
            }
        } catch (error) {
            console.error('Error updating username:', error);
            window.confirm('Error updating username:', error)
        }
    };

    const handlePasswordChange = event => {
        setNewPassword(event.target.value);
    };

    const handleUpdatePassword = async () => {
        if (newPassword.trim() === '') return;

        try {
            const response = await fetch(`/users/${user.id}`, {
                method: 'PATCH',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ password_hash: newPassword }),
            });

            if (response.ok) {
                setNewPassword('');
                console.log('Password changed ')
                window.confirm('Password updated successfully')
            } else {
                console.error('Failed to update password');
                window.confirm('Failed to update password')
            }
        } catch (error) {
            console.error('Error updating Password:', error);
            window.confirm('Error updating Password:', error)
        }
    };

    const handleDelete = (e) => {
        if (window.confirm('Are you sure you want to delete this user?')) {
            fetch(`/users/${user.id}`, {
                method: 'DELETE',
            })
                .then(response => {
                    if (response.ok) {
                        setUser(null)
                        history.push('signup')
                        window.confirm('Your account was deleted successfully.');
                    } else {
                        console.error('Error deleting user.');
                        window.confirm('Error deleting user.')
                    }
                })
                .catch(error => {
                    console.error('Error:', error);
                    window.confirm('Error:', error)
                });
        }
    };

    return (
        <div>
        
            {user ? (
                <>
                    <h3>Welcome Back, {user.name}!</h3>
                    <h4>User Name: {user.username}</h4>
                    <input
                        placeholder='New Name'
                        type="text"
                        id="name"
                        value={newName}
                        onChange={handleNameChange}
                    />
                    <button onClick={handleUpdateName}>Edit Your Name</button>
                    <input
                        placeholder='New Username'
                        type="text"
                        id="username"
                        value={newUsername}
                        onChange={handleUsernameChange}
                    />
                    <button onClick={handleUpdateUsername}>Edit Your Username</button>
                    <input
                        placeholder='New Password'
                        type="text"
                        id="password"
                        value={newPassword}
                        onChange={handlePasswordChange}
                    />
                    <button onClick={handleUpdatePassword}>Edit Your Password</button>
                    <button onClick={handleDelete}>Delete Your Profile</button>
                    <button onClick={handleLogOut}>Sign Out</button>
                </>
            ) : (
                // history.push('/login')
                <p>funtimes</p>
            )}
        </div>
    );
}

export default Profile;