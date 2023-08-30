import React, {useContext} from 'react';
import { useState, useEffect } from 'react'
import { UserContext } from './UseContext';
import ItemCrateCard from './ItemCrateCard'

function ItemCrate() {
    const [allItemCrates, setAllItemCrates] = useState([])
    const { user, setUser } = useContext(UserContext);


    useEffect(() => {
        user && fetch(`/itemcrates/${user.id}`)
            .then(r => r.json())
            .then(allItemCrates => {
                setAllItemCrates(allItemCrates)
            })
    }, [user])

    const handleDelete=((deletedId)=>{
        const updatedCrates= allItemCrates.filter((crate)=>crate.id!==deletedId)
        setAllItemCrates(updatedCrates)
    })

    const itemCrateCards = allItemCrates.map((itemcrate) => (
        <ItemCrateCard
            key={itemcrate.id}
            item={itemcrate.item}
            deletedId={itemcrate.id}
            handleDelete={handleDelete}
        />
    ))

    return (
        <div>
            {itemCrateCards}
        </div>
    )
}


export default ItemCrate