from flask import render_template,redirect,request, session
from flask_app import app, bcrypt
from flask_app.models import user
from flask import flash


@app.route('/')
def reg_login():

    if 'user_id' in session:
        return redirect('/dashboard')

    return render_template("index.html")

# @app.route('/dashboard')
# def dashboard_temp():
#     return render_template("dashboard.html")

# @app.route('/show')
# def dashboard_temp():
#     return render_template("show.html")

# @app.route('/edit')
# def dashboard_temp():
#     return render_template("edit.html")

# @app.route('/new')
# def dashboard_temp():
#     return render_template("new.html")


@app.route('/login', methods=['POST'])
def login():
    # see if the username provided exists in the database
    data = { 
        "email" : request.form["email"]
        }
    user_in_db = user.User.get_by_email(data)
    # user is not registered in the db
    if not user_in_db:
        flash(u"Invalid Email/Password", "login")
        return redirect("/")
    if not bcrypt.check_password_hash(user_in_db.password, request.form['password']):
        # if we get False after checking the password
        flash(u"Invalid Email/Password", "login")
        return redirect('/')
    # if the passwords matched, we set the user_id into session
    session['user_id'] = user_in_db.id
    
    # never render on a post!!!
    return redirect(f'/dashboard') 

@app.route('/create_user', methods=["POST"])  
def create_user():
    # First we make a data dictionary from our request.form coming from our template.
    # The keys in data need to line up exactly with the variables in our query string.
    if not user.User.validate_user(request.form):
        return redirect('/')

    password = bcrypt.generate_password_hash(request.form['password'])
    print(password)
    
    data = {

        "first_name": request.form["first_name"],
        "last_name" : request.form["last_name"],
        "email" : request.form["email"],
        "password" : password

    }
    # We pass the data dictionary into the save method from the Friend class.
    user.User.save(data)
    # Don't forget to redirect after saving to the database.
    return redirect('/dashboard')


@app.route('/logout')
def logout():

    session.clear()
    
    return redirect('/')