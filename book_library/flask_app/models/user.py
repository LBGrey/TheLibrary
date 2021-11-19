from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models import book, friend, library, review
from flask_app import Bcrypt        
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')



class User:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

        # self.recipes = []

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    @classmethod
    def data(cls, data):

        query = "SELECT * FROM users WHERE users.id = %(id)s;"

        results = connectToMySQL('book_library').query_db( query, data )
        user = cls(results[0])
        return user


    @classmethod
    def save(cls, data ):
        query = "INSERT INTO users ( first_name , last_name , email , password, created_at, updated_at ) VALUES ( %(first_name)s , %(last_name)s , %(email)s ,%(password)s, NOW() , NOW() );"
        # data is a dictionary that will be passed into the save method from server.py
        return connectToMySQL('book_library').query_db( query, data )
    
    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM users WHERE id=%(id)s;"
        results = connectToMySQL('book_library').query_db( query, data )
        if not results:
            return results
        return cls (results[0])  

    
    @classmethod
    def get_by_email(cls,data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        results = connectToMySQL('book_library').query_db(query,data)
        # Didn't find a matching user
        if not results:
            return results
        return cls(results[0])



    # @classmethod
    # def get_recipes_for_user(cls, data):
    #     query = "SELECT * FROM recipes LEFT JOIN users ON recipes.user_id = user_id WHERE user_id = %(id)s;"
    #     results = connectToMySQL('login_and_registration').query_db( query , data )
    #     user = cls( results[0] )

    #     recipes = []
        
    #     for row_from_db in results:
            
    #         recipe_data = {

    #             "id" : row_from_db["recipe.id"],
    #             "name": row_from_db["name"],
    #             "description": row_from_db["description"],
    #             "instructions": row_from_db["instructions"],
    #             "under_30_minutes" : row_from_db["under_30_minutes"],
    #             "created_at" : row_from_db["recipe.created_at"],
    #             "updated_at" : row_from_db["recipe.updated_at"],
    #             "user_id" : row_from_db["user_id"]
    #         }

    #         recipes.append(recipe.Recipe (recipe_data))
    #     user.recipes = recipes
    #     return user


    @staticmethod
    def validate_user(data):
        is_valid = True

        if len(data['first_name']) < 2:
            flash(u"First name must be at least 2 characters", "register")
            is_valid = False
        if len(data['last_name']) < 2:
            flash(u"Last name must be at least 2 characters", "register")
            is_valid = False
        if len(data['email']) == 0 :
            flash(u"Must enter valid email address", "register")
            is_valid = False
        if not EMAIL_REGEX.match(data['email']): 
            flash(u"Invalid email address", "register")
            is_valid = False
        if len(data['password']) < 8:
            flash(u"Password must be at least 8 characters.", "register")
            is_valid = False
        if len(data['confirm_password']) == ['password']:
            flash(u"Passwords do not match", "register")
            is_valid = False

        return is_valid

