"""
Inventory tracker to keep a list of what is in stock
Shipping functionality will track where its going and then remove from the main list

Author: zjanssen23@gmail.com
"""
import pandas as pd

#Enter path that you want the files saved for 'inventory_file' & 'shipping_file'
inventory_file = r"C:\Users\Zach\Documents\Asset Tracker\inventory_tracker.txt"
shipping_file = r"C:\Users\Zach\Documents\Asset Tracker\shipment_tracker.txt"

data = pd.read_csv(inventory_file)
df = pd.DataFrame(data, columns= ['asset', 'ritm', 'shipped', 'in/out', 'date'])

def search_asset_remove(asset_to_remove): #searches for asset given in shipping function then deletes it from inventory_file
    df = pd.DataFrame(data, columns= ['asset', 'ritm', 'shipped', 'in/out', 'date'])
    df = df[df["asset"].str.contains(asset_to_remove)==True]
    df.to_csv(inventory_file, index=False)    

def remove_asset(): #removes asset from inventory_file
    asset_to_remove = input("Asset checking out: ")
    df = pd.DataFrame(data, columns= ['asset', 'ritm', 'shipped', 'in/out', 'date'])
    df = df[df["asset"].str.contains(asset_to_remove)==True]
    df.to_csv(inventory_file, index=False) 

def show_inventory(): #shows what is currently in stock
    data = pd.read_csv(inventory_file)
    df = pd.DataFrame(data, columns= ['asset', 'ritm', 'shipped', 'in/out', 'date'])
    print(df)

def shipping(): #places info in shipping_file and then calls 'search_asset_remove' to remove from inventory file
    shipping_asset = input("Asset:  ")
    shipping_ritm = input("RITM: ")
    shipping_to = input("Shipping Address: ")
    date = input("Date: ")
    tracking_information = input("Tracking: ")
    search_asset_remove(shipping_asset)
    
    shipping_data = [[shipping_asset, shipping_ritm, shipping_to, date, tracking_information]]
    df2 = pd.DataFrame(shipping_data, columns= ['Asset', 'RITM', 'Shipped To', 'Date', 'Tracking'])
    df2.to_csv(shipping_file, mode='a', header=None, index=False) 

def add_asset(): #adds asset to inventory_file
    asset = input("Asset: ") 
    ritm = input("RITM: ")
    shipped = input("Shipped?: ")
    check_in = input("Date check in/out: ")  
    in_out = input("IN or OUT?: ")

    inventroy_data = [[asset, ritm, shipped, check_in, in_out]]
    df2 = pd.DataFrame(inventroy_data, columns= ['Asset', 'RITM', 'Shipped', 'Date', 'In/Out'])
    df2.to_csv(inventory_file, mode='a', header=None, index=False) 
    df2.close_csv()

if __name__ in '__main__':
    while True:
        print(
        '''


   ____                 ______                           __  
   /  _/   ____  _   __ /_  __/   _____  ____ _  _____   / /__
   / /    / __ \| | / /  / /     / ___/ / __ `/ / ___/  / //_/
 _/ /    / / / /| |/ /  / /     / /    / /_/ / / /__   / ,<   
/___/   /_/ /_/ |___/  /_/     /_/     \__,_/  \___/  /_/|_|  
                                                              


        #####################################################  
        # Enter number according to option                  #
        # 1. Check In Asset                                 #
        # 2. Check Out Asset                                #
        # 3. Ship Asset                                     #
        # 4. Show Inventory                                 #
        # 5. Exit                                           #
        #####################################################
        '''
        )
        option = input(":> ")
        if option == '1':
            add_asset()
        elif option == '2':
            remove_asset()    
        elif option == '3':
            shipping()
        elif option == '4':
            show_inventory()
        elif option == '5':
            break
        else:
            print("Not an option, try again")
