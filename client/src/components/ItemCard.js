import React from 'react';
import '../styling/itemcard.css'

function ItemCard({item}) {


    const addItem = () => {
        console.log('i work')
    }

    return (
        <div className="card">
            <h2>{item.name}</h2>
            <h3>{item.category.name}</h3>
            <h3>{item.amount}</h3>
            <button onClick={addItem}>Add item to MyStockpile</button>
        </div>
    )

}

export default ItemCard