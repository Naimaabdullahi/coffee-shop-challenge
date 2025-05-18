# Coffee Shop Challenge

A Python project modeling the relationships between customers, coffees, and orders in a coffee shop. This challenge demonstrates object-oriented programming, object relationships, validation, and data aggregation.

## Project Structure

coffee-shop-challenge/
├── coffee.py
├── customer.py
├── debug.py
├── order.py
├── Pipfile
└── README.md

markdown
Copy
Edit

## Models

### Customer
- **Attributes**: `name` (str, 1–15 characters)
- **Relationships**:
  - `.orders()` → List of `Order` instances by this customer
  - `.coffees()` → Unique list of `Coffee` instances ordered
- **Methods**:
  - `.create_order(coffee, price)` → Creates and links an `Order`
  - `@classmethod most_aficionado(coffee)` → Returns customer who spent the most on a coffee

### Coffee
- **Attributes**: `name` (str, ≥3 characters, immutable)
- **Relationships**:
  - `.orders()` → List of `Order` instances for this coffee
  - `.customers()` → Unique list of `Customer` instances
- **Methods**:
  - `.num_orders()` → Number of orders
  - `.average_price()` → Average price of all orders

### Order
- **Attributes**: `customer` (Customer), `coffee` (Coffee), `price` (float, 1.0–10.0)
- **Relationships**:
  - `.customer` → Linked `Customer`
  - `.coffee` → Linked `Coffee`

## Requirements Covered

- [x] Class initializers and validations
- [x] Getter/setter properties
- [x] Object relationships
- [x] Aggregate methods
- [x] Bonus method: `Customer.most_aficionado()`

## How to Run

```bash
# Clone the repo
git clone https://github.com/Naimaabdullahi/coffee-shop-challenge.git
cd coffee-shop-challenge

# Activate virtual environment
pipenv install
pipenv shell

# Run debug
python debug.py
Author
Developed by Naima Abdullahi