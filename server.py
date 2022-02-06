from flask import Flask, render_template  # added render_template!
app = Flask(__name__)

# @app.route('/<int:count>/<string:color>')
# def hello_world(count, color):
#     # Instead of returning a string,
#     # we'll return the result of the render_template method, passing in the name of our HTML file
#     return render_template('index.html', color=color, count=count)

@app.route('/play')
def play():
    return render_template('index.html', colors='blue', count=3)

@app.route('/play/<int:count>')
def a(count):
    return render_template('index.html', colors='blue', count=count)


@app.route('/play/<int:count>/<string:color>')
def b(count, color):
    return render_template('index.html', colors=color, count=count)

if __name__=="__main__":
    app.run(debug=True)
