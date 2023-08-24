import React, { useContext } from 'react'
import { UserContext } from './UseContext'

function Title() {
    const { user, setUser } = useContext(UserContext)
    const handleLogOut = (e) => {
        setUser(null)
    }

    return (
        <div>
            <h1>Staying Alive</h1>
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










// import React, { useState, useEffect } from 'react';
// import { useParams } from 'react-router-dom';
// import '../styling/profile.css';
// import { mockUsers } from '../mockData';

// function Profile() {
//     const { userId } = useParams();

//     const [userData, setUserData] = useState({});
//     const [newUsername, setNewUsername] = useState('');
//     const [newPassword, setNewPassword] = useState('');
//     const [showChangeUsername, setShowChangeUsername] = useState(false);
//     const [showChangePassword, setShowChangePassword] = useState(false);

//     useEffect(() => {
//         // Fetch user data or set it using mock data
//         const user = mockUsers.find(user => user.id === parseInt(userId));
//         if (user) {
//             setUserData(user);
//         }
//     }, [userId]);

//     const handleUsernameChange = event => {
//         setNewUsername(event.target.value);
//     };

//     const handlePasswordChange = event => {
//         setNewPassword(event.target.value);
//     };

//     const handleUpdateUsername = () => {
//         // Update username logic
//         if (newUsername.trim() !== '') {
//             // Update username logic
//             setUserData(prevUserData => ({ ...prevUserData, username: newUsername }));
//             setNewUsername('');
//         }
//     };

//     const handleUpdatePassword = () => {
//         // Update password logic
//         if (newPassword.trim() !== '') {
//             // Update password logic
//             setNewPassword('');
//         }
//     };

//     return (
//         <div className='profile-wrapper'>
//             <div className="profile-container">
//                 <h1 className="profile-title">Welcome to the Fight Club, {userData.username}</h1>
//                 <div className="profile-info">
//                     <p>Wins: {userData.wins}</p>
//                     <p>Losses: {userData.losses}</p>
//                     <p>Winrate: {userData.winrate}</p>
//                 </div>

//                 <div className="toggle-username">
//                     <button className="toggle-button" onClick={() => setShowChangeUsername(!showChangeUsername)}>Change Username</button>
//                     {showChangeUsername && (
//                         <div className="profile-section">
//                             <h3>Change Username</h3>
//                             <input
//                                 type="text"
//                                 placeholder="New Username"
//                                 value={newUsername}
//                                 onChange={handleUsernameChange}
//                                 className="custom-input"
//                             />
//                             <button className="update-button" onClick={handleUpdateUsername}>Update Username</button>
//                         </div>
//                     )}
//                 </div>

//                 <div className="toggle-password">
//                     <button className="toggle-button" onClick={() => setShowChangePassword(!showChangePassword)}>Change Password</button>
//                     {showChangePassword && (
//                         <div className="profile-section">
//                             <h3>Change Password</h3>
//                             <input
//                                 type="password"
//                                 placeholder="New Password"
//                                 value={newPassword}
//                                 onChange={handlePasswordChange}
//                                 className="custom-input"
//                             />
//                             <button className="update-button" onClick={handleUpdatePassword}>Update Password</button>
//                         </div>
//                     )}
//                 </div>
//             </div>
//         </div>
//     );

// }

// export default Profile;