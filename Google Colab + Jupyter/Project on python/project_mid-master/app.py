from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('tables.html')


@app.route('/charts')
def render_charts():
    return render_template('charts.html')


@app.route('/tables')
def render_tables():
    return render_template('tables.html')


if __name__ == '__main__':
    app.run(debug=True)