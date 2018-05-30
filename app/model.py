from flask import jsonify

class Books:
    books = {1:{"Title":"Paths Of Glory", "Author":"Jeffrey Archer", "Genre":"Adventure", "Items":5},
             2:{"Title":"Not A Penny More Not A Penny Less","Author":"Jeffrey Archer", "Genre":"Crime", "Items":7 }}
    
    def get_all_books(self):
        return self.books

    def get_a_book(self, book_id):
        if book_id not in self.books:
            return "Invalid Key"
        return self.books[book_id]

    def post_a_book(self, title, authors, genre, items):
        new_id = len(self.books) + 1
        self.books[new_id] = {"Title":title, "Author":authors, "Genre":genre, "Items":items}
        return "Book successfully added"


class Users:
    users = {101:{"Name":"Kathungu Bros", "Types":"Admin", "Age":20},
             102:{"Name":"Orlando Kabaya", "Types":"Normal", "Age":25}} 

    def get_users(self):
        return self.users

    def get_a_user(self,user_id):
        if user_id not in self.users:
            return "Enter a valid user_id"    
        return self.users[user_id]
        
    def post_a_user(self, name, types, age):
        new_id = len(self.users) + 1
        self.users[new_id] = {"Name":name, "Types":types, "Age":age}
        return "User successfully registered"                  
    


        



