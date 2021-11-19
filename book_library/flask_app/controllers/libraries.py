from flask import render_template,redirect,request, session
from flask_app import app, bcrypt
from flask_app.models import book, friend, library, review, user, wishlist
from flask import flash


@app.route('/add_library',methods=['POST'])
def add_library():

    data = {
        'user_id' : session['user_id'],
        'book_id' : request.form['book_id']
    }
    
    library.Library.save(data)

    return redirect('/dashboard')



@app.route('/delete_from_library', methods=["POST"])
def delete_from_library():

    # books = book.Book.get_one({'id':id})

    # if book.user_id != session['user_id']:
    #     return redirect('/')

    data = {
        **request.form,
        'user_id' : session['user_id'],
        'id' : request.form['book_id']
    }

    library.Library.delete_from_library(data)

    return redirect('/dashboard')



@app.route('/move_to_library',methods=['POST'])
def move_to_library():

    data = {
        'user_id' : session['user_id'],
        'book_id' : request.form['book_id']
    }
    
    library.Library.save(data)

    wishlist.Wishlist.delete(data)

    return redirect('/dashboard')



# @app.route('/delete_library', methods=["POST"])
# def delete_library(id):

#     book.Book.get_one({'id':id})

#     # if book.user_id != session['user_id']:
#     #     return redirect('/')

#     library.Library.delete({'id':id})

#     return redirect('/dashboard')