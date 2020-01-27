from flask import Flask, render_template, url_for
app = Flask(__name__)

posts = [
    {
        'title': 'Test 1',
        'content': 'test 1 content',
        'author': 'Jane',
        'date_posted': 'Yesterday'
    },
    {
        'title': 'Test 2',
        'content': 'test 2 content',
        'author': 'Eric',
        'date_posted': 'Today'
    },
    {
        'title': 'Test 3',
        'content': 'test 3 content',
        'author': 'Joe',
        'date_posted': 'Today'
    }
]

@app.route('/')
def hello_world():
    return render_template('home.html', posts=posts)

@app.route('/about')
def stuff():
    return render_template('about.html', title="about")

if __name__ == '__main__':
    app.run(debug=True, port=8080)