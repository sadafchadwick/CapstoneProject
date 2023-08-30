import React from 'react';
import '../styling/itemcard.css'

function ItemCard({ item }) {


    const addItem = () => {
        fetch('/login', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(formObj)
        })
            .then(r => {
                if (r.ok) {
                    r.json()
                        .then(data => {
                            setUser(data)
                            window.confirm("Item added to your stockpile")
                        })
                }
                else {
                    r.json()
                        .then(data => {
                            console.error('error logging in')
                            window.confirm("Username or password do not match")
                        })
                }
            })
        
    }

    return (
        <div className="card">
            <h2>{item.name}</h2>
            <img src={item.image_url}></img>
            <h3>{item.category.name}</h3>
            <h3>{item.amount}</h3>

            <button onClick={addItem}>Add item to MyStockpile</button>
        </div>
    )

}

export default ItemCard