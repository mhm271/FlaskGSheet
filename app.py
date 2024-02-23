from flask import Flask, render_template, request, redirect, url_for
from werkzeug.exceptions import Forbidden

app = Flask(__name__)

# Initial rolling message
rolling_message = "Welcome to our tuition center!"

# Middleware function to check if request originates from localhost
@app.before_request
def restrict_to_localhost():
    if request.remote_addr != '127.0.0.1':
        raise Forbidden("Access Forbidden. Requests must originate from localhost.")

@app.route('/')
def index():
    # Pass the rolling message to the template
    return render_template('dashboard.html', rolling_message=rolling_message)

@app.route('/update_message', methods=['POST'])
def update_message():
    global rolling_message
    # Update rolling message with data from POST request
    rolling_message = request.form.get('new_message')
    # Redirect to the homepage to trigger a page refresh
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
