from flask import render_template,redirect,request, session
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash, jsonify
from flask_app import app, bcrypt
from flask_app.models import user, book, friend, library, review, wishlist



@app.route('/dashboard')
def dashboard():

    # user.User.get_one({'id':session['user_id']})

    if 'user_id' not in session:
        return redirect('/')

    context = {
        'user' : user.User.get_one({'id':session['user_id']}),
        'all_libraries' : library.Library.get_all_library({'user_id' : session['user_id']})
    }
    
    return render_template('dashboard.html', **context)

@app.route('/all_books')
def all_books():

    if 'user_id' not in session:
        return redirect('/')

    context = {
        'user' : user.User.get_one({'id':session['user_id']}),
        'all_books_all' : book.Book.get_all()
    }
    
    return render_template('all_books.html', **context)


@app.route('/book/new')
def new_book():

    context = {
        'user' : user.User.get_one({'id':session['user_id']})
    }

    return render_template('add_book.html', **context)


# app.config["MYSQL_HOST"] = "localhost"
# app.config["MYSQL_USER"] = "root"
# app.config["MYSQL_PASSWORD"] = ""
# app.config["MYSQL_DB"] = "testingdb"
# app.config["MYSQL_CURSORCLASS"] = "DictCursor"

	
# @app.route("/search",methods=["POST","GET"])
# def search():
#     searchbox = request.form.get("text")
#     cursor = mysql.connection.cursor()
#     query = "SELECT * FROM books WHERE books LIKE '{}%' order by title".format(searchbox)
#     cursor.execute(query)
#     result = cursor.fetchall()
#     return jsonify(result)


@app.route('/create_book',methods=['POST'])
def create_book():
    print(request.form)

    # is_valid = book.Book.validate_book(request.form)
    
    # if not is_valid:
    #     return redirect('/book/new')

        
    data = {
        **request.form,
        'user_id' : session['user_id']

    }
    id = book.Book.save(data)
    print(id)
    return redirect(f'/show/{id}')


@app.route('/search_wishlist', methods=['POST'])
def search_wishlist():

    data = {

        'author' : request.form['search'],
        'title' : request.form['search'],
        'genre' : request.form['search']
    }

    books= book.Book.search_wishlist(data)
    return jsonify(books=books)

@app.route('/search_books', methods=['POST'])
def search_books():

    data = {

        'author' : request.form['search'],
        'title' : request.form['search'],
        'genre' : request.form['search']
    }

    books = book.Book.search_books(data)
    return jsonify(books=books)

@app.route('/search_library', methods=['POST'])
def search_library():

    data = {

        'author' : request.form['search'],
        'title' : request.form['search'],
        'genre' : request.form['search']
    }

    books = book.Book.search_library(data)
    print(books)
    return jsonify(books=books)





@app.route('/show/<int:id>')
def show_book(id):
    context = {
        'user' : user.User.get_one({'id':session['user_id']}),
        'book' : book.Book.get_one({'id':id}),
        
    }
    return render_template("show.html", **context)


@app.route('/book/<int:id>/edit')
def edit_book(id):

   

    # if library.Library.user_id != session['user_id']:
    #     return redirect('/')

    

    context = {
        'user' : user.User.get_one({'id':session['user_id']}),
        'book': book.Book.get_one({'id':id})
    }

    # Recipe.get_one({'id':id})
    return render_template("edit_book.html", **context)



@app.route('/update_book', methods=['POST'])
def update_book():


    # is_valid = book.Book.validate_book(request.form)

    # if not is_valid:
    #     return redirect(f'/book/{id}/edit')

    data = {

        **request.form,
        'user_id' : session['user_id'],
        'id' : request.form['book_id']


    }
    
    book.Book.update(data)
    return redirect('/dashboard')


@app.route('/delete_book', methods=["POST"])
def delete_book():

    # book.Book.get_one({'id':id})

    # if book.user_id != session['user_id']:
    #     return redirect('/')

    data = {
        **request.form,
        'user_id' : session['user_id'],
        'id' : request.form['book_id']
    }

    book.Book.delete(data)
    return redirect('/all_books')