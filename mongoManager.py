import pymongo as mongo
import bson


import dataclasses
from dotenv import load_dotenv, find_dotenv
from werkzeug.security import generate_password_hash, check_password_hash
import os
from datetime import datetime

load_dotenv(find_dotenv())
CONNECTION_URL = os.environ.get("CONNECTION_URL")





class MongoManager:
    def __init__(self, ):
        self.LIMIT=10

        
        print("sa", self.LIMIT)

        self.client = mongo.MongoClient(CONNECTION_URL)
        self.db = self.client['rippledb']
        self.users = self.db['Users']
        self.posts = self.db['Posts']
        self.following = self.db['Following']
        self.likes = self.db['Likes']
        self.comments= self.db['Comments']
    
    # Register a new user
    def add_user(self, username : str ,email : str , password : str, bio:str) :
        password = generate_password_hash(password)
        self.users.insert_one(
            {
                "_id": email, 
                "username": username,
                "password" : password,
                "bio" : bio,
                "joined On" : datetime.now()

            }
        )

    # check password of user 
    def check_password(self, email : str , password : str):
        user = self.users.find_one({"_id": email})
        if user:
            return check_password_hash(user["password"], password)
        return False
    
    # get user by email
    def get_user(self, email : str):
        user =  self.users.find_one({"_id": email}, {"_id": 0, "password": 0})
        user['email'] = user['_id']
        del user['_id']
        return user
    
    # Make  a post 
    def make_post(self, user_email: str, title:str, content:str):
        self.posts.insert_one({
            "user_email": user_email,
            "title": title,
            "content": content,
            "posted_on": datetime.now(),
        })


    # get all posts 
    def get_all_posts(self, offset:int = 0, limit:int = None) :
        
        
       
        return (
          list(self.posts.find().sort("createdOn",-1).limit(self.LIMIT).skip(offset))
        )
    
    # get posts of a list of users
    def get_posts_of_users(self, user_emails: list, offset:int = 0, ) :
        return (
            list(
                self.posts.find({"user_email" :  {
                    "$in" : user_emails
                }}).sort({"createdOn":-1}).limit(self.LIMIT).skip(offset)
            )
        )
    
    # delete a post
    def delete_post(self, post_id: str):
        self.posts.delete_one({"_id": bson.ObjectId(post_id)})
        

    
    # follow a user
    def follow_user(self, user_email: str, follower_email: str):
        count = self.following.count_documents({
              "user_email": user_email,
            "follower_email": follower_email,
        })
        if(count>1):
            return False
        self.following.insert_one({
            "user_email": user_email,
            "follower_email": follower_email,
            })
        
    #unfollow a user
    def unfollow_user(self, user_email: str, follower_email: str):
        self.following.delete_one({"user_email": user_email, "follower_email": follower_email})

    # like a post
    def like_post(self, post_id: str, user_email: str):
        self.linkes.insert_one({
            "post_id": post_id,
            "user_email": user_email
        })

    # unlike a post
    def unlike_post(self, post_id: str, user_email: str):
        self.linkes.delete_one({"post_id": post_id, "user_email": user_email})

    # Check if a user has liked this post
    def has_liked(self, post_id: str, user_email: str):
        count = self.linkes.count_documents({"post_id": post_id, "user_email": user_email})
        if(count==0): return False
        else: return True

    #check who liked a post
    def get_likers(self, post_id: str):
        return self.linkes.find({"post_id": post_id}).distinct("user_email")
    
    # get no of likes of a post
    def get_no_of_likes(self, post_id: str):
        return self.linkes.count_documents({"post_id": post_id})
    
    
    # make a comment
    def make_a_comment(self, parent_id, comment , parent_type):
       
        self.comments.insert_one({
            "parent_id": parent_id,
            "comment": comment,
            "parent_type": parent_type
            })
    
    # delete a comment
    def delete_a_comment(self, comment_id):
        self.comments.delete_one({"_id": comment_id})


    #def get comments of a post
    def get_comments(self, post_id):
        return self.comments.find({"parent_id": post_id}).sort("created_at", -1)
    
        
    
          
    

if __name__ == '__main__':
    manager = MongoManager()
    manager.follow_user(
        user_email="test@example.com",
        follower_email="user@example.com",
    )
