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
