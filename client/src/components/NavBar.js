import React from 'react';
// import { NavLink } from 'react-router-dom';
import '../styling/navbar.css';

const NavBar = () => {
    return (
        <div className='hovernav-bar'>
            <nav className='nav-list'>
                <a className='glow' href="/profile">Profile</a>
                <a className='glow' href="/itemcrate">My Stockpile</a>
                <a className='glow' href="/items">Generic items list</a>
                <a className='glow' href="/documents">Survival Documents</a>
                <a className='glow' href="/scenarios">Scenarios</a>
            </nav>
        </div>
    )
}

export default NavBar