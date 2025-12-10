from librarysql import db,cursor
import datetime

class books:
    def details(self,bookid,title,author,totalcpy):
        self.book_id=bookid
        self.title=title
        self.auther=author
        self.total_cpy=totalcpy
        self.avai_cpy=totalcpy

    def getid(self,title):
        sql="select bookid from books where title=%s"
        value=(title,)
        cursor.execute(sql,value)
        result=cursor.fetchone()
        if result:
            return result[0]
        else:
            print("not found!")


   
    def add_books(self):
        sql="insert into books values (%s,%s,%s,%s,%s)"
        values=(self.book_id,self.title,self.auther,self.total_cpy,self.avai_cpy)
        cursor.execute(sql,values)
        db.commit()

    

class members:
    def details(self,mem_id,name,contact_info):
        self.mem_id=mem_id
        self.name=name
        self.contact_info=contact_info

    def get_id(self,name):
        sql="select member_id from members where name=%s"
        value=(name,)
        cursor.execute(sql,value)
        result=cursor.fetchone()
        if result:
            return result[0]
        else:
            print("not found!")

    def bookid(self,name):
        sql="select book_id from members where name=%s"
        value=name
        cursor.execute(sql,value)
        result=cursor.fetchone()
        if result:
            return result[0]
        else:
            print("not found!")

    def add_member(self):
        sql="insert into members values (%s,%s,%s)"
        values=(self.mem_id,self.name,self.contact_info)
        cursor.execute(sql,values)
        db.commit()



class trans:
    def details(self,bookid,member_id,borrow_date,return_date):
        self.book_id=bookid
        self.member_id=member_id
        self.borrow_date=borrow_date
        self.return_date=return_date

    def borrow(self,title):
        sql="update books set available_copies=available_copies-1 where title=%s"
        values=(title,)
        cursor.execute(sql,values)
        db.commit()

    def retn(self,id):
        sql="update transactions set return_date=current_date where member_id=%s"
        value=(id,)
        cursor.execute(sql,value)
        db.commit()


    def add_trans(self):
        sql = "INSERT INTO transactions (book_id, member_id, borrow_date, return_date) VALUES (%s, %s, %s, %s)"
        values=(self.book_id,self.member_id,self.borrow_date,self.return_date)
        cursor.execute(sql,values)
        db.commit()


    def join(self):
        sql="select m.name,b.title,t.borrow_date,t.return_date from transactions as t inner join members as m on t.member_id=m.member_id inner join books as b on t.book_id=b.bookid"
        cursor.execute(sql)
        result=cursor.fetchall()
        for row in result:
            member_name, book_title, borrow_date, return_date = row
            # Handle case if book is not yet returned
            return_str = return_date if return_date else "Not returned"
            print(f"{member_name} borrowed \"{book_title}\" on {borrow_date}, returned on {return_str}")

o1=books()
o2=members()
o3=trans()
print("1.addd book")
print("2.add members ")
print("3.borrow book")
print("4.return books ")
print("5.view data")

while True:
    val=int(input("choose the operation to perform:"))
    if val==1:
        id=int(input("enter the book id "))
        title=input("enter the title ")
        author=input("enter the author ")
        tc=int(input("enter the num of copy: "))
        o1.details(id,title,author,tc)
        o1.add_books()

    elif val==2:
        mid=int(input("enter the member id "))
        name=input("enter the name ")
        cinfo=int(input("enter the contact number  "))
        o2.details(mid,name,cinfo)
        o2.add_member()

    elif val==3:
        name=input("enter ur name: ")
        book=input("enter the title of the book u wanna borrow::")

        mid=o2.get_id(name)
        bdate=datetime.date.today()
        rdate=None
        bk_id=o1.getid(book)
        o3.details(bk_id,mid,bdate,rdate)
        o3.add_trans()
        o3.borrow(book)

    elif val==4:
        name=input("enter ur name: ")
        val=o2.get_id(name)
        o3.retn(val)

    elif val==5:
        o3.join()

    else:
        print("exited sucessfully")
        break



#     # chatgpts best code for this problem:
#     from librarysql import db, cursor
# import datetime


# # ----------------------- BOOK CLASS -----------------------

# class Book:
#     def __init__(self, book_id=None, title=None, author=None, total_copies=None, available_copies=None):
#         self.book_id = book_id
#         self.title = title
#         self.author = author
#         self.total_copies = total_copies
#         self.available_copies = available_copies

#     def add_book(self):
#         sql = """INSERT INTO books (bookid, title, author, total_copies, available_copies)
#                  VALUES (%s, %s, %s, %s, %s)"""
#         val = (self.book_id, self.title, self.author, self.total_copies, self.available_copies)
#         cursor.execute(sql, val)
#         db.commit()
#         print(f"Book '{self.title}' added successfully.")

