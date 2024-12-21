#!/usr/bin/env python
# coding: utf-8

# # wap to simulate atm program , atm of a bank it should ask the user from a menue , press 1 to create pin and update balance , press 2 to change pin , press 3 to show balanced (provided correct pin is given) , press 4 to withdraw money , press 5 thank you for bank atm

# In[ ]:


class ATM:
    def __init__(self):
        self.pin = ''
        self.balance = 0
        self.menu()
    def menu(self):
        choice = input("""
        Welcome to ATM
        Press 1 : Create PIN 
        Press 2 : Change PIN
        Press 3 : Check Balance
        Press 4 : Withdraw
        Press 5 : Exit The System 
        You Press is : """)
        if choice == '1':
            self.createpin()
        elif choice == '2':
            self.changepin()
        elif choice == '3':
            self.checkbalance()
        elif choice == '4':
            self.withdraw()
        else:
            print("Thank You .... Visit Again!!!!!!!")
    def createpin(self):
        userpin = input("Enter the PIN : ")
        self.pin = userpin
        balance = int(input("Enter the Balance : "))
        self.balance = balance
        print("PIN Created")
        self.menu()
    def changepin(self):
        oldpin = input("Enter the PIN : ")
        if oldpin == self.pin:
            newpin = input("Enter the New PIN : ")
            self.pin = newpin
            print("PIN Changed")
        else:
            print("Enter Correct PIN")
        self.menu()
    def checkbalance(self):
        userpin = input("Enter the PIN : ")
        if userpin == self.pin:
            print("Your Account Balanced is :",self.balance)
        else:
            print("Enter the Correct PIN")
        self.menu()
    def withdraw(self):
        userpin = input("Enter the PIN : ")
        if userpin == self.pin:
            print("Your Account Balanced is :",self.balance)
            Withdrawamount = int(input("How many Amount are Withdraw : "))
            if Withdrawamount <= self.balance:
                self.balance -= Withdrawamount
                print("Your Amount is Successfully withdraw")
            else:
                print("Unifficient Balanced is your Account")
        else:
            print("Enter the PIN")
        self.menu()
atmforyourservice = ATM()


# 1.  make a constructor with a valid parameter  ,
# 2.  shift() returns the first element and removes it from the list. Also, use the custom(raise) exception in this method.
# 3.  unshift() "pushes" a new element to the front or head of the list
# 4.  push() adds a new element to the end of a list
# 5.  pop() returns the last element and removes it from the list
# 6.  remove() returns the maximum element of the list and removes it from the list.
# 7.  Create the object and call all methods of the SQ class.

# In[5]:


class EmptyListError(Exception):
    pass

class SQ:
    def __init__(self, initial_list=None):
        self.items = initial_list or []

    def shift(self):
        if not self.items:
            raise EmptyListError("Cannot shift from an empty list")
        return self.items.pop(0)

    def unshift(self, item):
        self.items.insert(0, item)

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.items:
            raise EmptyListError("Cannot pop from an empty list")
        return self.items.pop()

    def remove(self):
        if not self.items:
            raise EmptyListError("Cannot remove from an empty list")
        max_element = max(self.items)
        self.items.remove(max_element)
        return max_element

    def __str__(self):
        return str(self.items).replace("[0, ", "[")

# Example usage:
sq = SQ([1, 2, 3, 4, 5])

# Shift
try:
    print("Shifted:", sq.shift())
except EmptyListError as e:
    print(e)

# Unshift
sq.unshift(0)
print("After Unshift:", sq)

# Push
sq.push(6)
print("After Push:", sq)

# Pop
try:
    print("Popped:", sq.pop())
except EmptyListError as e:
    print(e)

# Remove
try:
    print("Removed Max Element:", sq.remove())
except EmptyListError as e:
    print(e)

# Display final state
print("Final State:", sq)


# # wap to create a dominoz app using two classes pizza and order the counstructre method should have pizza(size , toppping and cheses) , small pizza prize is 50 , mediam is 100 , large is 200 , topping costs 20 ruppes extra for onione and capsicum and 50 ruppes for mashrum and olives , extra chees 50 rupees extra the order class has name and coustmer id constructer create method prize in pizza and order in bill in order class and print the final bill

# In[ ]:


class InvalidToppingException(Exception):
    pass

class InvalidCheeseException(Exception):
    pass

class Pizza:
    def __init__(self, size, toppings, cheese):
        self.size = size
        self.toppings = toppings
        self.cheese = cheese
        self.validate_toppings()
        self.validate_cheese()

    def validate_toppings(self):
        valid_toppings = ['corn', 'tomato', 'onion', 'capsicum', 'mushroom', 'olives', 'broccoli']
        for topping in self.toppings:
            if topping not in valid_toppings:
                raise InvalidToppingException(f"Invalid topping: {topping}")

    def validate_cheese(self):
        valid_cheese = ['mozzarella', 'feta', 'cheddar']
        for cheese in self.cheese:
            if cheese not in valid_cheese:
                raise InvalidCheeseException(f"Invalid cheese: {cheese}")

    def price(self):
        size_price = {'small': 50, 'medium': 100, 'large': 200}
        topping_price = 20
        exotic_toppings_price = 50
        cheese_price = 50

        total_price = size_price[self.size]

        for topping in self.toppings:
            if topping in ['broccoli', 'olives', 'mushroom']:
                total_price += exotic_toppings_price
            else:
                total_price += topping_price

        total_price += len(self.cheese) * cheese_price
        return total_price


class Order:
    def __init__(self, name, customer_id):
        self.name = name
        self.customer_id = customer_id
        self.pizzas = []

    def order(self, pizza):
        self.pizzas.append(pizza)

    def bill(self):
        total_cost = 0
        print(f"Order details for customer {self.name} (ID: {self.customer_id}):")
        for index, pizza in enumerate(self.pizzas, start=1):
            print(f"\nPizza {index}:")
            print(f"Size: {pizza.size}")
            print(f"Toppings: {', '.join(pizza.toppings)}")
            print(f"Cheese: {', '.join(pizza.cheese)}")
            pizza_cost = pizza.price()
            print(f"Cost: {pizza_cost} rupees")
            total_cost += pizza_cost
        print(f"\nTotal Order Cost: {total_cost} rupees")


# Example usage:
try:
    pizza1 = Pizza('medium', ['corn', 'tomato'], ['mozzarella', 'feta'])
    pizza2 = Pizza('large', ['mushroom', 'olives'], ['cheddar'])
    pizza3 = Pizza('small', ['onion', 'capsicum', 'broccoli'], ['mozzarella'])

    order = Order("John Doe", 123)
    order.order(pizza1)
    order.order(pizza2)
    order.order(pizza3)

    order.bill()
except InvalidToppingException as ite:
    print(f"Error: {ite}")
except InvalidCheeseException as ice:
    print(f"Error: {ice}")


# In[ ]:


https://patelmanishv.github.io/python1/

