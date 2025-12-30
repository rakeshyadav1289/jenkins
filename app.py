from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

# Route that renders the initial HTML page
@app.route('/')
def index():
    return render_template('index.html')

# Route that handles the redirection
@app.route('/go-to-success')
def go_to_success():
    # Redirects to the success_page function
    return redirect(url_for('success_page'))

@app.route('/success')
def success_page():
    return render_template('success.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
