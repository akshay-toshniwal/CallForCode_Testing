import sys
import os
from tkinter import *

root =Tk()
root.geometry("1340x680+0+0")
root.title("Voice To Power")
root.configure(background='#b3d9ff')
root.configure(relief=SOLID)
root.configure(bd=7)

###################################TOP#########################################


lblTitle=Label(root,font=('arial',60,'bold'),text='Voice To Power',bd=21,bg='black',
                fg='cornsilk',justify=CENTER,relief=RIDGE,pady=10,padx=10)
lblTitle.place(x=340,y=80)


##################################LABELS###########################################

lblopt1 =Label(root,font=('arial',20,'bold'),text='Risk Prediction',bd=21,
                bg="#b3d9ff",fg='Black',justify=CENTER,)
lblopt1.place(x=260,y=300)
lblopt2 =Label(root,font=('arial',20,'bold'),text='Online Order',bd=21,
                bg="#b3d9ff",fg='Black',justify=CENTER)
lblopt2.place(x=560,y=300)
lblopt3 =Label(root,font=('arial',20,'bold'),text='Donation Form',bd=21,
                bg="#b3d9ff",fg='Black',justify=CENTER)
lblopt3.place(x=850,y=300)


############################################FUNCTION################################################

def riskpredex():
    root.destroy()
    os.system("python prediction.py")

def migrationex():
    root.destroy()
    os.system("python onlineOrder.py")

def donationex():
    root.destroy()
    os.system("python donation.py")


#####################################Buttons####################################

btnEx=Button(root,padx=16,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=16,text='Execute',
                        bg='#b3d9ff',command=riskpredex)
btnEx.place(x=250,y=400)

btnEx1=Button(root,padx=16,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=16,text='Execute',
                        bg='#b3d9ff',command= migrationex)
btnEx1.place(x=550,y=400)

btnEx2=Button(root, padx=16, pady=1, bd=7, fg='black', font=('arial',16,'bold'), width=16, text='Execute',
              bg='#b3d9ff',command= donationex)
btnEx2.place(x=850,y=400)





root.mainloop()