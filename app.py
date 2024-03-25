from flask import Flask, url_for

# class must be instantiated as an object
app = Flask(__name__)


# bind a URL to python code using @ decorator
@app.route('/')
@app.route('/home/')
def home_page():
    about_url = url_for('about_page')
    return f"""
    <html>
    <head>
        <title>hw10 practice</title>
    </head>
    <body>
        <h1>Home Page</h1>
        <p>It's the home page!</p>
         <p>It's a boring here, so why don't you check out the <a href="{about_url}">About Page</a> instead?</p>
        <hr>
        <a href="{about_url}">About Page</a>
    </body>
    </html>        
    """


@app.route('/hello/<name>')
def hello(name):
    greet = f"How's it going {name}?"
    return greet


@app.route('/about/')
def about_page():
    home_url = url_for('home_page')
    return f"""
    <html>
    <head>
        <title> hw10 practice</title>
    </head>
    <body>
        <h1>About Page</h1>
        <p>What brings you to the about page?</p>
        <hr>
        <a href="{home_url}">Home Page</a>
    </body>
    </html>        
    """


if __name__ == "__main__":
    app.run(debug=True)

