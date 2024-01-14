from flask import Flask,render_template
import requests
app=Flask(__name__)

response=requests.get("https://api.npoint.io/935908f9dc4d4516b62b")
data=response.json()  

@app.route('/')
def home():
    return render_template("index.html",posts=data)

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")

@app.route('/<int:id>')
def show_post(id):
    required_post=None
    for post in data:
        if post["id"]==id:
            required_post=post
            break
    return render_template("post.html",post=required_post,id=id)


if __name__=='__main__':
    app.run(debug=True)