import tkinter as tk
import Model

def test(text):
    label['text']=Model.validate(text)
    

if __name__ == "__main__":
    root=tk.Tk()

    bg_image=tk.PhotoImage(file='.//images//Picture by joanna-kosinska-on-unsplash1.png')
    bg_label=tk.Label(root,image=bg_image)
    bg_label.place(relheight=1,relwidth=1)
    # Cradits to joanna-kosinska for image

    frame1=tk.Frame(root,bg='#ff5e19',bd=3)
    frame1.place(relx=.25,rely=.4,relheight=.08,relwidth=.5)

    entry=tk.Entry(frame1,font=('Courier',12))
    entry.place(relx=.01,rely=.05,relheight=.9,relwidth=.76)

    btn1=tk.Button(frame1,text='Check',font=('Courier',12),command=lambda:test(entry.get()))
    btn1.place(relx=.78,rely=.05,relheight=.9,relwidth=.21)

    frame2=tk.Frame(root,bg='#ff5e19',bd=1)
    frame2.place(relx=.425,rely=.53,relheight=.08,relwidth=.15)

    label=tk.Label(frame2,text='',font=('Courier',12),bg='#ffffff')
    label.place(relx=.01,rely=.03,relheight=.94,relwidth=.98)

    root.title('Spam Detector')
    root.minsize(1050,600)
    root.iconbitmap('.//images//icons8-important-mail-64.ico')

    root.mainloop()