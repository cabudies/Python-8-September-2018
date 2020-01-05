import pandas as pd

file_location = 'chipotle-data.csv'

data = pd.read_csv(file_location)

# print all the columns name
print(data.info())

# print first 5 rows in the table
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)
print(data.head())

##############################
## Questions

# Question 1 - Which was the most ordered-item and how many times, it was ordered?
# Answer - Chicken Bowl for 726 Times
# Code to get the answer -
# print(data['item_name'].value_counts().head(1))

# Question 2 - For the order that contains maximum quantity, print the details
# Answer - Order id 1443. Details of the order are like this -
#       order_id  quantity                     item_name choice_description item_price
# 3598      1443        15  Chips and Fresh Tomato Salsa                NaN    $44.25
# code to get the answer -
# order_with_max_quantity = data['quantity'].max()
# print(data[data['quantity']==order_with_max_quantity])

# Question 3 - What is the price of each item?
# Answer - Cannot be determined.

# Question 4 - Print the details of the order with the highest price tag.
# Answer - Highest price of any order is $ 44.25.
# Details of that order are -
#       order_id  quantity                     item_name choice_description  item_price
# 3598      1443        15  Chips and Fresh Tomato Salsa                NaN       44.25
# Code to get this result -
# def condition(x):
#     x = x.strip('$')
#     return float(x)
#
# data['item_price'] = data['item_price'].apply(condition)
# print(data['item_price'])
#
# highest_price_tag_order = data['item_price'].max()
# print(data[data['item_price']==highest_price_tag_order])

# Question 5 - How many times, people ordered more than one Canned Soda?
# Answer - 20
# Code to get this -
# print(data[(data['item_name']=='Canned Soda') & (data['quantity']>1)].shape[0])

# Question 6 - How many times, people ordered a Chicken items.
# Answer - There are 6 items that contains 'Chicken' in it.
# Code to get this -
# print(data['item_name'][data['item_name'].str.contains('Chicken')].unique().shape[0])

# Question 7 - What is the average bill of the orders that contains Chicken Bowl.
# Answer - 10.113953168044079
# Code to get this -
# def condition(x):
#     x = x.strip('$')
#     return float(x)
#
# data['item_price'] = data['item_price'].apply(condition)
#
# print(data['item_price'][data['item_name']=='Chicken Bowl'].mean())

# Question 8 - Calculate the menu items, in which people are least interested.
# Answer - People are least interested in - ['Salad', 'Crispy Tacos', 'Veggie Crispy Tacos', 'Carnitas Salad', 'Chips and Mild Fresh Tomato Salsa']
# Code to get this -
# print(data['item_name'].value_counts().tail().index.tolist())

# Question 9 -Taking into consideration that chicken items have 100 calories, soda contains 200 calories and so on.
# Calculate the calories that the user will consume.

# Question 10 - Describe the statistics regarding each order item.
# Answer -
# count             4622
# unique              50
# top       Chicken Bowl
# freq               726
# Code to get this -
# print(data['item_name'].describe())

# Question 11 - Map all the Indian values regarding each dish.
# Answer - all the values being converted into indian rupees.
# code to get this -
# # taking value of $ to 74
# def condition(x):
#     x = x.strip('$')
#     x = float(x)*74
#     return float(x)
#
# data['item_price'] = data['item_price'].apply(condition)
# print(data['item_price'])
#
# print(data['item_price'].head())

# Question 12 - Create a new dictionary, which categorize each item into different types and if the order, contains
# any of the veg, non-veg item, label the order as veg or non-veg.

# step 1 - print all the unique items in our dataset.
# item_names = data['item_name'].unique()
# print(list(item_names))

# step 2 - convert the list into python series
# menu_items = pd.Series(item_names)
# print(menu_items)

# step 3 - write the series back to python file
# menu_items.to_csv('items_names.csv')

# step 4 - open up the file in excel and make food as veg or non-veg.

# step 5 - open up the items_names.csv file and categorize veg and non-veg items separately
# items = pd.read_csv('items_names.csv')
# veg_items = items['item_name'][items['item_category']=='veg']
# non_veg_items = items['item_name'][items['item_category']=='non-veg']
# print(veg_items)
# print('print non veg items now..')
# print(non_veg_items)

# step 6 - add a new column item_category to the dataset but before adding it to our dataset, create a new list to define
# if the order made by the user was veg or non-veg.
# veg_items = list(veg_items)
#
# veg_dishes = data['item_name'][data['item_name'].isin(veg_items)]
# non_veg_dishes = data['item_name'][data['item_name'].isin(non_veg_items)]
#
# print("Total number of veg orders - ", len(veg_dishes))
# print("Total number of non-veg orders - ", len(non_veg_dishes))
#
# data['item_category'] = ['veg' if x in(veg_items) else 'non-veg' for x in data['item_name']]
# print(data['item_category'])

# Question 13 - Group the orders by veg and non-veg category and tell me if our customers are more vegetarian or non-vegetarian.
# Answer - Based on the frequency that we have, the next user is vegetarian.
# Code to get this result
# print(data['item_category'].value_counts())


# Question 14 - Compute the probability if the a new user is going to come, is he a vegetarian or non-vegetarian.
# Answer - It's 51% probability, that the next user is vegetarian.
# Code to get this result
# print(data['item_category'].value_counts())
