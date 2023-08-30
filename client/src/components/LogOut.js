// import React from 'react';
// import {useContext} from 'react'
// import { useHistory } from 'react-router-dom'
// import { UserContext } from './UseContext'

// function LogOut() {
//     const { user, setUser } = useContext(UserContext)
//     const history = useHistory()

//     const handleLogOut = (e) => {
//         fetch('/logout', {
//             method: 'DELETE',
//         }).then(() => {
//             setUser(null)
//             window.confirm('Logged out successfully')
//         })
//         history.push('/login')
//     }
    
//     return (
//         <div>
//             {user ? (
//                 <button onClick={handleLogOut}>Sign Out</button>
//                 ):(
//                 history.push('/login')
//                 )}
//         </div>
//     )
// }

// export default LogOut