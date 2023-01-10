from flask import Flask, render_template, url_for

app = Flask(__name__)

active_page = ''

@app.route('/')
def main():
   active_page = '/'
   return render_template('index.html')

@app.route('/about')
def about():
   active_page = 'about'
   return render_template('about.html')

@app.route('/blog')
def blog():
   active_page = 'blog'
   return render_template('blog.html')

@app.route('/contact')
def contact():
   active_page = 'contact'
   return render_template('contact.html')

@app.route('/menu')
def menu():
   active_page = 'menu'
   return render_template('menu.html')

@app.route('/order')
def order():
   active_page = 'order'
   return render_template('order.html')

@app.route('/login')
def login():
   active_page = 'login'
   return render_template('login.html')




if __name__ == '__main__':
   app.run(debug=True)