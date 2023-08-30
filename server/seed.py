from config import db, app
from models import User, Item, ItemCrate
from faker import Faker

fake = Faker()

def generate_image_url(image_types=['medical', 'weapon', 'beverages', 'food', 'clothing', 'cooking supplies', 'radio', 'tool', 'document'], width=200, height=200):
    image_id = fake.random_int(min=1, max=100)
    selected_type = fake.random_element(image_types)
    return f"https://picsum.photos/{width}/{height}?image={image_id}&type={selected_type}"

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
                item_name = f'{category.name.capitalize()} Item {i+1}'  # Use "name" instead of "category"
                image_url = generate_image_url(image_types=['medical', 'weapon', 'perishable', 'clothing', 'cooking supplies', 'radio', 'tool', 'document'])
                item = Item(name=item_name, category=category.name, image_url=image_url)  # Use "name" instead of "category"
                items.append(item)
        
        # Create item crates
        itemcrates = []
        for user in users:
            for item in items:
                itemcrate = ItemCrate(quantity=10, user=user, item=item)
                itemcrates.append(itemcrate)

        # Delete existing data before reseeding
        db.session.query(ItemCrate).delete()
        db.session.query(Item).delete()
        db.session.query(User).delete()
        
        # Add data to session and commit to the database
        db.session.add_all(users + categories + items + itemcrates)
        db.session.commit()

if __name__ == '__main__':
    seed_data()
    print('Database seeded successfully!')