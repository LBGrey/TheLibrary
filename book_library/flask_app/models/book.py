from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app import Bcrypt  
from flask_app.models import user, library, review, friend, wishlist
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')



class Book:
    def __init__( self , data ):
        self.id = data['id']
        self.title = data['title']
        self.author = data['author']
        self.description = data['description']
        self.genre = data['genre']
        self.pages = data['pages']
        self.read = data['read']
        self.rating = data['rating']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'
    
    @property
    def creator(self):
        return user.User.get_one({'id': self.user_id})


    @classmethod
    def save(cls, data ):
        query = "INSERT INTO books ( title , author , genre, created_at, updated_at) VALUES ( %(title)s , %(author)s , %(genre)s, NOW() , NOW() );"
        # data is a dictionary that will be passed into the save method from server.py
        return connectToMySQL('book_library').query_db( query, data )

    # @classmethod
    # def get_one(cls):
    #     query = "SELECT * FROM recipes WHERE id = %(id)s;"
    #     results = connectToMySQL('login_and_registration').query_db(query)
    #     recipes = []
    #     for recipe in results:
    #         recipes.append ( cls(recipe))
    #     return recipes

    # @classmethod
    # def get_all_by_user(cls, data):
    #     query = "SELECT * FROM recipes LEFT JOIN users ON recipes.user_id = user_id WHERE user_id = %(id)s;"
    #     results = connectToMySQL('login_and_registration').query_db( query , data )
    #     if not results:
    #         return results

    #     all_recipes = []
    #     for recipes in results:
    #         all_recipes.append( cls(recipes))
    #     return all_recipes

    @classmethod
    def search_wishlist(cls,data):
        query = "SELECT * FROM books JOIN wishlists ON books.id = wishlists.book_id WHERE author LIKE CONCAT ('%%', %(author)s, '%%') OR title LIKE CONCAT('%%', %(title)s, '%%') OR genre LIKE CONCAT ('%%', %(genre)s, '%%') ORDER BY author ASC;"
        results = connectToMySQL('book_library').query_db(query,data)

        if len(results):
            all_books_searchw = []
            for books in results:
                all_books_searchw.append( (books) )

            return all_books_searchw

    @classmethod
    def search_books(cls,data):
        query = "SELECT * FROM books WHERE author LIKE CONCAT ('%%', %(author)s, '%%') OR title LIKE CONCAT ('%%', %(title)s, '%%') OR genre LIKE CONCAT ('%%', %(genre)s, '%%') ORDER BY author ASC;"
        results = connectToMySQL('book_library').query_db(query,data)

        if len(results):
            all_books_search = []
            for books in results:
                all_books_search.append( (books) )

            return all_books_search

    @classmethod
    def search_library(cls,data):
        query = "SELECT * FROM books JOIN libraries ON books.id = libraries.book_id WHERE author LIKE CONCAT ('%%', %(author)s, '%%') OR title LIKE CONCAT('%%', %(title)s, '%%') OR genre LIKE CONCAT ('%%', %(genre)s, '%%') ORDER BY author ASC;"
        results = connectToMySQL('book_library').query_db(query,data)

        if len(results):
            all_books_searchl = []
            for books in results:
                all_books_searchl.append( (books) )

            return all_books_searchl


    @classmethod
    def update(cls,data):
        query = "UPDATE books SET title=%(title)s, author=%(author)s, genre=%(genre)s, books.read=%(read)s, updated_at = NOW() WHERE id = %(id)s;"
        return connectToMySQL('book_library').query_db(query,data)

    @classmethod
    def get_one(cls,data):
        query = "SELECT * FROM books WHERE books.id = %(id)s;"
        results = connectToMySQL('book_library').query_db(query,data)

        if not results:
            return results

        data = {
            **results[0]
        }

        return cls(data)


    @classmethod
    def get_all(cls):
        query = "SELECT * FROM books ORDER BY author ASC;"
        results = connectToMySQL('book_library').query_db(query)

        if len(results):
            all_books = []
            for books in results:
                all_books.append( cls(books) )

            return all_books

    # @classmethod
    # def get_all_in_library(cls):
    #     query = "SELECT * FROM books LEFT JOIN libraries on libraries.user_id WHERE user_id = %(user_id)s"
    #     results = connectToMySQL('book_library').query_db(query)

    #     if len(results):
    #         all_books_library = []
    #         for books in results:
    #             all_books_library.append( cls(books) )

    #         return all_books_library



    @classmethod
    def delete(cls,data):
        query = "DELETE FROM books WHERE id = %(id)s;"
        return connectToMySQL('book_library').query_db(query,data)



    @staticmethod
    def validate_book(book):
        is_valid = True # we assume this is true
        if len(book['title']) < 2:
            flash("Title must be at least 2 characters.", 'error_title')
            is_valid = False
        if len(book['author']) < 3:
            flash("Author must be at least 3 characters.", 'error_author')
            is_valid = False
        # if len(book['description']) < 3:
        #     flash("Description must be at least 10 characters.", 'error_desc')
        #     is_valid = False
        # if len(book['genre']) < 3:
        #     flash("Genre must be at least 3 characters", 'error_genre')
        # if len(book['pages']) == 0:
        #     flash("Number of pages must be given", 'error_pages')
        #     is_valid = False
        # if len(book['rating']) == 0:
        #     flash("Rating must be given", 'error_pages')
        #     is_valid = False

        return is_valid