#     @staticmethod
#     def get_id_by_title(title):
#         cursor.execute("SELECT bookid FROM books WHERE title=%s", (title,))
#         result = cursor.fetchone()
#         return result[0] if result else None

#     @staticmethod
#     def update_available(book_id, amount):
#         cursor.execute("UPDATE books SET available_copies = available_copies + %s WHERE bookid=%s",
#                        (amount, book_id))
#         db.commit()


# # ----------------------- MEMBER CLASS -----------------------

# class Member:
#     def __init__(self, member_id=None, name=None, contact=None):
#         self.member_id = member_id
#         self.name = name
#         self.contact = contact

#     def add_member(self):
#         sql = "INSERT INTO members (member_id, name, contact) VALUES (%s, %s, %s)"
#         cursor.execute(sql, (self.member_id, self.name, self.contact))
#         db.commit()
#         print(f"Member '{self.name}' added successfully.")

#     @staticmethod
#     def get_id_by_name(name):
#         cursor.execute("SELECT member_id FROM members WHERE name=%s", (name,))
#         result = cursor.fetchone()
#         return result[0] if result else None


# # ----------------------- TRANSACTION CLASS -----------------------

# class Transaction:
#     def __init__(self, book_id=None, member_id=None, borrow_date=None, return_date=None):
#         self.book_id = book_id
#         self.member_id = member_id
#         self.borrow_date = borrow_date
#         self.return_date = return_date

#     def borrow(self):
#         sql = """INSERT INTO transactions (book_id, member_id, borrow_date, return_date)
#                  VALUES (%s, %s, %s, %s)"""
#         cursor.execute(sql, (self.book_id, self.member_id, self.borrow_date, self.return_date))
#         db.commit()

#         # deduct 1 book
#         Book.update_available(self.book_id, -1)
#         print("Book borrowed successfully.")

#     def return_book(self):
#         sql = """UPDATE transactions 
#                  SET return_date = CURRENT_DATE
#                  WHERE book_id=%s AND member_id=%s AND return_date IS NULL"""
#         cursor.execute(sql, (self.book_id, self.member_id))
#         db.commit()

#         # add back 1 book
#         Book.update_available(self.book_id, +1)
#         print("Book returned successfully.")

#     @staticmethod
#     def view_join():
#         sql = """
#         SELECT m.name, b.title, t.borrow_date, t.return_date
#         FROM transactions t
#         INNER JOIN members m ON t.member_id = m.member_id
#         INNER JOIN books b ON t.book_id = b.bookid
#         """
#         cursor.execute(sql)
#         results = cursor.fetchall()

#         for member_name, book_title, borrow_date, return_date in results:
#             r = return_date if return_date else "Not returned"
#             print(f"{member_name} borrowed \"{book_title}\" on {borrow_date}, returned on {r}")


# # ----------------------- MAIN PROGRAM -----------------------

# while True:
#     print("\n--- Library Management ---")
#     print("1. Add Book")
#     print("2. Add Member")
#     print("3. Borrow Book")
#     print("4. Return Book")
#     print("5. View Transactions")
#     print("6. Exit")

#     ch = input("Enter choice: ")

#     # Add Book
#     if ch == "1":
#         bid = int(input("Book ID: "))
#         title = input("Book Title: ")
#         author = input("Author: ")
#         total = int(input("Total Copies: "))

#         obj = Book(bid, title, author, total, total)
#         obj.add_book()

#     # Add Member
#     elif ch == "2":
#         mid = int(input("Member ID: "))
#         name = input("Name: ")
#         contact = input("Contact: ")

#         obj = Member(mid, name, contact)
#         obj.add_member()

#     # Borrow Book
#     elif ch == "3":
#         name = input("Your Name: ")
#         title = input("Book Title: ")

#         member_id = Member.get_id_by_name(name)
#         book_id = Book.get_id_by_title(title)

#         if not member_id:
#             print("Member not found.")
#             continue
#         if not book_id:
#             print("Book not found.")
#             continue

#         # check availability
#         cursor.execute("SELECT available_copies FROM books WHERE bookid=%s", (book_id,))
#         available = cursor.fetchone()[0]

#         if available <= 0:
#             print("Book not available.")
#             continue

#         today = datetime.date.today()
#         obj = Transaction(book_id, member_id, today, None)
#         obj.borrow()

#     # Return Book
#     elif ch == "4":
#         name = input("Your Name: ")
#         title = input("Book Title to Return: ")

#         member_id = Member.get_id_by_name(name)
#         book_id = Book.get_id_by_title(title)

#         if not member_id or not book_id:
#             print("Invalid entry.")
#             continue

#         obj = Transaction(book_id, member_id)
#         obj.return_book()

#     # View All Transactions (JOIN)
#     elif ch == "5":
#         Transaction.view_join()

#     elif ch == "6":
#         print("Exiting…")
#         break

#     else:
#         print("Invalid choice.")
