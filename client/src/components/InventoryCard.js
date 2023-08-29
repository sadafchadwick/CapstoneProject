import React from 'react';
import '../styling/itemcard.css'

function InventoryCard({inventory}) {

    const deleteItem = (deletedId) => {
        fetch('/inventory/${deletedId}',
            {method: 'DELETE'})
        .then(() => console.log("this is deleted"))
        .catch(error => console.error('Error:', error))
    }

    const addItem = () => {
        console.log('i work')
    }

    return (
        <div className="card">
            <h2>{inventory.name}</h2>
            <h3>{inventory.category.name}</h3>
            <h3>{inventory.amount}</h3>
            <button onClick={addItem}>Add item to MyStockpile</button>
        </div>
    )

}

export default InventoryCard