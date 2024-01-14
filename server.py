from flask import Flask,render_template
import requests
app=Flask(__name__)

response=requests.get("https://api.npoint.io/f841091ebd32f50c96a0")
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



if __name__=='__main__':
    app.run(debug=True)