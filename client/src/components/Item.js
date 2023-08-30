import React, { useEffect, useState, useContext } from 'react';
import ItemCard from './ItemCard';
import { UserContext } from './UseContext';

function Item() {
    const [allItem, setAllItem] = useState([]);
    const { user, setUser } = useContext(UserContext);

    useEffect(() => {
        fetch('/items')
            .then(r => r.json())
            .then(allItemData => {
                setAllItem(allItemData);
            });
    }, []);

    const handleUpdate=((id)=>{
        const updatedItems= allItem.filter((item)=>item.id!==id)
        setAllItem(updatedItems)
    })

    const itemCards = allItem.map((item) => {
        if (user?.itemcrates?.find(i => i.item_id === item.id)){
        }
        else{
            return(
            <ItemCard
                key={item.id}
                item={item}
                handleUpdate={handleUpdate}
            />
            )
        }}
    );

    return (
        <div>
            {itemCards}
        </div>
    );
}

export default Item;
