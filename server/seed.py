from config import db, app
from models import User, Item, ItemCrate
from faker import Faker

def seed_data():
    with app.app_context():
        # Create users
        users = [
            User(name=f'User{i}', username=f'user{i}', password_hash='hashed_password') for i in range(1, 6)
        ]
        
        # Create categories
        category_names = [
            'medical', 'weapon', 'ammunition', 'beverages', 'perishable food', 
            'non-perishable food', 'clothing', 'cooking supplies', 'radio', 'tool', 'document'
        ]
        
        categories = [
            Item(name=name, category=name) for name in category_names
        ]
        
        # Create items
        items = []
        for category in categories:
            for i in range(10):
                item_name = f'{category.category.capitalize()} Item {i+1}'
                item = Item(name=item_name, category=category.category)
                items.append(item)
        
        # Create itemcrate
        itemcrates = []
        for user in users:
            for item in items:
                itemcrate = ItemCrate(quantity=10, user=user, item=item)
                itemcrates.append(itemcrate)
        
        #Delete database before reseeding
        User.query.delete()
        Item.query.delete()
        ItemCrate.query.delete()
        
        # Add data to session and commit to the database
        db.session.add_all(users + categories + items + itemcrates)
        db.session.commit()

if __name__ == '__main__':
    fake = Faker()
    seed_data()
    print('Database seeded successfully!')
