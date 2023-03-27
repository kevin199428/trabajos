# -*- coding: utf-8 -*-
"""
Created on Sun Mar 26 18:35:09 2023

@author: Kevin
"""

while True:
    new_item = input("Enter a new device (type 'exit' to quit): ")
    if new_item.lower() == "exit":
        print("All done!")
        break
    with open("devices.txt", mode="a") as file:
        file.write(new_item + "\n")