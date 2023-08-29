import React from 'react';

function Inventory() {
    const [allItem, setAllItem] = useState([])

    const deleteItem = (deletedId) => {
        fetch('/inventories/${deletedId}',
            { method: 'DELETE' })
            .then(() => console.log("this is deleted"))
            .catch(error => console.error('Error:', error))
    }

    useEffect(() => {
        fetch('/items')
            .then(r => r.json())
            .then(allItem => {
                setAllItem(allItem)
            })
    }, [])

    const addItem = () => {
        console.log('i work')
    }


    const inventoryCards = allInventory.map((inventory) => (
        <InventoryCard
            key={inventory.id}
            inventory={inventory}
        />
    ))
    
    return (
        <div>
            {itemCards}
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


export default Inventory