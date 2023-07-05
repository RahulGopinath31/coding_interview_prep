'''
3. An e-commerce site tracks the purchases made each day. The product that is purchased the most one day 
is the featured product for the following day. If there is a tie for the product purchased most frequently, 
product names are ordered alphabetically ascending and the last name in the list is chosen.[Amazon]

['yellowShirt', 'redHat', 'blackShirt', 'bluePants', 'redHat','pinkHat', 'blackShirt', 'yellowShirt', 
'greenPants', 'greenPants', 'greenPants']

'yellowShirt' - 2
'redHat' - 2
'blackShirt' - 2
'bluePants' - 1
'greenPants' - 3
'pinkHat' - 1

Output - greenPants

'''

# featured product

def featured_product(items):
    ## create a dictionary with items and its corresponding occurance in the list
    item_num_dict = dict()
    max = 0

    for item in items: # T(n) = O(n)
        if item in item_num_dict:
            item_num_dict[item] += 1
        
        else:
            item_num_dict[item] = 1

        if item_num_dict[item] > max:
            max = item_num_dict[item]

        
    
    item_name = ''
    for key in item_num_dict.keys():
        if item_num_dict[key] == max and item_name < key:
            item_name = key


    return item_name






# diver function
items = ['yellowShirt', 'redHat', 'blackShirt', 'bluePants', 'redHat','pinkHat', 'blackShirt', 'yellowShirt', 
'greenPants', 'greenPants', 'greenPants']
print(featured_product(items))

# items2 = ['yellowShirt', 'redHat', 'blackShirt', 'bluePants', 'redHat','pinkHat', 'blackShirt', 'yellowShirt', 
# 'greenPants', 'greenPants']
# print(featured_product(items2))

# time complexity : O(n)
# space complexity : O(k), where k is the number of unique items.


