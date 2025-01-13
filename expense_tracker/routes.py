from flask import Blueprint, render_template, redirect, url_for, request, flash
from app import db
from models import Expense
from datetime import datetime

bp = Blueprint('routes', __name__)

@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/add', methods=['GET', 'POST'])
def add_expense():
    if request.method == 'POST':
        name = request.form['name']
        amount = float(request.form['amount'])
        category = request.form['category']
        date = datetime.strptime(request.form['date'], '%Y-%m-%d')
        notes = request.form.get('notes', '')

        expense = Expense(name=name, amount=amount, category=category, date=date, notes=notes)
        db.session.add(expense)
        db.session.commit()
        flash('Expense added successfully!')
        return redirect(url_for('routes.view_expenses'))
    return render_template('add_expense.html')

@bp.route('/expenses')
def view_expenses():
    expenses = Expense.query.all()
    return render_template('view_expenses.html', expenses=expenses)

@bp.route('/edit/<int:expense_id>', methods=['GET', 'POST'])
def edit_expense(expense_id):
    expense = Expense.query.get_or_404(expense_id)
    if request.method == 'POST':
        expense.name = request.form['name']
        expense.amount = float(request.form['amount'])
        expense.category = request.form['category']
        expense.date = datetime.strptime(request.form['date'], '%Y-%m-%d')
        expense.notes = request.form.get('notes', '')

        db.session.commit()
        flash('Expense updated successfully!')
        return redirect(url_for('routes.view_expenses'))
    return render_template('edit_expense.html', expense=expense)
