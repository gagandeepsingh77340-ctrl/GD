# import tkinter as tk
# from PIL import Image,ImageTk
# root=tk.Tk()
# root.geometry("600x300")
# root.title("Hello")
# root.minsize(100,100)
# root.maxsize(700,800)

# photo=Image.open("Tk/—Pngtree—a red suv car in_20147947.png")

# img= photo.resize((300,250))

# # label=tk.Label(image=photo,width=300,height=250)

# photo=ImageTk.PhotoImage(img)

# label=tk.Label(image=photo)


# label.pack()
# root.mainloop()



import tkinter as tk
import time

window=tk.Tk()
window.geometry("1500x800")
window.maxsize(1500,800)
window.configure(bg="white")

frame=tk.Frame(window,bg="red",width=1500, height=50)
frame.pack(side="top")

photo=tk.PhotoImage(file="Tk/6727646.png")
label=tk.Label(window,image=photo,bg="white")
label.pack(side="left")

# frame9=Entry(window,bg="black")
# frame9.pack(side=TOP,pady=40,padx=40)

# screen=Entry(frame9,textvariable=scvalue,bg="white",width=200,font="luciba 40 bold",fg="black")
# screen.pack(side=TOP,pady=40,padx=50)

frame2=tk.Frame(window,bg="green",width=1500, height=50)
frame2.pack(side="bottom")

b=tk.Button(window,text="Close",command=label.destroy,width=5,height=2)
b.pack(side="right",padx=100)
# b2=tk.Button(text="Close")
# b2.pack()

# time.sleep(2)
# label.destroy


# frame=tk.Frame(window)
# frame.pack()
# button=tk.Button(text="Close",command=hello())
# button.pack()
window.mainloop()