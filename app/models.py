from datetime import datetime
from app import db

class Author(db.Model):
   id = db.Column(db.Integer, primary_key=True)
   lastname = db.Column(db.String(100), index=True, unique=True)
   firstname = db.Column(db.String(200), index=True, unique=True)
   book = db.relationship("Book", backref="author", lazy="dynamic")


   def __str__(self):
       return f"<Author {self.Author}>"


class Book(db.Model):
   id = db.Column(db.Integer, primary_key=True)
   title = db.Column(db.Text)
   author_id = db.Column(db.Integer, db.ForeignKey('author.id'))
   available = db.relationship("Available", backref="book", lazy="dynamic")

   
   def __str__(self):
       return f"<Book {self.id}{self.Book}>"


class Available(db.Model):
   id = db.Column(db.Integer, primary_key=True)
   title = db.Column(db.Text)
   borrow = db.Column(db.Text)
   date = db.Column(db.DateTime, index=True, default=datetime.utcnow)
   book_id = db.Column(db.Integer, db.ForeignKey('book.id'))


   def __str__(self):
       return f"<Available {self.id}{self.Available}>"