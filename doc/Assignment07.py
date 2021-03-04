# ---------------------------------------------------------------------------- #
# Title: Assignment 07
# Description: Working with error handling and picking
# ChangeLog (Who,When,What):
# C. Halim,3.1.2021, Create script
#------------------------------------------------------------------------------#
# Pickling
import pickle
InventoryList= {"Lamp","Table","Chair"}
pickling_data = open("InventoryList.dat","wb")
pickle.dump(InventoryList, pickling_data)
pickling_data.close()

pickle_close = open("InventoryList.dat", 'rb')
Inventory = pickle.load(pickle_close)
for item in InventoryList:
      print("Inventory_List for", item)
# Error Handling
try:
        new_inventory_list = input("Enter an item for inventory: ")
        if new_inventory_list.isnumeric():
            raise Exception ('no numeric')
        else:
            raise ''
except Exception as e:
        print("Error: please enter alphabets only")