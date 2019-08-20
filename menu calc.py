# -*- coding: utf-8 -*-
"""
Created on Fri Aug 16 21:18:45 2019

@author: Fearghusson
"""
#limits of this code - can't have more than 10 menu items. 

menu = {1:['chicken strips', 3.50], 2:['french fries', 2.50]}

def create_list(value):
    
    #create a blank list to store the data
    order_list = []
    
    #take the input_order and append the list with each 
    #value in the input_order then get the menu item that
    #matches the input_order
    for v in value:
        order_list.append(menu.get(int(v)))
        
    return order_list

def add_list(value):
    
    #create blank number
    value_price = 0
    
    #takes list value and adds each value together
    for v in value:
        value_price += v[1]
        
    return value_price

def full_order(list_value):
    
    return add_list(create_list(list_value))

current_menu = ''

for v in menu.values():
    #print('Item: ' + str(v[0] + ' $' + str(v[1])))
    current_menu += 'Item: ' + str(v[0]) + ' $' + str(v[1]) + '\n'

#printing the full menu
print('Menu Items & Prices' + '\n' + current_menu.center(1))
   
while True:
    #continuing loop to get the orders
    input_order = input('Order Numbers?\n')
    
    print(full_order(input_order)) 
    
    finish = input('finished?\n')
    
    if finish == 'yes':
        break
