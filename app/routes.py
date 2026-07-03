from flask import Blueprint, render_template, request, redirect, url_for
from utils.email_generator import generate_emails

main = Blueprint('main', __name__)

@main.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        email_count = int(request.form.get('email_count', 100))
        emails = generate_emails(email_count)
        return redirect(url_for('main.email_result', emails=emails))

    return render_template('index.html')

@main.route('/email-result/<emails>')
def email_result(emails):
    return render_template('email_result.html', emails=emails)
