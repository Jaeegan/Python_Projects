# -*- coding: utf-8 -*-
"""
    A password authentication system that checks the identity of a user.

Author:
    Joshua Gan - 29.06.2023
"""

import getpass

database = {}


def new_user():
    """Creates a new user and stores it in a dictionary database."""

    new_user = input("Create username: ").upper()

    while new_user in database:
        print("User already exists. Please enter a new username.")
        new_user = input("Create username: ").upper()

    new_password = input("Create password: ")
    database[new_user] = new_password


def login():
    """Credentials for login. Verify that user exists and password is correct."""

    if len(database) < 1:
        raise ValueError(
            "No existing users in database. Create user with 'new_user()'."
        )

    username = input("Enter username: ").upper()
    password = getpass.getpass("Enter password: ")

    for user, passw in database.items():
        if username == user:
            attempts = 2
            while password != passw and attempts != -1:
                password = getpass.getpass("Enter password again: ")
                print(f"You have {attempts} remaining.")
                attempts -= 1
            if password == passw:
                print("Verified")
            else:
                print("Invalid password, please try again.")
        else:
            print("Incorrect username. Username dones not exist.")
