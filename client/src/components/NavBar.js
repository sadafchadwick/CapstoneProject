import React from 'react';
import { NavLink } from 'react-router-dom';
import '../styling/navbar.css';

const NavBar = () => {
    return (
        <div className='navbar-container'>
            <nav className='nav-list'>
                <NavLink to="/profile" activeClassName="active-link">Profile</NavLink>
                <NavLink to="/itemcrate" activeClassName="active-link">My Stockpile</NavLink>
                <NavLink to="/items" activeClassName="active-link">Items list</NavLink>
            </nav>
        </div>
    )
}

export default NavBar;
