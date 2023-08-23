import React from "react";
import { NavLink, useNavigate } from "react-router-dom"

const NavBar = () => {
    // const navigate = useNavigate()
    return (
    <nav>
        <div className="glow-on-hover">
        <NavLink className="nav-button" to="/">HOME</NavLink>
        </div>
        <div className="glow-on-hover">
        <NavLink className="nav-button" to="/Inventory">My Stockpile</NavLink>
        </div>
        <div className="glow-on-hover">
        <NavLink className="nav-button" to="/medicaldocs">Survival Documents</NavLink>
        </div>
        {/* <NavLink to="/supplies">Supply List</NavLink>
        <NavLink to="/resources">Resources</NavLink> */}
        
    </nav>
    )
}

export default NavBar;