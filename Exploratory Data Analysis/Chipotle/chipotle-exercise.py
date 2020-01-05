import pandas as pd

file_location = 'chipotle-data.csv'

data = pd.read_csv(file_location)
print(data)

##############################
## Questions

# Question 1 - Which was the most ordered-item and how many times, it was ordered?
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)
print(data.head())

print(data['item_name'].value_counts())
# Answer - Chicken Bowl

# Question 2 - For the order that contains maximum quantity, print the details
highest_quantity = data['quantity'].max()
print(data[data['quantity']==highest_quantity])

# Question - What is the price of each item?
# Question - Print the details of the order with the highest price tag.
# Question - How many times, people ordered more than one Canned Soda?
# Question - How many times, people ordered a Chicken items.
# Question - What is the average bill of the orders that contains Chicken Bowl.
# Question - Calculate the menu items, in which people are least interested.
# Question - Taking into consideration that chicken items have 100 calories, soda contains 200 calories and so on.
#            the calories that the user will consume.
# Question - Describe the statistics regarding each order item.
# Question - Map all the Indian values regarding each dish.
# Question - Create a new dictionary, which categorize each item into different types and if the order, contains
#            any of the veg, non-veg item, label the order as veg or non-veg.
# Question - Group the orders by veg and non-veg category and tell me if our customers are more vegetarian or non-vegetarian.
# Question - Compute the probability if the a new user is going to come, is he a vegetarian or non-vegetarian.


# Question 3 - print the details of the order which has the highest price
data['item_price'] = data['item_price'].str.strip('$')
data['item_price'] = data['item_price'].astype('float64')
print("Maximum price is: ", data['item_price'].max())
maximum_price = data['item_price'].max()
print(data[data['item_price'] == maximum_price])

# Question 4 - What is the total and average revenue amount per order?
# formula for revenue is Quantity * Item_Price
data['revenue'] = data['quantity'] * data['item_price']
print("Total revenue : ", data['revenue'].sum())
print("Average revenue : ", data['revenue'].mean())


###############
## Data Visualization

## Graphically, represent all the different items that were ordered.
import matplotlib.pyplot as plt

item_values = data['item_name'].value_counts()
print(item_values)
items_dictionary = dict(item_values.head(8))

menu_items = list(items_dictionary.keys())
total_purchases = list(items_dictionary.values())

plt.bar(menu_items, total_purchases)
# plt.show()

## Question - What is the probability, that the person coming to the restaurant is going to order chicken?
## Answer -

from functools import reduce

condition = lambda x, y: x+y
total = reduce(condition, total_purchases)
chicken_bowl_count = data['item_name'].value_counts()
print("Total chicken bowls: ", chicken_bowl_count['Chicken Bowl'])

print("Probability that the customer, is going to order 'Chicken Bowl' is: ", (chicken_bowl_count['Chicken Bowl']/total))