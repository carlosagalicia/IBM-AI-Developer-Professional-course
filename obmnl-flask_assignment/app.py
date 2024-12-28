# Import libraries
from flask import Flask, request, url_for, redirect, render_template

# Instantiate Flask functionality
app = Flask(__name__)

# Sample data
transactions = [
    {'id': 1, 'date': '2023-06-01', 'amount': 100},
    {'id': 2, 'date': '2023-06-02', 'amount': -200},
    {'id': 3, 'date': '2023-06-03', 'amount': 300}
]


# Read operation
@app.route("/", methods=["GET"])
def get_transactions():
    return render_template("transactions.html", transactions=transactions)


# Create operation
@app.route("/add", methods=["GET", "POST"])
def add_transaction():
    if request.method == "POST":
        transaction = {
            'id': len(transactions) + 1,
            'date': request.form['date'],
            'amount': float(request.form['amount'])
        }
        transactions.append(transaction)
        return redirect(url_for("get_transactions"))
    return render_template("form.html")


# Update operation
@app.route("/edit/<int:transaction_id>", methods=["GET", "POST"])
def edit_transaction(transaction_id):
    if request.method == "POST":
        for transaction in transactions:
            if transaction['id'] == transaction_id:
                transaction['date'] = request.form['date']
                transaction['amount'] = float(request.form['amount'])
                break
        return redirect(url_for("get_transactions"))

    for transaction in transactions:
        if transaction['id'] == transaction_id:
            return render_template("edit.html", transaction=transaction)

    return {"message": "Transaction not found"}, 404


# Delete operation
@app.route("/delete/<int:transaction_id>")
def delete_transaction(transaction_id):
    for transaction in transactions:
        if transaction['id'] == transaction_id:
            transactions.remove(transaction)
            break
    return redirect(url_for("get_transactions"))


@app.route("/search", methods=["GET", "POST"])
def search_transactions():
    if request.method == "POST":
        minimum = float(request.form['min_amount'])
        maximum = float(request.form['max_amount'])
        filtered_transactions = []
        for transaction in transactions:
            if minimum <= transaction['amount'] <= maximum:
                filtered_transactions.append(transaction)
        return render_template("transactions.html", transactions=filtered_transactions)
    return render_template("search.html")


@app.route("/balance", methods=["GET"])
def total_balance():
    balance = 0
    for transaction in transactions:
        balance += transaction['amount']
    return render_template("transactions.html", transactions=transactions, balance=balance)


# Run the Flask app
if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)
