import time

# welcome the customer
welcome = "Welcome to Fulfu's Restaurant"
print(welcome)

# display the menu
menu = {
    "Burger": 30, 
    "Fries": 15,  
    "Chicken Wings": 25,     
}

print("Menu: ")
for item, price in menu.items():
    print(f"{item}: ${price}")

# ask what they want to eat
choice = str(input("What do you want to eat, sir? ")).strip().title()

# cook the item and check if the item is available
if choice not in menu:
    print("Sorry, the dish you ordered is not available.")
else:
    print("Your food is cooking, sir.")
    time.sleep(4)
    print("Here's your food.")
    time.sleep(4)

    # calculate the bill
    gst = 4
    total_bill = menu[choice] + gst
    print(f"Your total bill, including GST, is ${total_bill}.")

# ask for the feedback
feedback = input("How was your meal? We would appreciate your feedback: ")

# Save feedback to a file
with open("feedback.txt", "a") as file:
    file.write(feedback + "\n")
    file.write(str(total_bill))

print("Thank you for dining with us! Please come again.")
