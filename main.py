expenses = []

print("Welcome to Expense Tracker 💸")

while True:
    print("\n--------MENU--------")
    print("1.) Add Expense")
    print("2.) View All Expenses")
    print("3.) View Total Spending")
    print("4.) View Spending by Category")
    print("5.) Exit")
    print("----------------------")

    choice = input("Enter your choice(1-5): ")

    if choice == "1":
        date = input("Enter date (DD-MM-YYYY): ")
        category = input("Enter category (Food,Travel,etc): ")
        description = input("Enter short description: ")
        amount = float(input("Enter amount(₹): "))

        expense = {
            'date': date,
            'category': category,
            'description': description,
            'amount': amount
        }

        expenses.append(expense)
        print("\n✅ Expense added successfully!")

    elif choice == "2":
        if len(expenses) == 0:
            print("\n⚠️ No expenses recorded yet.")
        else:
            print("\n--- All Expenses ---")
            i = 1
            for e in expenses:
                print(f"{i}. {e['date']} | {e['category']} | {e['description']} | ₹{e['amount']}")
                i += 1
            print("---------------------")

    elif choice == "3":
        total = 0
        for e in expenses:
            total += e["amount"]
        print(f"\n💰 Total Spending = ₹{total}")

    elif choice == "4":
        if len(expenses) == 0:
            print("\n⚠️ No expenses recorded yet.")
        else:
            summary = {}
            for e in expenses:
                cat = e["category"]
                if cat in summary:
                    summary[cat] += e["amount"]
                else:
                    summary[cat] = e["amount"]

            print("\n📊 Spending by Category:")
            for cat, amt in summary.items():
                print(f"{cat}: ₹{amt}")

    elif choice == "5":
        print("\n👋 Thanks for using Expense Tracker! Bye!")
        break

    else:
        print("\n❌ Invalid choice. Please try again.")
