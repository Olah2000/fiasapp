"""
Sebastian Olah
Muhammad Usman
Josh Rudnick

UML Diagram Assignment
CSIII
Mr.Ding

Starter code for GUI
"""

#Modules (Just for now importing entire module. Will change in later sessions)
import face_recognition
import cv2 as webcam
import numpy
from tkinter import *
from tkinter import ttk



"""
Main window segment... Will polish into with a
proper wrapper but produces a window! (A little past starter code but worth having.)
"""
tkinter = Tk()
frame = ttk.Frame(tkinter, padding = 15)
frame.grid()
ttk.Label(frame, text = "Test widget for group project").grid(column = 0, row = 0)
ttk.Button(frame, text = "Exit", command = tkinter.destroy).grid(column = 1, row = 0)
tkinter.mainloop()

attendance_status = "Absent"

"""
Main webcam segment.. Will also wrap up in future sessions
Works! Successfuly makes a frame that's live webcam capture.
"""
capture = webcam.VideoCapture(0)    # 0 is default value webcam device so should NEVER have to change

if not capture.isOpened():
    print("Error opening camera")
    exit()

while True:
    recieved, frame = capture.read()

    if not recieved:
        print("Can't recieve frame")
        break

    #Display
    webcam.imshow("frame", frame)
    if webcam.waitKey(1) == ord("q"):
        break

capture.release()
webcam.destroyAllWindows()




