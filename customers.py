# 1. 
# 2. 
#exercise1
customer={
    "name": "John Doe",
    "email": "johnd@example.com",
    "tier": "gold",
    "ytd_spend": 12400
}
print(customer["name"])
print(customer["email"])
print(customer["tier"])
print(customer["ytd_spend"])
print(customer)
#exercise2
customer["phone"]="555-1234"
print(customer)
customer["tier"]="platinum"
print(customer)
del customer["email"]
print(customer)
#exercise3
print(customer.get('email', 'no email on file.'))
try:
    print(customer['email'])
except KeyError:
    print('no email on file.')
#exercise4
print(customer.items())
for key, value in customer.items():
    print(f"{key}: {value}")
#the .items() method returns the raw data.
#the for loop used is much leaner and can be formatted as we like.
#exercise5
tier_discounts = {
    "bronze": 0,
    "silver": 0.05,
    "gold": 0.1,
    "platinum": 0.15}
purchase=200
discount = tier_discounts.get(customer["tier"], 0)
print(f"Discount for tier: {customer['tier']} : {discount*100:.0f}% - final price: ${purchase*(1-discount):.2f}")
#exercise6
dict1 = {
    "name": "John Doe",
    "tier": "gold",
    "discount": 0.1
}
dict2 = {
    "name": "Jane Smith",
    "tier": "silver",
    "discount": 0.05
}
dict3 = {
    "name": "Bob Johnson",
    "tier": "platinum",
    "discount": 0.15
}
customers = [dict1, dict2, dict3]
for customer in customers:
    rate = tier_discounts.get(customer["tier"], 0)
    discount_amount = (300 * rate)
    print(f"{customer['name']} - {customer['tier']} - ${discount_amount:.2f} discount on a $300 purchase.")
#exercise7
catalog = {"Widget A": {"price": 9.99, "stock": 150}, "Gadget C": {"price": 49.99, "stock": 8}}
for item, details in catalog.items():
    if details["stock"] < 20:
        print("LOW STOCK ALERT: " + item)
#exercise8
