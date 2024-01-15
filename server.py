from flask import Flask,render_template,request
import requests
import smtplib
app=Flask(__name__)

response=requests.get("https://api.npoint.io/935908f9dc4d4516b62b")
data=response.json()  

@app.route('/')
def home():
    return render_template("index.html",posts=data)

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/contact', methods=["GET","POST"])
def contact():
    if request.method=="POST":
        dt=request.form
        name=dt["name"]
        email=dt["email"]
        phone=dt["phone"]
        message=dt["message"]
        my_email="maleanmarshal@gmail.com"
        password="tfpkbvtucowmyrin"
        
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(my_email,password)
            connection.sendmail(from_addr=my_email,to_addrs="marshalmaleane123@gmail.com",msg=f"Subject:Form Data.\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage: {message}")
        return render_template("contact.html",msg_sent=True)
    else:
        return render_template("contact.html",msg_sent=False)


    

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