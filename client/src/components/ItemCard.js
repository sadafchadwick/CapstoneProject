import React, {useContext} from 'react';
import '../styling/itemcard.css'
import { UserContext } from './UseContext';

function ItemCard({ item, handleUpdate }) {
    const { user, setUser } = useContext(UserContext);
    const addItem = (e) => {
        const data={'user_id': user.id, 'item_id': item.id, 'quantity': 1}
        fetch('/itemcrates', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(data)
        })
            .then(r => {
                if (r.ok) {
                    r.json()
                        .then(itemcrate => {
                            console.log(itemcrate)
                            window.confirm("Item added to your stockpile")
                            handleUpdate(itemcrate.item_id)
                        })
                }
                else {
                    r.json()
                        .then(data => {
                            console.error('Error adding item')
                            window.confirm("Item failed to add to your stockpile!")
                        })
                }
            })
    }
    // console.log(user)
    return (
        <div className="card">
            <h3>{item.name}</h3>
            <img src={item.image_url}></img>
            <h5>{item.category}</h5>
            <button onClick={addItem}>Add item to MyStockpile</button>
        </div>
    )
    }
export default ItemCard