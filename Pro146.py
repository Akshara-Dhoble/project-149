from tkinter import*
import random

root = Tk()
root.title("Random Password")
root.geometry("500x500")
root.configure(background="blue")

label1 = Label(root)

def generate_random_password():
    list1 = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    random_no1 = random.randint(53,63)
    random_no2 = random.randint(27,52)
    random_no3 = random.randint(1,26)
    random_no4 = random.randint(64,94)
    random_no5 = random.randint(64,94)
    
    random_alpha1 = list1[random_no1]
    random_alpha2 = list1[random_no2]
    random_alpha3 = list1[random_no3]
    random_alpha4 = list1[random_no4]
    random_alpha5 = list1[random_no5]
    
    label1["text"] = rendom_alpha1 + rendom_alpha2 + rendom_alpha3 + rendom_alpha4 + rendom_alpha5
    
btn = Button(root , text="Generated Random Password" , command=generate_random_password)  
btn.place(relx=0.5 , rely=0.4 , anchor=CENTER)
label1.place(relx=0.5 , rely = 0.5 , anchor=CENTER)  

root.mainloop()
