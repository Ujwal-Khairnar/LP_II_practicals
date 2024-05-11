import time

class PizzaBot:
    def __init__(self):
        self.name = "PizzaBot"
    
    def greet(self):
        print("Welcome to PizzaBot! How can I assist you today?")
    
    def take_order(self):
        print("Great! What size pizza would you like? (small, medium, large, extra-large)")
        size = input().lower()
        
        print("What toppings would you like? (pepperoni, mushrooms, onions, green peppers, sausage, extra cheese)")
        toppings = input().lower()
        
        print("Would you like to add any drinks or sides? (yes/no)")
        extras = input().lower()
        
        if extras == "yes":
            print("What would you like to add?")
            additional_items = input()
        else:
            additional_items = "None"
        
        print("Can I have your delivery address, please?")
        address = input()
        
        print("Finally, what's your phone number in case we need to reach you?")
        phone_number = input()
        
        print("Thank you! Your order has been placed.")
        print("Size: " + size)
        print("Toppings: " + toppings)
        print("Additional items: " + additional_items)
        print("Delivery address: " + address)
        print("Phone number: " + phone_number)
        print("Your total comes to $15.99. Your pizza will be delivered within 30 minutes.")
    
    def farewell(self):
        print("Enjoy your pizza, and have a great day!")

def main():
    bot = PizzaBot()
    bot.greet()
    time.sleep(1)
    bot.take_order()
    time.sleep(1)
    bot.farewell()

if __name__ == "__main__":
    main()
