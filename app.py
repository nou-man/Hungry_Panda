from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/')
def main():
   return render_template('index.html')

@app.route('/about')
def about():
   return render_template('about.html')

@app.route('/blog')
def blog():
   return render_template('blog.html')

@app.route('/contact')
def contact():
   return render_template('contact.html')

@app.route('/menu')
def menu():
   return render_template('menu.html')

@app.route('/order')
def order():
   return render_template('order.html')

@app.route('/login')
def login():
   return render_template('login.html')








if __name__ == '__main__':
   app.run(debug=True)