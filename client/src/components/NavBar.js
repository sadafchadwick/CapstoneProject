import React from 'react';
import { NavLink } from 'react-router-dom';


const NavBar = () => {
    // const navigate = useNavigate()
    return (
    <nav>
        <NavLink to="/">HOME</NavLink>
        <NavLink to="/inventory">My Stockpile</NavLink>
        <NavLink to="/medicaldocs">Survival Documents</NavLink>
        <NavLink to="/senarios">Senarios</NavLink>
    </nav>
    )
}

export default NavBar;