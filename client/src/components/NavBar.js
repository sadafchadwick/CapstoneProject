import React from 'react';
import { NavLink } from 'react-router-dom';


const NavBar = () => {
    // const navigate = useNavigate()
    return (
        <nav>
            <NavLink className="glow" href="#" to="/">HOME</NavLink>
            <NavLink to="/inventory">My Stockpile</NavLink>
            <NavLink to="/medicaldocs">Survival Documents</NavLink>
            <NavLink to="/senarios">Senarios</NavLink>
            <div className='hovernav-bar'></div>
        </nav>
    )
}

export default NavBar;