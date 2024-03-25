from flask import Flask, url_for

app = Flask(__name__)
# instantiating a flask object


# make the function http callable using a decorator
# route is a method
@app.route('/')
@app.route('/home/')
def homepage():
    about_url = url_for('about_page')
    lisa_url = url_for('lisa')
    bart_url = url_for('bart')
    homer_url = url_for('homer')
    marge_url = url_for('marge')
    maggie_url = url_for('maggie')
    return f"""
        <!DOCTYPE html>
        <html>
            <head>
                <title>Home</title>
                <style>
                    body {{
                        text-align: center;
                    }}
                    ul {{
                        list-style-type: none;
                        padding: 0;
                    }}
                    li {{
                        display: inline;
                        margin-right: 20px;
                    }}
                </style>
            </head>
            <body>
                <h1>Welcome to the Springfield Archive</h1>
                <p>Check out our list of residents in Springfield</p>
                <ul>
                    <li><a href="{lisa_url}">Lisa Simpson</a></li>
                    <li><a href="{bart_url}">Bart Simpson</a></li>
                    <li><a href="{homer_url}">Homer Simpson</a></li>
                    <li><a href="{marge_url}">Marge Simpson</a></li>
                    <li><a href="{maggie_url}">Maggie Simpson</a></li>
                </ul>
                <hr>
                <a href="{about_url}">About Page</a>
            </body>
        </html>
        """


# simple html page
@app.route('/about/')
def about_page():
    home_url = url_for('homepage')
    return f"""
    <!DOCTYPE html>
    <html>
        <head>
            <title>About Page</title>
            <style>
                body {{
                    text-align: center;
                }}
                .content-container {{
                    width: 80%;
                    margin: 0 auto;
                    text-align: left;
                }}
            </style>
        </head>
        <body>
            <h1>About our Archive</h1>
            <p>This archive was made in 2024. Lorem ipsum dolor sit amet, consectetur adipiscing elit. 
            Proin tempor nunc eget libero interdum pretium sit amet vitae erat. Interdum et malesuada fames ac ante 
            ipsum primis in faucibus. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia 
            curae; Fusce scelerisque tellus a euismod efficitur. Pellentesque commodo augue non quam rhoncus, eget 
            efficitur dolor consequat. Etiam maximus leo rutrum eros feugiat ultricies. In porttitor, lorem nec 
            vulputate pulvinar, erat mi posuere lacus, ut rhoncus diam nibh nec erat. Mauris aliquet enim nunc, 
            sit amet scelerisque purus condimentum eu.
            </p>
            <hr>
            <a href="{home_url}">Home Page</a>
        </body>
    </html>
    """


@app.route('/lisa/')
def lisa():
    home_url = url_for('homepage')
    about_url = url_for('about_page')
    bart_url = url_for('bart')
    homer_url = url_for('homer')
    marge_url = url_for('marge')
    maggie_url = url_for('maggie')
    return f"""
    <!DOCTYPE html>
    <html>
        <head>
            <title>About Lisa</title>
            <style>
                body {{
                    text-align: center;
                }}
                .content-container {{
                    width: 80%;
                    margin: 0 auto;
                    text-align: left;
                }}
            </style>
        </head>
        <body>
            <h1>Lisa Marie Simpson</h1>
            <p>Intelligent, kind, and passionate about the planet and all living things, 
            Lisa Simpson is the second child of 
            <a href="{homer_url}">Homer</a> 
            and <a href="{marge_url}">Marge</a>
            born May 4th 1984 , the younger sister of 
            <a href="{bart_url}">Bart</a>, 
            and the older sister of <a href="{maggie_url}">Maggie</a>, at age 8.</p>
            <hr>
            <a href="{home_url}">Home Page</a>
            <a href="{about_url}">About the Archive</a>
        </body>
    </html>
    """


@app.route('/bart/')
def bart():
    home_url = url_for('homepage')
    about_url = url_for('about_page')
    lisa_url = url_for('lisa')
    homer_url = url_for('homer')
    marge_url = url_for('marge')
    maggie_url = url_for('maggie')
    return f"""
    <!DOCTYPE html>
    <html>
        <head>
            <title>About Bart</title>
            <style>
                body {{
                    text-align: center;
                }}
                .content-container {{
                    width: 80%;
                    margin: 0 auto;
                    text-align: left;
                }}
            </style>
        </head>
        <body>
            <h1>Bartholomew Jojo "Bart" Simpson</h1>
            <p>At ten years old, Bart is the eldest child and only son of 
            <a href="{homer_url}">Homer</a> 
            and <a href="{marge_url}">Marge</a>, 
            and the brother of 
            <a href="{lisa_url}">Lisa</a> and 
            <a href="{maggie_url}">Maggie</a>. 
            Bart's most prominent and popular character traits are his mischievousness, rebelliousness and 
            disrespect for authority. </p>
            <hr>
            <a href="{home_url}">Home Page</a>
            <a href="{about_url}">About the Archive</a>
        </body>
    </html>
    """


