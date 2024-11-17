import datetime

print("Welcome to payment receipt generator")
print("Enter Admin password")

def welcome():
    print("Welcome to payment receipt generator")
    print("Enter the name of the person")
    global name 
    name = input()
    print("Enter the amount of money")
    global amount
    amount = input()
    global date
    date = datetime.datetime.now()
    print("Enter the payment method c for cash, d for card, o for online")
    global method
    method = input()
    if method == "c":
        print("Enter the cash given by the customer")
        global cash
        cash = input()
        print("Enter the change given to the customer")
        global change
        change = input()
    elif method == "d":
        print("Enter the card number")
        global card_number
        card_number = input()
        print("Enter the expiry date of the card")
        global expiry_date
        expiry_date = input()
        print("Enter the CVV number")
        global cvv
        cvv = input()
    elif method == "o":
        print("Enter the transaction ID")
        global transaction_id
        transaction_id = input()
        print("Enter the bank name")
        global bank_name
        bank_name = input()
    else:  
        print("Invalid payment method")

def print_receipt():
    print("\n\n\n\n\n\n\n")
    print("Name: ", name)
    print("Amount: ", amount)
    print("Date & Time: ", date)
    print("Payment method: ", method)
    if method == "c":
        print("Cash given: ", cash)
        print("Change given: ", change)
    elif method == "d":
        print("Card number: ", card_number)
        print("Expiry date: ", expiry_date)
        print("CVV: ", cvv)
    elif method == "o":
        print("Transaction ID: ", transaction_id)
        print("Bank name: ", bank_name)
    else:
        print("Invalid payment method")
        
def save_txt():
    with open("reciept.txt", "w") as f:
        f.write("Payment Receipt\n\n")
        f.write(f"Name: {name}\n")
        f.write(f"Amount: {amount}\n")
        f.write(f"Date & Time: {date}\n")
        f.write(f"Payment method: {method}\n")
        if method == "c":
            f.write(f"Cash given: {cash}\n")
            f.write(f"Change given: {change}\n")  
        elif method == "d":
            f.write(f"Card number: {card_number}\n")
            f.write(f"Expiry date: {expiry_date}\n")
            f.write(f"CVV: {cvv}\n")
        elif method == "o":
            f.write(f"Transaction ID: {transaction_id}\n")
            f.write(f"Bank name: {bank_name}\n")
        else:
            f.write("Invalid payment method")
        f.write("\n\nThank you for using our service")

def print_printer():
    import subprocess

    def print_file(file_path):
        subprocess.run(["lp", "-d", "your_printer_name", file_path])  # Replace "your_printer_name" with the actual printer name

    file_path = "reciept.txt"
    print_file(file_path)

admin_password = input()
password = "password"
if admin_password == password:
    while True:
        welcome()
        print_receipt()
        save_txt()
        print_printer()
        print("\n\n\n\nDo you want to generate another receipt? y for yes, n for no")
        choice = input()
        if choice == "n":
            break
        elif choice == "y":
            continue
        else:
            print("Invalid choice")



    print("Thank you for using our service")
else:
    print("Wrong password")
