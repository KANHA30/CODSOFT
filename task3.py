import tkinter
import random

r=tkinter.Tk()
r.title("PASSWORD GENERATOR")
r.geometry("500x300")
r.config(bg="navy")
def update():                                   
    t1.config(text="")
    complexmsg.config(text="")
def weakpassword(l):
    p=""
    for i in range(l):
        ran=random.randrange(1,3)
        if ran==1:                                    
            p+=chr(random.randrange(65,91))
        else:                                         
            p+=chr(random.randrange(97,123))
    return p                                         
def moderatepassword(l):
    print("Y")
    p=""
    for i in range(l):
        ran=random.randrange(1,4)
        if ran==1:                        
            p+=chr(random.randrange(65,91))
        elif ran==2:                               
            p+=chr(random.randrange(97,123))
        else:
            p+=chr(random.randrange(48,58))            
    return p                                         
                          
def strongpassword(l):
    p=""
    for i in range(l):
        p+=chr(random.randrange(48,123))              
    return p                                         

                                   
def click():
    if length.get()=="":                        
        t1.config(text=f"Enter the number")            
        r.after(2000,update)                
        return
        
    if length.get().isdigit():                                         

        l=int(length.get())
        if l>=5 and l<=50:                                          

            if complexity.get() != "None":                            
                password=""
                
                if complexity.get()=="weak":                          
                    password=weakpassword(l)
                  
                    
                elif complexity.get()=="moderate":                       
                    password=moderatepassword(l)
                 
                    
                else:
                    password=strongpassword(l)                           
           
                    
                rr=tkinter.Tk()                                   
                rr.geometry("500x100")
                rr.config(bg="midnightblue")
                label=tkinter.Label(rr,text=password,bg="midnightblue",fg="white",font=("Cascadia Code ExtraLight",30,"bold","italic"))
                label.pack(pady=20)
              
    
            else:                                                       
                complexmsg.config(text=f"specify the complexity of password")
                r.after(2000,update)
            
    
        else:                                                          
            t1.config(text=f"length should be in between 5 to 50")
            r.after(2000,update)
    else:                                                                
        t1.config(text=f"length should be in digits only")
        r.after(2000,update)
    
    
heading=tkinter.Label(text="-: PASSWORD GENERATOR :-",bg="navy",fg="snow",font=("ALGERIAN",17,"italic"),padx=50)      
heading.pack(anchor="nw",padx=50,pady=10)

                                  
f1=tkinter.Frame(r,bg="navy")
length=tkinter.StringVar()                          
t=tkinter.Label(f1,text="Password Length:",fg="white",bg="navy",font=("Cascadia Code ExtraLight",12,"bold"))       
t.grid(row=0,column=0,padx=5)

lengthentry=tkinter.Entry(f1,text=length,bg="skyblue",fg="black",font=("Cascadia Code ExtraLight",10,"bold"),justify="center")   
lengthentry.grid(row=0,column=1,padx=4)

t1=tkinter.Label(f1,text="",font=("Ariel",10),bg="navy",fg="red")              
t1.grid(row=1,column=1)

f1.pack(pady=20)


f2=tkinter.Frame(r,bg="navy")
complexity=tkinter.StringVar()                       
complexity.set(None)

radio1=tkinter.Radiobutton(f2,text="Weak",fg="black",bg="skyblue",font=("Cascadia Code ExtraLight",12,"bold"),variable=complexity,value="weak")    
radio1.grid(row=0,column=0,padx=5)

radio2=tkinter.Radiobutton(f2,text="Moderate",fg="black",bg="skyblue",font=("Cascadia Code ExtraLight",12,"bold"),variable=complexity,value="moderate")
radio2.grid(row=0,column=1,padx=5)

radio3=tkinter.Radiobutton(f2,text="Strong",fg="black",bg="skyblue",font=("Cascadia Code ExtraLight",12,"bold"),variable=complexity,value="strong")   
radio3.grid(row=0,column=2,padx=5)

f2.pack()

complexmsg=tkinter.Label(r,text="",font=("Ariel",10),bg="navy",fg="red")       


f3=tkinter.Frame(r,bg="navy")

b=tkinter.Button(f3,text="Generate",bg="darkgreen",fg="white",font=("Cascadia Code ExtraLight",12,"bold"),command=click)    
b.grid(row=0,column=0,padx=5)
b1=tkinter.Button(f3,text="Quit",bg="red",fg="white",font=("Cascadia Code ExtraLight",12,"bold"),command=quit)        
b1.grid(row=0,column=1,padx=5)

f3.pack(pady=10)



r.mainloop()