from tkinter import *
import pyscreenrec

mafixx = Tk()
mafixx.geometry("400x600")
mafixx.title("Screen Recorder")
mafixx.config(bg="#fff")
mafixx.resizable(False,False)

def start_rec():
    file = Filename.get()
    recorder.start_recording(str(file+".mp4"),10)

def pause_rec():
    recorder.pause_recording()

def resume_rec():
    recorder.resume_recording()

def stop_rec():
    recorder.stop_recording()

recorder = pyscreenrec.ScreenRecorder()

#icon
image_icon = PhotoImage(file="./img/ico.png")
mafixx.iconphoto(False,image_icon)

#background-images
imageCam = PhotoImage(file="./img/camera.png")
Label(mafixx,image=imageCam,bg="#fff").place(x=165,y=50)

#head
lbl = Label(mafixx,text="Screen Recorder by mafixx",bg="#fff",font="arial 15 bold")
lbl.pack(pady=20)

#entrypoint
Filename = StringVar()
entry = Entry(mafixx,textvariable=Filename,width=18,font="arial 15")
entry.place(x=100,y=350)
Filename.set("NewRec1")

#buttons
imageRec = PhotoImage(file="./img/record.png")
start = Button(mafixx,image=imageRec,bd=0,bg="#fff",command=start_rec)
start.place(x=165,y=250)

imageResume = PhotoImage(file="./img/play.png")
resume = Button(mafixx,image=imageResume,bd=0,bg="#fff",command=resume_rec)
resume.place(x=50,y=450)

imagePause = PhotoImage(file="./img/pause.png")
pause = Button(mafixx,image=imagePause,bd=0,bg="#fff",command=pause_rec)
pause.place(x=185,y=450)

imageStop = PhotoImage(file="./img/stop.png")
stop = Button(mafixx,image=imageStop,bd=0,bg="#fff",command=stop_rec)
stop.place(x=300,y=450)

mafixx.mainloop()
