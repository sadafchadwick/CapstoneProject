import React from 'react';
import { useState, useEffect } from 'react'

function ItemCrate() {
    const [allItemCrates, setAllItemCrates] = useState([])

    const deleteItem = (deletedId) => {
        fetch('/itemcrates/${deletedId}',
            { method: 'DELETE' })
            .then(() => console.log("this is deleted"))
            .catch(error => console.error('Error:', error))
    }

    useEffect(() => {
        fetch('/itemcrates')
            .then(r => r.json())
            .then(allItemCrates => {
                setAllItemCrates(allItemCrates)
            })
    }, [])

    const addItemCrate = () => {
        console.log('i work')
    }


    const itemCrateCards = allItemCrates.map((itemcrate) => (
        <ItemCrate
            key={itemcrate.id}
            itemcrate={itemcrate}
        />
    ))

    return (
        <div>
            {itemCrateCards}
        </div>
    )
}

//     return (
//         <div>
//             <h1>Your Inventory</h1>
//             <div className="card">
//                 <h2>{inventory.name}</h2>
//                 <h3>{inventory.category.name}</h3>
//                 <h3>{inventory.amount}</h3>
//                 <button onClick={addItem}>Add item to MyStockpile</button>
//             </div>
//         </div>
//     )
// }


export default ItemCrate