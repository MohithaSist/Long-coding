from datetime import datetime
userdetail=[]
Sign_in=[]
movieList=[]

av_seat=[[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15]]
class UserProfile:
    def userprofile(self):
        self.userid=int(input("Enter userid : "))
        self.username=input("Enter username : ")
        self.password=input("Enter password : ")
        self.gender=input("Enter gender : ")
        self.ph_no=int(input("Enter ph_no : "))
        print()
        userdetail.append(self.userid)
        userdetail.append(self.username)
        userdetail.append(self.password)
        userdetail.append(self.gender)
        userdetail.append(self.ph_no)
    def signin(self):
        self.user_name=input("Enter username : ")
        self.pass_word=input("Enter password : ")
        Sign_in.append(self.user_name)
        Sign_in.append(self.pass_word)
        if ((self.username==self.user_name) and (self.password==self.pass_word)):
            print("Welcome",self.username+'!')
        else:
            print("Enter Valid Login Credentials")
            exit()

class MovieListenins:
    def __init__(self,movieid:int,moviename:str,genere:str,timelen:str,releasedate:str):
        self.movieid=movieid
        self.moviename=moviename
        #self.language=language
        self.genere=genere
        self.timelen=timelen
        self.releasedate=releasedate

class MovieList:
    def moviesdetail(self):
        print()
        lang=input("Enter your language : ")
        print()
        if lang=='tamil':
            tam_movie1=MovieListenins(1.1,'Doctor','suspence','2.30','19/7/2019')
            tam_movie2=MovieListenins(1.2,'Kanchana','horror','1.50.55','8/6/2004')
            tam_movie3=MovieListenins(1.3,'Remo','love','2.00','30/8/2016')

            movieList.append(tam_movie1)
            movieList.append(tam_movie2)
            movieList.append(tam_movie3)

        elif lang=='english':
            eng_movie1=MovieListenins(2.1,'John Wick','suspence','2.00','9/9/2005')
            eng_movie2=MovieListenins(2.2,'The Nun','horror','1.50','3/4/2010')
            eng_movie3=MovieListenins(2.3,'Titanic','love','2.15','21/6/2018')
            movieList.append(eng_movie1)
            movieList.append(eng_movie2)
            movieList.append(eng_movie3)

        elif lang=='telugu':
            tel_movie1=MovieListenins(3.1,'Manan','suspence','2.30','27/6/2005')
            tel_movie2=MovieListenins(3.2,'Magadheera','horror','1.40.60','6/9/2010')
            tel_movie3=MovieListenins(3.3,'Pokiri','love','2.15','7/9/2022')
            movieList.append(tel_movie1)
            movieList.append(tel_movie2)
            movieList.append(tel_movie3)

        elif lang=='hindhi':
            hin_movie1=MovieListenins(4.1,'Pathaan','suspence','2.30','27/6/2005')
            hin_movie2=MovieListenins(4.2,'KGF','thriller','1.40.60','6/9/2010')
            hin_movie3=MovieListenins(4.3,'Bahubali','historical','2.15','7/9/2022')
            movieList.append(hin_movie1)
            movieList.append(hin_movie2)
            movieList.append(hin_movie3)

        for i in movieList:
            print(i.movieid)
            print(i.moviename)
            print(i.genere)
            print(i.timelen)
            print(i.releasedate)
            print()
        
        
class Showtime:
    def __init__(self):
        self.movie_time=[]
    def showtime(self):
        a=int(input("Enter Showtiming Id(1.mrng/2.afternoon/3.night) : "))
        if a==1:
            show1='5.00 AM to 9.00 AM'
            show2='9.15 AM to 12.00 AM'
            self.movie_time.append(show1)
            self.movie_time.append(show2)
        elif a==2:
            show1='12.15 AM to 3.00 PM'
            show2='3.15 PM to 6.00 PM'
            self.movie_time.append(show1)
            self.movie_time.append(show2)
        elif a==3:
            show1='6.15 PM to 9.00PM'
            show2='9.15 PM to 12.00AM' 
            self.movie_time.append(show1)
            self.movie_time.append(show2)
        print(showtym.movie_time)
        seat.enter_choice()
       
av_seat=[[1,2,3,4,5],[6,7,8,9,10],[11,12,13,0,15]]

class Seat_selection:
    
    def enter_choice(self):
        choice=input("Enter Choose your choice(normal/gold/platinum) : ")
        if choice=='normal':
            print("Select Your seat from available seat (0-already booked)")
            print(av_seat[0])
        elif choice=='gold':
            print("Select Your seat from available seat")
            print(av_seat[1])
        elif choice=='platinum':
            print("Select Your seat from available seat")
            print(av_seat[2])
    
        
    def seat_book(self):
        self.history_list=[]
        a=list(map(int,input("Enter your seat no: ").split(',')))
        self.l=len(a)
        
        for i in range(0,len(av_seat)):
            for j in range(0,len(av_seat[i])):
                if av_seat[i][j] in a:
                    av_seat[i][j]=0
                    now=datetime.now()
                    time=now.strftime("%y %m %d %H:%M:%S")
                    self.history_list.append(str(time))
        print("Your seat(s) has been booked!")
        print()
        print(av_seat)
        bookhis=Booking_history()
        bookhis.booking_history()
        

class Booking_history:
    def booking_history(self):
        m=seat.history_list[::-1]
        for i in m:
            print(i,end=',')
            print("name:",userdetail[0],end=',')
            print("id",userdetail[1])
        pay=Payment()
        pay.pay_mode()

       
    
class Payment:
    upi=[1234]
    credit=[123456789,333,'09/30']
    ph=1111111111
    
    def pay_mode(self):
        pay_method=input("Enter your mode of payment(upi/debit) : ")
        print("Your total : ",(seat.l)*200)
        print()
        if pay_method=="upi":
            Payment.met_upi(self)
        elif pay_method=="debit":
            Payment.met_debit(self)
        
    def met_upi(self):
        mob=int(input("Enter mobile no :"))
        if mob==Payment.ph:
            pin=int(input("Enter your upi id : "))
            if pin==Payment.upi[0]:
                self.charge=input("Enter Amount : ")
                Payment.change(self)
    def met_debit(self):
        mob=int(input("Enter mobile no :"))
        if mob==Payment.ph:
            card_no=int(input("Enter your cardno : "))
            cvv=int(input("Enter your cvv : "))
            exp=input("Enter Exp.date : ")
            if card_no==Payment.credit[0] and cvv==Payment.credit[1] and exp==Payment.credit[2]:
                self.charge=int(input("Enter Amount : "))
                Payment.change(self)
    def change(self):
        if self.charge==(seat.l)*200:
            Payment.greet(self)
        elif self.charge<(seat.l)*200:
            print("Please pay remaining :",(seat.m)*200)-self.charge
            Payment.greet(self)
        elif self.charge>(seat.l)*200:
            print("Amount repaid is :",self.charge-(seat.l)*200)
            Payment.greet(self)

    def greet(self):
        print()
        print("Thanks for Booking your seat!")
        print("Happy Moviesss!")
        
        




seat=Seat_selection()
userprof=UserProfile()
userprof.userprofile()
userprof.signin()
lis=MovieList()
lis.moviesdetail()
showtym=Showtime()
showtym.showtime()
seat=Seat_selection()
seat.seat_book()
