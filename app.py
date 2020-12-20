from flask import Flask, render_template

app = Flask(__name__)

posts = [

    {
        'author': 'victor Madaraka',
        'title': 'Ten ways to die',
        'content': 'Beers comes this macabre series that re-creates',
        'date': 'April 20 2020'
    },
    {
        'author': '254_effect',
        'title': 'Ten best programmming languages',
        'content': 'Beers comes this macabre series that re-creates true incidents',
        'date': 'April 22 2020'
    },
    {
        'author': 'Shennon Victor',
        'title': 'Python Golang',
        'content': 'Beers comes this macabre series that',
        'date': 'April 24 2020'
    }
]

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)

@app.route('/about')
def about():
    return render_template('about.html')  

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/skills')
def skills():
    return render_template('skills.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/education')
def education():
    return render_template('education.html')

                 

if __name__ == "__main__":
    app.run(debug=True)   