# Sal's Shipping
# Sal runs the biggest shipping company in the tri-county area, Sal’s Shippers. Sal wants to make sure that every single one of his customers has the best, and most affordable experience shipping their packages.
# 
# In this project, you’ll build a program that will take the weight of a package and determine the cheapest way to ship that package using Sal’s Shippers.
# 
# Sal’s Shippers has several different options for a customer to ship their package:
# 
# Ground Shipping, which is a small flat charge plus a rate based on the weight of your package.
# Ground Shipping Premium, which is a much higher flat charge, but you aren’t charged for weight.
# Drone Shipping (new), which has no flat charge, but the rate based on weight is triple the rate of ground shipping.
# Here are the prices:
# 
# Ground Shipping
# 
# Weight of Package	Price per Pound	Flat Charge
# 2 lb or less	$1.50	$20.00
# Over 2 lb but less than or equal to 6 lb	$3.00	$20.00
# Over 6 lb but less than or equal to 10 lb	$4.00	$20.00
# Over 10 lb	$4.75	$20.00
# 
# Ground Shipping Premium
# 
# Flat charge: $125.00
# 
# Drone Shipping
# 
# Weight of Package	Price per Pound	Flat Charge
# 2 lb or less	$4.50	$0.00
# Over 2 lb but less than or equal to 6 lb	$9.00	$0.00
# Over 6 lb but less than or equal to 10 lb	$12.00	$0.00
# Over 10 lb	$14.25	$0.00
# 
# Write a shipping.py Python program that asks the user for the weight of their package and then tells them which method of shipping is cheapest and how much it will cost to ship their package using Sal’s Shippers.


### User input 
weight = input("What is the weight of your package ? : ")
ground_cost = 1

#This is to convert the string into an int or a float depending on the input

if '.' in weight:
    weight = float(weight)
else:
    weight = int(weight)

#Ground Shipping 

if weight <= 2:
    ground_cost = weight * 1.50 + 20
elif weight > 2 and weight <= 6:
    ground_cost = weight * 3.0 + 20
elif weight > 6 and weight <= 10:
    ground_cost = weight * 4.0 + 20
elif weight > 10:
    ground_cost = weight * 4.75 + 20

print("The cost of Ground shipping is : " + str(ground_cost))


#Ground shipping premium 
ground_cost_premium = 125

print("The cost of Ground premium shipping is : " + str(ground_cost_premium))

#Drone shipping  
drone_cost = 1

if weight <= 2:
    drone_cost = weight * 4.50
elif weight > 2 and weight <= 6:
    drone_cost = weight * 9
elif weight > 6 and weight <= 10:
    drone_cost = weight * 12
elif weight > 10:
    drone_cost = weight * 14.25

print("the cost for Drone shipping is : " + str(drone_cost) + "$")

#This part is to calculate which option is the cheapest for user and return the name of the option 
#We do this by assigning all the cost variables to a dictionary and assigning Strings as values 
#Then we pass use the get method on the dictionary which returns the value of a certain key and we select that key with the min 
#function which will compare the 3 values and return the smallest key (key are variables defined by loops above)

cost_dictionary = {ground_cost:"Ground Shipping Cost",ground_cost_premium:"Premium Ground Shipping Cost",drone_cost:"Drone Sjipping Cost"}

print("The lowest option for you is : " + str(cost_dictionary.get(min(cost_dictionary)())))

