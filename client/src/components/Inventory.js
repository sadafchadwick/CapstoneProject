import React, {useEffect, useState} from 'react'
import InventoryCard from './InventoryCard';

function Inventory(){
    const [allInventory, setAllInventory] = useState([])

    useEffect(() => {
        fetch ('/inventories')
        .then(r =>r.json())
        .then(allInventory => {
            setAllInventory(allInventory)
        })
    }, [])

    const inventoryCards =  allInventory.map((inventory) => (
        <InventoryCard
            key={inventory.id}
            inventory = {inventory}
        />
    ))

    return (
        <div>
            {inventoryCards }
        </div>
    )

}

export default Inventory