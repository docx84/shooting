from flask import Flask, redirect

app = Flask(__name__, static_url_path='', static_folder="vue/dist")


@app.route('/')
def hello_world():
    return redirect("/index.html", code=302)


if __name__ == '__main__':
    app.run(debug=True)
