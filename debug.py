from customer import Customer
from coffee import Coffee
from order import Order

c1 = Customer("Alice")
c2 = Customer("Bob")
cf1 = Coffee("Latte")
cf2 = Coffee("Espresso")

c1.create_order(cf1, 4.5)
c1.create_order(cf2, 5.0)
c2.create_order(cf1, 6.0)

print("All Orders:", Order.all_orders)
print("Coffees for Alice:", [c.name for c in c1.coffees()])
print("Customers who ordered Latte:", [c.name for c in cf1.customers()])
print("Average price of Latte:", cf1.average_price())
print("Most aficionado for Latte:", Customer.most_aficionado(cf1).name)
