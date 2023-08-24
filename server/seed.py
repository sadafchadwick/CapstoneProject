#!/usr/bin/env python3

# Standard library imports
from random import random, randint, choice as rc

# Remote library imports
from faker import Faker

# Local imports
from app import app
from models import db, User, Food, UserFood

fake = Faker()

food_list = ['apples','corn','hamburger', 'chicken', 'pears', 'beans', 'eggs', 'cookies', 'almonds', 'pecans','whiskey','water', 'dr.pepper']

def create_users():
    users = []
    for _ in range(10):
        u = User(
            name=fake.name(),
            username=fake.user_name(),
            password_hash='password123'
        )
        users.append(u)
    return users

def create_foods():
    foods = []
    for food in food_list:
        import random
        random_amount= random.uniform(1,30)
        f = Food(
            name=food,
            amount=round(random_amount, 2)
        )
        foods.append(f)
    return foods


def create_userfoods():
    userfoods = []
    for _ in range (20):
        uf= UserFood(
            user_id = randint(1,10),
            food_id = randint(1,20)
        )
        userfoods.append(uf)
    return userfoods


if __name__ == '__main__':
    fake = Faker()
    with app.app_context():
        print("Starting seed...")
        # Seed code goes here!

        User.query.delete()
        Food.query.delete()
        UserFood.query.delete()


        users = create_users()
        db.session.add_all(users)
        db.session.commit()

        foods = create_foods()
        db.session.add_all(foods)
        db.session.commit()

        userfoods = create_userfoods()
        db.session.add_all(userfoods)
        db.session.commit()



# FOR AMMAR????
# from app import app, db
# from models import User, Fighter, Match

# def create_users():
#     users = []
#     for _ in range(20):
#         u = User(
#             username=fake.user_name(),
#             password_hash='password123'
#         )
#         users.append(u)
#     return users

# def create_fighters():
#     fighters = []
#     for _ in fighters:
#         import random
#         random_amount= random.uniform(1,10)
#         f = Fighter(
#             name=fake.first_name(),
#             hp=round(random_amount),
#             ap=round(random_amount)
#         )
#         fighters.append(f)
#     return foods


# def create_matches():
#     matches = []
#     for _ in range (20):
#         m= Match(
#             win_loss = randint(0,1),
#             user1 = randint(0,1),
#             fighter1 = randint(0,10),
#             fighter2 = randint(0,10)
#         )
#         userfoods.append(uf)
#     return userfoods


# if __name__ == '__main__':
#     fake = Faker()
#     with app.app_context():
#         print("Starting seed...")
#         # Seed code goes here!

#         User.query.delete()
#         Fighter.query.delete()
#         Match.query.delete()


#         users = create_users()
#         db.session.add_all(users)
#         db.session.commit()

#         fighters = create_fighters()
#         db.session.add_all(fighters)
#         db.session.commit()

#         matches = create_matches()
#         db.session.add_all(matches)
#         db.session.commit()