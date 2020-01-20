import tkinter as tk
rx=1
ry=1
rh=1
rw=1
root=tk.Tk()

bg_image=tk.PhotoImage(file='..//Raw material//Picture by joanna-kosinska-on-unsplash1.png')
bg_label=tk.Label(root,image=bg_image)
bg_label.place(relheight=1,relwidth=1)
# Cradits to joanna-kosinska


frame1=tk.Frame(root,bg='#ff5e19',bd=3)
frame1.place(relx=.25*rx,rely=.4*ry,relheight=.08*rh,relwidth=.5*rw)

entry=tk.Entry(frame1)
entry.place(relx=.01*rx,rely=.05*ry,relheight=.9*rh,relwidth=.76*rw)

btn1=tk.Button(frame1,text='Check',font=12)
btn1.place(relx=.78*rx,rely=.05*ry,relheight=.9*rh,relwidth=.21*rw)

frame2=tk.Frame(root,bg='#ff5e19',bd=1)
frame2.place(relx=.425*rx,rely=.53*ry,relheight=.08*rh,relwidth=.15*rw)

label=tk.Label(frame2,text='',font=(1),bg='#ffffff')
label.place(relx=.01*rx,rely=.03*ry,relheight=.94*rh,relwidth=.98*rw)

root.title('Spam Detector')
root.minsize(600,300)
root.iconbitmap('..//Raw material//icons8-important-mail-64.ico')

root.mainloop()
