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