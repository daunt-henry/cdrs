import tkinter
import cv2
import PIL.Image, PIL.ImageTk
import threading
import imutils
import time
from functools import partial

stream = cv2.VideoCapture("video1.mp4")
flag = True
def play(speed):
    global flag
    print(f"You clicked on play. Speed is {speed}")

        #Play the video in reverse
    frame1 = stream.get(cv2.CAP_PROP_POS_FRAMES)
    stream.set(cv2.CAP_PROP_POS_FRAMES, frame1 + speed)

    grabbed, frame = stream.read()
    if not grabbed:
        exit()
    frame = imutils.resize(frame, width = SET_WIDTH, height= SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0,0,image=frame,anchor=tkinter.NW)
    if flag:
        #play the video in forward
        canvas.create_text(129,25,fill="red", font= "Times 18  bold",text="DECISION PENDING")
    flag = not flag

def pending(decision):
    # 1. Display decison pending image
    frame = cv2.cvtColor(cv2.imread("pending.jpg"), cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame, width= SET_WIDTH, height= SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0,0,image=frame,anchor=tkinter.NW)
    #2. Wait for 1 second
    time.sleep(1)
    #3. Display sponder image
    frame = cv2.cvtColor(cv2.imread("SPONSER.jpg"), cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame, width= SET_WIDTH, height= SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0,0,image=frame,anchor=tkinter.NW)
    #4. Wait for 1.5 seconD
    time.sleep(1.5)
    #5. Display out/not out image.
    if decision == 'out':
        decisionImg = "OUT.jpg"
    else:
        decisionImg = "NOT OUT.jpg"
    frame = cv2.cvtColor(cv2.imread(decisionImg), cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame, width= SET_WIDTH, height= SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0,0,image=frame,anchor=tkinter.NW)
    pass

def out():
    thread=threading.Thread(target=pending, args=("out",))
    thread.daemon = 1
    thread.start()
    print("Player is out")

def not_out():
       thread=threading.Thread(target=pending, args=("not out",))
       thread.daemon = 1
       thread.start()
       print("Player is out")

SET_WIDTH = 650
SET_HEIGHT = 360

#tkinter gui starts here
window = tkinter.Tk()
window.title("Daunt Third Empire DRS System")
cv_img = cv2.cvtColor(cv2.imread("WELCOME.jpg"), cv2.COLOR_RGB2BGR)
canvas = tkinter.Canvas(window, width=SET_WIDTH, height=SET_HEIGHT)
photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(cv_img))
image_on_canvas = canvas.create_image(0,0,ancho=tkinter.NW, image=photo)
canvas.pack()

#button to control playback
btn = tkinter.Button(window, text="<< Previous (fast)", width = 50, command=partial(play, -25))
btn.pack()

btn = tkinter.Button(window, text="<< Previous (slow)", width = 50, command=partial(play, -2))
btn.pack()

btn = tkinter.Button(window, text="<< Next (slow)", width = 50, command=partial(play, 2))
btn.pack()

btn = tkinter.Button(window, text="<< Next (fast)", width = 50, command=partial(play, 25))
btn.pack()

btn.pack()
btn = tkinter.Button(window, text="Give out", width = 50, command=out)
btn.pack()
btn = tkinter.Button(window, text="Give Not OUt", width = 50, command=not_out)
btn.pack()

window.mainloop()