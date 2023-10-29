from tkinter import *
import os
import psutil
import pygame

root = Tk()
root.geometry("353x225")
root.title("System Optimizer")


def optimize_computer():
    result_label = Label(text="")
    result_label.place(x=90, y=150)
    temp_folder = os.environ.get("TEMP")
    for root_pro, dirs, files in os.walk(temp_folder):
        for file in files:
            file_path = os.path.join(root_pro, file)
            try:
                os.remove(file_path)
            except Exception as e:
                pass

    try:
        os.system('rd /s /q C:\\$Recycle.Bin')
    except Exception as e:
        pass

    def dst_lbl():
        result_label.destroy()


    cpu_usage = psutil.cpu_percent(interval=1)
    pygame.mixer.init()
    pygame.mixer.music.load("v_effect1.mp3")
    pygame.mixer.music.play()
    optimize_button.config(text="BOOSTED")
    auto_f5()
    result_label.config(text="Cleanup done! CPU Usage: {0:.2f}%".format(cpu_usage))
    result_label.after(4000, dst_lbl)


def auto_f5():
    root.event_generate("<F5>")


background_image = PhotoImage(file="C:/Users/user/Desktop/bg2.png")
background_img = Label(image=background_image)
background_img.place(x=0, y=0)

optimize_button = Button(root, height=1, width=9, text="BOOST", relief=FLAT, command=optimize_computer, bg="#000987",
                         activeforeground="#3172e0",
                         activebackground="#0000ff", fg="#66b0ff", borderwidth=2, font=("Impact", 16))
optimize_button.place(x=130, y=90)

root.mainloop()
