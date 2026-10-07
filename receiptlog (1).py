import json

FILENAME = "purchases.json"
CATEGORIES = ["food", "transportation", "entertainment", "bills", "shopping"]


# read the json file into a python list of purchases
def load_purchases(filename):
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


# write the python list of purchases back to the json file
def save_purchases(purchases, filename):
    with open(filename, "w") as file:
        json.dump(purchases, file, indent=4)


# keep asking until the user picks a valid category (or "all" if allowed)
def ask_category(allow_all=False):
    options = ", ".join(CATEGORIES)
    if allow_all:
        options += ", or all"

    while True:
        category = input(f"Choose a category ({options}): ").lower().strip()
        if category in CATEGORIES or (allow_all and category == "all"):
            return category
        print("That's not one of the options, please try again!")


# print purchases as a lined-up table
def print_purchases(purchases):
    print(f"{'Store':<15} {'Item':<15} {'Price':<10} {'Category'}")
    print("-" * 55)
    for purchase in purchases:
        print(
            f"{purchase['store'].title():<15} "
            f"{purchase['item'].title():<15} "
            f"${purchase['price']:<9.2f} "
            f"{purchase['category'].title()}"
        )
    print("-" * 55)


def add_purchase(filename):
    purchases = load_purchases(filename)

    store = input("What store did you visit? ").lower().strip()
    item = input("What did you purchase? ").lower().strip()

    # only the price needs a loop, because only the price can be invalid here
    while True:
        try:
            price = float(input("How much did you spend? "))
            if price > 0:
                break
            print("Price must be more than 0! Please try again!")
        except ValueError:
            print("Price must be a number! Please try again!")

    category = ask_category()

    purchase = {
        "store": store,
        "item": item,
        "price": price,
        "category": category,
    }

    purchases.append(purchase)
    save_purchases(purchases, filename)
    print("Purchase has been successfully added!")


def view_purchases(filename):
    purchases = load_purchases(filename)
    if not purchases:
        print("No purchases to view at this time!")
        return

    category = ask_category(allow_all=True)

    if category == "all":
        to_show = purchases
    else:
        to_show = [purchase for purchase in purchases if purchase["category"] == category]

    if not to_show:
        print(f"No {category} purchases yet!")
        return

    print_purchases(to_show)


def total_spent(filename):
    purchases = load_purchases(filename)
    if not purchases:
        print("No purchases to total at this time!")
        return

    category = ask_category(allow_all=True)

    if category == "all":
        to_total = purchases
    else:
        to_total = [purchase for purchase in purchases if purchase["category"] == category]

    if not to_total:
        print(f"No {category} purchases yet!")
        return

    total = sum(purchase["price"] for purchase in to_total)

    print_purchases(to_total)
    print(f"Total {category.title()} Spending: ${total:.2f}")


def main(filename):
    print("\n" + "=" * 55)
    print("             PERSONAL RECEIPT TRACKER")
    print("=" * 55)

    while True:
        print("\n" + "=" * 55)
        print("1. Add a purchase")
        print("2. View purchases")
        print("3. Calculate total spent")
        print("4. Exit")

        choice = input("Please choose an option (1-4): ").strip()

        if choice == "1":
            add_purchase(filename)
        elif choice == "2":
            view_purchases(filename)
        elif choice == "3":
            total_spent(filename)
        elif choice == "4":
            print("Thanks for using the receipt tracker! Goodbye!")
            break
        else:
            print("Invalid option, please enter a number 1-4!")


if __name__ == "__main__":
    main(FILENAME)
