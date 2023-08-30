import React, { useEffect, useState } from 'react'
import ItemCard from './ItemCard';

function Item() {
    const [allItem, setAllItem] = useState([])

    useEffect(() => {
        fetch('/items')
            .then(r => r.json())
            .then(allItem => {
                setAllItem(allItem)
            })
    }, [])

    const itemCards = allItem.map((item) => (
        <ItemCard
            key={item.id}
            item={item}
        />
    ))

    return (
        <div>
            {itemCards}
        </div>
    )
}

export default Item