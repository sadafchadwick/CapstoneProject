import React from 'react';
import { NavLink } from 'react-router-dom';
import '../styling/navbar.css';

const NavBar = () => {
    return (
        <div className='hovernav-bar'>
            <nav className='nav-list'>
                <NavLink to="/profile">Profile</NavLink>
                <NavLink to="/itemcrate">My Stockpile</NavLink>
                <NavLink to="/items">Generic items list</NavLink>
                <NavLink to="/documents">Survival Documents</NavLink>
                {/* <NavLink to="/logout">LogOut</NavLink> */}
            </nav>
        </div>
    )
}

export default NavBar