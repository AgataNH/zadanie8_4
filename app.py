from flask import Flask

app = Flask(__name__)

from flask import render_template
from flask import request
from flask import redirect

@app.route("/mypage/me")
def me():
    return render_template("me.html")

@app.route('/mypage/contact', methods=['GET', 'POST'])
def message():
   if request.method == 'GET':
       print("We received GET")
       return render_template("contact.html")
   elif request.method == 'POST':
       print("We received POST")
       print(request.form)
       return redirect("/")