import React from 'react';
import '../styling/itemcard.css'

function ItemCrateCard({ deletedId, item, handleDelete }) {

    const deleteItemCrate = () => {
        fetch(`/itemcrates/${deletedId}`,
            { method: 'DELETE' })
            .then(() => console.log("This is deleted"))
            .catch(error => console.error('Error:', error))
            handleDelete(deletedId)
    }

    return (
        <div className="card">
            <h2>{item?.name}</h2>
            <img src={item?.image_url}></img>
            <h5>{item?.category}</h5>
            <h5>{item?.amount}</h5>
            <button onClick={deleteItemCrate}>Delete item from My Stockpile</button>
        </div>
    )

}

export default ItemCrateCard