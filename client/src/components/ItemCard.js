import React from 'react';

function ItemCard({item}) {
    const deleteItem = (deletedId) => {
        fetch('/items/${deletedId}',
            {method: 'DELETE'})
        .then(() => console.log("this is deleted"))
        .catch(error => console.error('Error:', error))
    }

    const addItem = () => {
        console.log('i work')
    }

    return (
        <div>
            <h2>{item.name}</h2>
            <h3>{item.category.name}</h3>
            <h3>{item.amount}</h3>
            <button onClick={addItem}>Add item to MyStockpile</button>
            <button onClick={() => deleteItem(item.id)}>Delete item item</button>
        </div>
    )

}

export default ItemCard