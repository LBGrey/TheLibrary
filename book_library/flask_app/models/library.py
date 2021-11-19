from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app import Bcrypt  
from flask_app.models import user, book, review, friend, wishlist
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')



class Library:
    def __init__( self , data ):
        self.id = data['id']
        self.author = data['author']
        self.title = data['title']
        self.genre = data['genre']
        self.read = data['read']
        self.book_id = data['book_id']
        self.user_id = data['user_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @property
    def creator(self):
        return user.User.get_one({'id': self.user_id})


    @classmethod
    def save(cls, data ):
        query = "INSERT INTO libraries ( book_id , user_id, created_at, updated_at) VALUES ( %(book_id)s , %(user_id)s, NOW() , NOW() );"
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
    def update(cls,data):
        query = "UPDATE libraries SET book_id=%(book_id)s, user_id=%(user_id)s, updated_at = NOW() WHERE id = %(id)s;"
        return connectToMySQL('book_library').query_db(query,data)

    @classmethod
    def get_one(cls,data):
        query = "SELECT * FROM libraries WHERE libraries.id = %(id)s;"
        results = connectToMySQL('book_library').query_db(query,data)

        if not results:
            return results

        data = {
            **results[0]
        }

        return cls(data)

    @classmethod
    def get_all_library(cls, data):
        query = "SELECT * FROM books JOIN libraries ON books.id  = libraries.book_id JOIN users ON libraries.user_id = users.id WHERE user_id = %(user_id)s ORDER BY author ASC;"
        results = connectToMySQL('book_library').query_db(query, data)

        if len(results):
            all_libraries = []
            for libraries in results:
                all_libraries.append( cls(libraries) )

            return all_libraries

    @classmethod
    def delete(cls,data):
        query = "DELETE FROM books WHERE id = %(id)s;"
        return connectToMySQL('book_library').query_db(query,data)


    @classmethod
    def delete_from_library(cls,data):
        query = "DELETE FROM libraries USING users LEFT JOIN libraries on users.id = libraries.user_id LEFT JOIN books ON libraries.book_id = books.id WHERE user_id = %(user_id)s AND book_id = %(id)s;"
        return connectToMySQL('book_library').query_db(query,data)


    # @staticmethod
    # def validate_library(library):
    #     is_valid = True # we assume this is true
    #     if len(library['title']) < 3:
    #         flash("Title must be at least 3 characters.", 'error_title')
    #         is_valid = False
    #     if len(library['author']) < 3:
    #         flash("Author must be at least 3 characters.", 'error_author')
    #         is_valid = False
    #     if len(library['description']) < 3:
    #         flash("Description must be at least 10 characters.", 'error_desc')
    #         is_valid = False
    #     if len(library['genre']) == 0:
    #         flash("Genre must be chosen", 'error_genre')
    #         is_valid = False
    #     if len(library['pages']) == 0:
    #         flash("Number of pages must be given", 'error_pages')
    #         is_valid = False

    #     return is_valid

