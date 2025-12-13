from movie_hall_sql import mydb,cursor

class movies:
    def __init__(self,name,time,genre):
        self.name=name
        self.duration=time
        self.genre=genre

    def mov_upload(self):
        sql="insert into movies(name,duration,genre) values(%s,%s,%s)"
        values=(self.name,self.duration,self.genre)
        cursor.execute(sql,values)
        mydb.commit()

    @staticmethod
    def mov_id(name):
        sql="select id from movies where name=%s"
        values=(name,)
        cursor.execute(sql,values)
        result=cursor.fetchone()
        if result is None:
            return None
        
        return result[0]   


    @staticmethod
    def show_movies():
        sql="select m.name from movies as m"
        cursor.execute(sql)
        result=cursor.fetchall()
        return result
        

class shows:
    def __init__(self,name,time):
        self.name=name
        self.showtime=time

    def show_upload(self):
        try:
            sql="insert into shows(name,show_time,movid) values(%s,%s,%s)"
            values=(self.name,self.showtime,movies.mov_id(self.name))
            cursor.execute(sql,values)
            mydb.commit()
            print("movie uploaded sucessfully!!")

        except Exception as e:
            print("cannot perform this action",e)

    @staticmethod
    def show_shows():
        sql="select sh.name,sh.show_time from shows as sh"
        cursor.execute(sql)
        result=cursor.fetchall()
        for i in result:
            name,time=i
            print(f"name:{name},Time: {time.strftime('%Y-%m-%d %H:%M:%S')}")
    
    @staticmethod
    def show_id(name,time):
        sql = "SELECT id FROM shows WHERE name=%s and show_time=%s"
        values = (name,time)
        cursor.execute(sql, values)

        result = cursor.fetchone()   # do NOT index here

        if result is None:
            return None
        
        return result[0]
    

class seats:
    def __init__(self,value):
        pass

    @staticmethod
    def seats_upload(id):
        for i in range(3):
            sql="insert into seats(status,showid) values (%s,%s)"
            values=(0,id)
            cursor.execute(sql,values)
            mydb.commit()

    @staticmethod
    def book_seat():
        id=input("enter the seat id ::")
        val=seats.check_status(id)
        if val==1:
            print("already booked !!")
            return
        else:
            sql="update seats set status=%s where id=%s"
            values=(1,id)
            cursor.execute(sql,values)
            mydb.commit()
            print("booked sucessfully!!")

    @staticmethod
    def check_status(id):
        sql="select status from seats where id=%s"
        values=(id,)
        cursor.execute(sql,values)
        result=cursor.fetchone()[0]
        return result

    
    @staticmethod    
    def show_seats(name):
        sql="select sh.name,sh.show_time,se.id,se.status from shows as sh left join seats as se on sh.id=se.showid where sh.name=%s"
        values=(name,)
        cursor.execute(sql,values)
        result=cursor.fetchall()
        for i in result:
            name,time,seatid,status=i
            print(f" seat id={seatid},show name:{name},status={status},show time:{time}")

print("\n====== Movie Ticket Booking System ====\n")
val=input("are you an employee-- yes or no::")
while True:    
    if val=="yes":
        print("1. Upload Movie")
        print("2. Upload Show")
        print("3.exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            name=input("enter the movie name::")
            duration=input("enter the duration time::")
            genre=input("enter the genre::")
            o1=movies(name,duration,genre)
            o1.mov_upload()
            
        elif choice == "2":
            name=input("enter the show name:")
            time=input("enter the showtime eg:YYYY-MM-DD HH:MM:SS \t::")
            o2=shows(name,time)
            o2.show_upload()  
            id=shows.show_id(name,time) 
            seats.seats_upload(id)  
        else:
            print("exited sucessfully!!")
            break
    elif val=="no":
        print("3. Show Movies")
        print("4. Show Shows for Movies")
        print("5. Show Seats for a Show")
        print("6. Book a Seat")
        print("7. Exit")
        choice = input("Enter your choice: ")       
        if choice == "3":
            print("\n")
            print(movies.show_movies())
            
        elif choice == "4":
            print(shows.show_shows())


        elif choice == "5":
            name=input("enter the movie name::") 
            seats.show_seats(name)
            
        elif choice == "6":
            seats.book_seat()
            
        elif choice == "7":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")
    else:
        print("invalid")
        break