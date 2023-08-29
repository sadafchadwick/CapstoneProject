from config import db, app
from models import User, Category, Item

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
            Category(name=name) for name in category_names
        ]
        
        # Create items
        items = []
        for category in categories:
            for i in range(10):
                item_name = f'{category.name.capitalize()} Item {i+1}'
                item = Item(name=item_name, user=users[i % 5], category=category, amount=i*5)
                items.append(item)
        
        # Add data to session and commit to the database
        db.session.add_all(users + categories + items)
        db.session.commit()

if __name__ == '__main__':
    seed_data()
    print('Database seeded successfully!')
