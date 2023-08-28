from config import db, app
from models import User, Category, Inventory


def seed_data():
    with app.app_context():
    
        User.query.delete()
        Category.query.delete()
        Inventory.query.delete()
        
        users = [
            User(name=f'User{i}', username=f'user{i}', password_hash='hashed_password') for i in range(1, 6)
        ]
        
        # Create categories
        categories = [
            Category(name=name) for name in [
                'medical', 'weapon', 'ammunition', 'beverages', 'perishable food', 
                'non-perishable food', 'clothing', 'cooking supplies', 'radio', 'tool', 'document'
            ]
        ]
        
        # Create inventories
        inventories = []
        for category in categories:
            for i in range(10):
                inventory_name = f'{category.name.capitalize()} Item {i+1}'
                inventory = Inventory(name=inventory_name, user=users[i % 5], category=category, amount=i*5)
                inventories.append(inventory)
        
        # Add data to session and commit to the database
        db.session.add_all(users + categories + inventories)
        db.session.commit()

if __name__ == '__main__':
    seed_data()
    print ('Data seeded successfully')