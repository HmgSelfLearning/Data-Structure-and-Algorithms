# -*- coding: utf-8 -*-
"""
Created on Tue May 20 19:27:45 2025

@author: hadis
"""

user = {
    "name": "Kyle",
    "age": 54,
    "magic": True,
    "scream": lambda: print("aaaaaah!")
}

# Lookup O(1)
print(user["name"])

# Insert O(1)
user["spell"] = "abra kadabra"

# Display full dictionary
print(user)

user["scream"]()
print(user["scream"]())

