# Personal Receipt Tracker

A command-line Python tool for logging purchases and tracking spending by category. Each receipt is saved to a JSON file, so your spending history is still there the next time you run it.

## Features

- **Add a purchase**: log the store, item, price, and category
- **View purchases**: see every purchase, or only one category, in a lined-up table
- **Total spent**: get the total for one category or for everything
- **Input validation**: rejects prices that aren't positive numbers and categories that aren't on the list, and asks again instead of crashing
- Starts safely on a first run, even if `purchases.json` doesn't exist yet

Categories: food, transportation, entertainment, bills, and shopping.

## Requirements

- Python 3.6 or newer
- No external packages; it uses only Python's built-in `json` module

## Getting Started

1. Clone the repository:

   ```bash
   git clone https://github.com/MichaelTM0/receipt-tracker.git
   cd receipt-tracker
   ```

2. Run the program:

   ```bash
   python receiptlog.py
   ```

3. Choose option 1 to log your first purchase. The program creates `purchases.json` automatically.

## Usage

```
=======================================================
1. Add a purchase
2. View purchases
3. Calculate total spent
4. Exit
Please choose an option (1-4):
```

Example output for option 3, choosing `food`:

```
Store           Item            Price      Category
-------------------------------------------------------
Publix          Groceries       $54.30     Food
Chipotle        Burrito         $12.50     Food
-------------------------------------------------------
Total Food Spending: $66.80
```

## How Data Is Stored

`purchases.json` holds a list of purchases, where each purchase is a dictionary:

```json
[
    {
        "store": "publix",
        "item": "groceries",
        "price": 54.3,
        "category": "food"
    }
]
```

## Configuration

The categories are set in one constant at the top of `receiptlog.py`:

```python
CATEGORIES = ["food", "transportation", "entertainment", "bills", "shopping"]
```

Add or remove a category there and every menu and validation check updates automatically.

## How It Works

- `load_purchases()` and `save_purchases()` handle all reading and writing of the JSON file, and every feature reuses them.
- `ask_category()` asks for a category until the answer is valid. Its `allow_all` switch accepts "all" when viewing or totaling, but not when adding a purchase.
- `view_purchases()` and `total_spent()` decide which purchases to show, and `print_purchases()` handles how they look.

## Future Improvements

- Track the date of each purchase and filter by month
- Edit or delete a purchase
- Monthly budgets with a warning when a category goes over
- Export spending to CSV or a chart

## What I Learned

- Storing records as a list of dictionaries in JSON
- Validating user input with loops, and only looping the part that needs repeating
- Writing helper functions with default parameters (`allow_all=False`)
- Combining conditions with `and` / `or`
- Separating what data to show from how to display it

## Author

**Michael Murchie**

- GitHub: [@MichaelTM0](https://github.com/MichaelTM0)
- LinkedIn: [michael-murchie](https://www.linkedin.com/in/michael-murchie/)
