from tkinter import *
import time

root=Tk()
root.geometry("1080x700")
root.title("TVS App")
root.configure(background="white")

title_lable= Label(text="Welcome to TVS App",bg="red",fg="white",padx=500*5, font=("none" , 15))
title_lable.pack()

photo = PhotoImage(file="Hero.png")
v_image = Label(image=photo, background="white")
v_image.pack()

def tab1():
     def tab2():
         def tab3():
             frame2.destroy()
             button1.destroy()
             button2.destroy()
             button3.destroy()
             button12.destroy()

             def back1():
                 title_lable2.destroy()
                 frame3.destroy()
                 button4.destroy()
                 button5.destroy()
                 frame9.destroy()
                 tab2()


             def click(event):
                 text = event.widget.cget("textvariable")
                 scvalue.set(text)
                 screen.update()
                 time.sleep(2)
                 scvalue.set("Oil Level is Ok")
                 screen.update()


             frame3 = Frame(root, bg="white")
             frame3.pack(side=BOTTOM,padx=40,pady=100)

             button4 = Button(frame3, fg="white", text="Oil level",textvariable="checking...",font="luciba 20 bold", bg="green",width=10,padx=5)
             button4.pack(side=LEFT, padx=80)
             button4.bind("<Button-1>", click)
             button5 = Button(frame3, fg="white", text="back", font="luciba 20 bold", bg="blue",width=10,command=back1)
             button5.pack(side=LEFT,padx=80)

             global scvalue

             scvalue= StringVar()
             scvalue.set("")
             frame9=Entry(root,bg="black")
             frame9.pack(side=TOP,pady=40,padx=40)

             screen=Entry(frame9,textvariable=scvalue,bg="white",width=200,font="luciba 40 bold",fg="black")
             screen.pack(side=TOP,pady=40,padx=50)



         def tab4():
             frame2.destroy()
             button1.destroy()
             button2.destroy()
             button3.destroy()
             button12.destroy()

             def click2(event):
                 text = event.widget.cget("textvariable")
                 scvalue2.set(text)
                 screen2.update()
                 time.sleep(2)
                 scvalue2.set("Engine Working Properly")


             def back2():
                 title_lable2.destroy()
                 frame4.destroy()
                 button6.destroy()
                 button7.destroy()
                 tab2()
                 frame10.destroy()

             frame4 = Frame(root, bg="white")
             frame4.pack(padx=40, pady=100, side=BOTTOM)

             button6 = Button(frame4, fg="white", text="Engine",textvariable="Checking...", font="luciba 20 bold", bg="green",width=10)
             button6.pack(side=LEFT,padx=80)
             button6.bind("<Button-1>", click2)
             button7 = Button(frame4, fg="white", text="back",font="luciba 20 bold", bg="blue", command=back2,width=10)
             button7.pack(side=LEFT,padx=80)

             global scvalue2

             scvalue2 = StringVar()
             scvalue2.set("")
             frame10 = Entry(root, bg="black")
             frame10.pack(side=TOP, pady=40, padx=40)

             screen2 = Entry(frame10, textvariable=scvalue2, bg="white", width=200, font="luciba 40 bold", fg="black")
             screen2.pack(side=TOP, pady=40, padx=50)

         def tab5():
             frame2.destroy()
             button1.destroy()
             button2.destroy()
             button3.destroy()
             button12.destroy()

             def click3(event):
                 text = event.widget.cget("textvariable")
                 scvalue3.set(text)
                 screen3.update()
                 time.sleep(2) 
                 scvalue3.set("All Electronic part working properly")


             def back3():
                 title_lable2.destroy()
                 frame5.destroy()
                 button8.destroy()
                 button9.destroy()
                 tab2()
                 frame11.destroy()

             frame5 = Frame(root, bg="white")
             frame5.pack(padx=40, pady=100, side=BOTTOM)
             button8 = Button(frame5, fg="white", text="Electronic",textvariable="Checking...", font="luciba 20 bold", bg="green",width=10)
             button8.pack(side=LEFT,padx=80)
             button8.bind("<Button-1>", click3)
             button9 = Button(frame5, fg="white", text="back", font="luciba 20 bold", bg="blue", command=back3,width=10)
             button9.pack(side=LEFT,padx=80)

             global scvalue3

             scvalue3 = StringVar()
             scvalue3.set("")
             frame11 = Entry(root, bg="black")
             frame11.pack(side=TOP, pady=40, padx=40)

             screen3 = Entry(frame11, textvariable=scvalue3, bg="white", width=200, font="luciba 40 bold", fg="black")
             screen3.pack(side=TOP, pady=40, padx=50)

         def tab6():
             button12.destroy()
             button3.destroy()
             button2.destroy()
             button1.destroy()
             frame2.destroy()

             def close():
                 time.sleep(1)
                 root.destroy()

             title_lable2 = Label(text="Thank You", bg="white", fg="black", font=("none", 150))
             title_lable2.pack(side=TOP,pady=180)

             button13 = Button(root, fg="white", text="Close", font="luciba 20 bold", bg="black",width=10,command=close)
             button13.pack(side=BOTTOM)

         v_image.destroy()
         button11.destroy()
         title_lable.destroy()

         title_lable2 = Label(text="TVS App", bg="red", fg="white", padx=500 * 5, font=("none", 15))
         title_lable2.pack()

         frame2 = Frame(root, bg="white")
         frame2.pack(padx=40, pady=290, side=TOP)

         button1 = Button(frame2, fg="white", text="Oil level", font="luciba 20 bold", bg="red", command=tab3,width=10)
         button1.pack(side=LEFT, padx=50)
         button2 = Button(frame2, fg="white", text="Engine", font="luciba 20 bold", bg="red",command=tab4,width=10)
         button2.pack(side=LEFT, padx=50)
         button3 = Button(frame2, fg="white", text="Electronic", font="luciba 20 bold", bg="red",command=tab5,width=10)
         button3.pack(side=LEFT, padx=50)
         button12 = Button(frame8, fg="white", text="Starting Vehicle", font="luciba 20 bold", bg="Green", command=tab6)
         button12.pack(side=LEFT, padx=80)

     frame8 = Frame(root, bg="white")
     frame8.pack(padx=80,side=BOTTOM, pady=40)

     button11 = Button(frame8, fg="white", text="Open Option", font="luciba 20 bold", bg="Black", command=tab2)
     button11.pack(side=LEFT, padx=80)

tab1()
root.mainloop()