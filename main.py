
def calculate_change(paid, due):
    if paid > due:
        return paid - due
    else:
        pass
        return 0


try:
    due = float(input("Enter parking ticket amount: ₹"))

    if due <= 0:
        print("Ticket amount must be positive.")
    else:
        paid = 0

        print("\nInsert coins: ₹5, ₹10, ₹20 or ₹25")
        print("Type 0 to finish.")

        while paid < due:
            try:
                coin = int(input("Insert coin: ₹"))

                if coin == 0:
                    print("Payment stopped.")
                    break

                if coin not in [5, 10, 20, 25]:
                    print("Invalid coin. Try again.")
                    continue

                paid += coin
                print("Total paid: ₹", paid)

            except ValueError:
                print("Invalid input. Enter a whole number.")
                continue

        if paid >= due:
            change = calculate_change(paid, due)
            print("\nPayment successful!")
            print(f"Ticket amount: ₹{due:.2f}")
            print(f"Amount paid: ₹{paid:.2f}")
            print(f"Change returned: ₹{change:.2f}")
        else:
            print(f"Payment incomplete. You paid ₹{paid:.2f}.")
            print(f"Amount remaining: ₹{due - paid:.2f}")

except ValueError:
    print("Invalid ticket amount.")

