import React from 'react';

function InventoryCard({inventory}) {
    const deleteInventory = (deletedId) => {
        fetch('/inventories/${deletedId}',
            {method: 'DELETE'})
        .then(() => console.log("this is deleted"))
        .catch(error => console.error('Error:', error))
    }

    const addInventory = () => {
        console.log('i work')
    }

    return (
        <div>
            <h2>{inventory.name}</h2>
            <h3>{inventory.category.name}</h3>
            <h3>{inventory.amount}</h3>
            <button onClick={addInventory}>Add item to MyStockpile</button>
            <button onClick={() => deleteInventory(inventory.id)}>Delete inventory item</button>
        </div>
    )

}

export default InventoryCard