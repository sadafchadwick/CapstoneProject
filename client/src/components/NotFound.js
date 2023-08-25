import React from 'react';
import { Link } from 'react-router-dom';

function NotFound() {
    return (
        <div>
            <h1>Error 404: Not Found</h1>
            <h2>That is not a valid life choice! Rethink your future!</h2>
            <Link to='/home'>
                <button>Go Home</button>
            </Link>
        </div>
    )
}

export default NotFound