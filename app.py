from flask import Flask, render_template

app = Flask(__name__)

# Home page
@app.route('/')
def home():
    return render_template('home.html')

# Subjects page
@app.route('/subjects')
def subjects():
    return render_template('subjects.html')

# Videos page
@app.route('/videos')
def videos():
    return render_template('videos.html')

# Previous Year Papers page
@app.route('/papers')
def papers():
    return render_template('papers.html')

# Programming tutorials page
@app.route('/programming')
def programming():
    return render_template('programming.html')

if __name__ == '__main__':
    app.run(debug=True) 