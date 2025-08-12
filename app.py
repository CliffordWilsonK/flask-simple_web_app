# Import libraries
from flask import Flask, request, url_for, render_template, redirect
# Instantiate Flask functionality
app = Flask(__name__)
# Sample data
transactions = [
    {'id': 1, 'date': '2023-06-01', 'amount':100 },
    {'id': 2, 'date': '2023-06-02', 'amount':-200 },
    {'id': 3, 'date': '2023-06-03', 'amount':300 }
]
# Read operation
@app.route('/')
def get_transactions():
    return render_template("transactions.html", transactions=transactions)
# Create operation
@app.route('/add', methods=['GET', 'POST'])
def add_transaction():
    if request.method == "GET":
        return render_template('form.html')
    if request.method == "POST":
        new_transaction = {
            'id': len(transactions)+1,
            'date': request.form['date'],
            'amount': request.form['amount']
        }
        transactions.append(new_transaction)
        return redirect(url_for('get_transactions'))

# Update operation
@app.route('/edit/<int:transaction_id>', methods=["GET", "POST"])
def edit_transaction(transaction_id):
    if request.method == "GET":
        transaction = next((t for t in transactions if t['id'] == transaction_id), None)
        return render_template('edit.html', transaction=transaction)
    if request.method == "POST":
        for t in transactions:
            if t['id'] == transaction_id:
                t['date'] = request.form['date']
                t['amount'] = request.form['amount']
        return redirect(url_for('get_transactions'))
# Delete operation
@app.route('/delete/<int:transaction_id>')
def delete_transaction(transaction_id):
    global transactions
    transactions = [t for t in transactions if t['id'] != transaction_id]
    return redirect(url_for('get_transactions'))
# Run the Flask app

if __name__ == "__main__":
    app.run(debug=True)