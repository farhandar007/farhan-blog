from flask import Flask, render_template, request
import requests
import smtplib

app = Flask(__name__)

# getting blog data from API
response = requests.get("https://api.npoint.io/093dd2803b85074c2347").json()
# print(response)


# home page
@app.route("/")
def home():
    return render_template("index.html", all_posts=response)

# about page
@app.route("/about")
def about():
    return render_template("about.html")

# contact page(combined contact-form)
@app.route("/contact", methods=["POST","GET"])
def contact():
    if request.method == "POST":
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        message = request.form['message']
        # send mail to website owner
        my_email = "pythoncode61xd@gmail.com"
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=my_email, password="viyxkqqbdzjlfwfm")
            connection.sendmail(from_addr=my_email, to_addrs="frhndar@gmail.com",
                                msg=f"Subject:New Message\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage:{message}")
        return render_template("contact.html", contact_message="Message Sent")
    else:
        return render_template("contact.html", contact_message="Contact Me")




# blog page
@app.route('/blog/<current_id>')
def get_blog(current_id):
    id = int(current_id) - 1
    current_blog = response[id]
    print(current_blog)
    return render_template("post.html", blog=current_blog)


if __name__ == "__main__":
    app.run(debug=True)



