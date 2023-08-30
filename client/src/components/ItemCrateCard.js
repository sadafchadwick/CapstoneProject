import React from 'react';
import '../styling/itemcard.css'

function ItemCrateCard({ itemcrate }) {

    const deleteItem = (deletedId) => {
        fetch('/itemcrate/${deletedId}',
            { method: 'DELETE' })
            .then(() => console.log("this is deleted"))
            .catch(error => console.error('Error:', error))
    }

    const addItem = () => {
        console.log('i work')
    }

    return (
        <div className="card">
            <h2>{itemcrate.name}</h2>
            <h3>{itemcrate.category.name}</h3>
            <h3>{itemcrate.amount}</h3>
            <button onClick={addItem}>Add item to MyStockpile</button>
        </div>
    )

}

export default ItemCrateCard