from fb_mysql import mydb,cursor

class user:
    def __init__(self,name,email,password):
        self.username=name
        self.email=email
        self.password=password

    def details(self):
        sql="insert into users(username,email,password) values(%s,%s,%s)"
        values=(self.username,self.email,self.password)
        cursor.execute(sql,values)
        mydb.commit()

    def user_id(self):
        username=self.username
        pws=self.password
        sql="select id from users where username=%s and password=%s"
        values=(username,pws)
        cursor.execute(sql,values)
        result=cursor.fetchone()[0]
        return result if result else "no such user found"

    @staticmethod
    def login():
        username=input("enter the username::")
        pws=input("enter the password::")
        sql="select id from users where username=%s and password=%s"
        values=(username,pws)
        cursor.execute(sql,values)
        result=cursor.fetchone()[0]
        return result if result else 0

class post:
    def __init__(self,userid,title,content):
        self.user_id=userid
        self.title=title
        self.content=content

    def post(self):
        try:
            sql="insert into posts(user_id,title,content,created_at) values (%s,%s,%s,current_date)"
            values=(self.user_id,self.title,self.content)
            cursor.execute(sql,values)
            mydb.commit()
        except Exception as e:
            print("cannot perform this action::",e)



class comment:
    def __init__(self,postid,userid):
        self.post_id=postid
        self.user_id=userid

    def cmt(self):
        try:
            comment_txt=input("enter the comment::")                                        
            sql="insert into comments (post_id,user_id,comment_text,created_at) values (%s,%s,%s,current_date)"
            values=(self.post_id,self.user_id,comment_txt)
            cursor.execute(sql,values)
            mydb.commit()
        except:
            print("cannot perform this action!!")

class like:
    def __init__(self,postid,userid):
        self.post_id=postid
        self.user_id=userid

    def like_add(self):
        check_sql = "SELECT id FROM likes WHERE post_id=%s AND user_id=%s"
        cursor.execute(check_sql, (self.post_id, self.user_id))
        row = cursor.fetchone()

        if row:
            print("❌ You already liked this post!")
            return
        
        try:
            sql="insert into likes(post_id,user_id,created_at) values (%s,%s,current_date)"
            values=(self.post_id,self.user_id)
            cursor.execute(sql,values)
            mydb.commit()

        except:
            print("cannot perform this action")

    @staticmethod
    def show_details(id):
        if id==None:
            print("login first!")
            return
        sql="select u.username,p.user_id,p.content,c.comment_text,IFNULL(l.like_count, 0) AS total_likes from posts as p inner join users as u on u.id=p.user_id left join comments as c on p.id=c.post_id LEFT JOIN (SELECT post_id, COUNT(*) AS like_count FROM likes GROUP BY post_id) AS l on p.id=l.post_id where u.id=%s"
        values=(id,)
        cursor.execute(sql,values)
        result=cursor.fetchall()
        for i in result:
            username,user_id,content,text,total_likes=i
            print(f"username={username},id={user_id},content={content},comments={text},like count={total_likes}")
        
print("\n===== SIMPLE BLOG SYSTEM =====")
print("1. Create Account")
print("7.already has account login:")
print("2. Create Post")
print("3. Comment on Post")
print("4. Like a Post")
print("5. View Post")
print("6. Exit")

id=None
while True:
    choice = input("Enter your choice (1-6): ")
    if choice == '1':
        name=input("enter the username")
        email=input("enter the email")
        pws=input("enter the password")
        o1=user(name,email,pws)
        o1.details()
        id=o1.user_id()

    elif choice=="7":
        id=user.login()
        if id==0:
            print("no such user found!!")

        
    elif choice == '2':
        uid=id
        title=input("enter the title")
        content=input("enter the content")
        o2=post(uid,title,content)
        o2.post()
    
    elif choice == '3':
        postid=int(input("enter the postid::"))
        uid=id
        o3=comment(postid,uid)
        o3.cmt()
        
    elif choice == '4':
        pid=input("enter the post id !!")
        uid=id
        o4=like(pid,uid)
        o4.like_add()
        
    elif choice == '5':
        uid=id
        like.show_details(id)

    else :
        print("exited sucessfully")
        break