@app.route('/homer/')
def homer():
    home_url = url_for('homepage')
    about_url = url_for('about_page')
    lisa_url = url_for('lisa')
    bart_url = url_for('bart')
    marge_url = url_for('marge')
    maggie_url = url_for('maggie')
    return f"""
    <!DOCTYPE html>
    <html>
        <head>
            <title>About Homer</title>
            <style>
                body {{
                    text-align: center;
                }}
                .content-container {{
                    width: 80%;
                    margin: 0 auto;
                    text-align: left;
                }}
            </style>
        </head>
        <body>
            <h1>Homer Jay Simpson</h1>
            <p>Homer is the nominal foreman of the paternally eponymous family. He and his wife 
            <a href="{marge_url}">Marge</a> have 
            three children: <a href="{bart_url}">Bart</a>, 
            <a href="{lisa_url}">Lisa</a> and <a href="{maggie_url}">Maggie</a>.</p>
            <hr>
            <a href="{home_url}">Home Page</a>
            <a href="{about_url}">About the Archive</a>
        </body>
    </html>
    """


@app.route('/marge/')
def marge():
    home_url = url_for('homepage')
    about_url = url_for('about_page')
    lisa_url = url_for('lisa')
    bart_url = url_for('bart')
    homer_url = url_for('homer')
    maggie_url = url_for('maggie')
    return f"""
    <!DOCTYPE html>
    <html>
        <head>
            <title>About Marge</title>
            <style>
                body {{
                    text-align: center;
                }}
                .content-container {{
                    width: 80%;
                    margin: 0 auto;
                    text-align: left;
                }}
            </style>
        </head>
        <body>
            <h1>Marjorie Jacqueline "Marge" Simpson</h1>
            <p>Marge is the matriarch of the Simpson family. With her husband 
            <a href="{homer_url}">Homer</a>, 
            she has three children: 
            <a href="{bart_url}">Bart</a>, 
            <a href="{lisa_url}">Lisa</a>, 
            and <a href="{maggie_url}">Maggie</a>.
            <hr>
            <a href="{home_url}">Home Page</a>
            <a href="{about_url}">About the Archive</a>
        </body>
    </html>
    """


@app.route('/maggie/')
def maggie():
    home_url = url_for('homepage')
    about_url = url_for('about_page')
    lisa_url = url_for('lisa')
    bart_url = url_for('bart')
    homer_url = url_for('homer')
    marge_url = url_for('marge')
    return f"""
    <!DOCTYPE html>
    <html>
        <head>
            <title>About Maggie</title>
            <style>
                body {{
                    text-align: center;
                }}
                .content-container {{
                    width: 80%;
                    margin: 0 auto;
                    text-align: left;
                }}
            </style>
        </head>
        <body>
            <h1>Margaret "Maggie" Simpson</h1>
            <p>Maggie is the youngest child of <a href="{homer_url}">Homer</a>
             and <a href="{marge_url}">Marge</a>, 
             and the younger sister to <a href="{bart_url}">Bart</a>
             and <a href="{lisa_url}">Lisa</a>. 
             She is often seen sucking on her orange pacifier and, when she walks, she trips over her clothing and falls on her face.
            <hr>
            <a href="{home_url}">Home Page</a>
            <a href="{about_url}">About the Archive</a>
        </body>
    </html>
    """


# dictionary to join the paths and page names
pages = {
    'Home': '/',
    'About': '/about/',
    'Lisa Simpson': '/lisa/',
    'Bart Simpson': '/bart/',
    'Homer Simpson': '/homer/',
    'Marge Simpson': '/marge/',
    'Maggie Simpson': '/maggie/'
}


@app.route('/<path:invalid_page>')
def page_not_found(invalid_page):
    return f"""
    <h1>Oops! You seem to be lost!</h1>
    <style>
            body {{
                text-align: center;
            }}
            ul {{
                list-style-type: none;
                padding: 0;
            }}
            li {{
                display: inline;
                margin-right: 20px;
            }}
    </style>
    <p>The page "{invalid_page}" does not exist.</p>
    <h2>Did you mean:</h2>
    <ul>
        {"".join(f'<li><a href="{url}">{name}</a></li>' for name, url in pages.items())}
    </ul>
    """


if __name__ == "__main__":
    app.run(debug=True)
