from flask import render_template,redirect,request, session
from flask_app import app, bcrypt
from flask_app.models import book, friend, library, review, user, wishlist
from flask import flash



@app.route('/wishlist')
def show_wishlist():
    if 'user_id' not in session:
        return redirect('/')

    context = {
        'user' : user.User.get_one({'id':session['user_id']}),
        'all_books_wishlist' : wishlist.Wishlist.get_all_wishlist({'user_id' : session['user_id']})
    }
    
    return render_template('wishlist.html', **context)



@app.route('/add_wishlist',methods=['POST'])
def add_wishlist():

    data = {
        'user_id' : session['user_id'],
        'book_id' : request.form['book_id']
    }
    
    wishlist.Wishlist.save(data)

    return redirect('/wishlist')

@app.route('/delete_from_wishlist', methods=["POST"])
def delete_from_wishlist():

    # book.Book.get_one({'id':id})

    # if book.user_id != session['user_id']:
    #     return redirect('/')

    data = {
        **request.form,
        'user_id' : session['user_id'],
        'id' : request.form['book_id']
    }

    wishlist.Wishlist.delete_from_wishlist(data)


    return redirect('/wishlist')