from tkinter import *

def start():
	global time_stopped
	time_stopped = False
	window.after(10, main)

def stop():
	global time_stopped
	time_stopped = True
	window.after(10, main)

def reset():
	global time
	time = [0, 0, 0]

def main():
	global time_stopped
	time[2] += 1
	if time[2] == 100:
		time[1] += 1
		time[2] = 0
	if time[1] == 60:
		time[0] += 1
		time[1] = 0

	time_screen['text'] = str(time[0]) + ":" + str(time[1]) + ":" + str(time[2])
	if not time_stopped:
		window.after(10, main)

window = Tk()
window.geometry("500x300")
window.resizable(False, False)
window.title("MineSweeper")

time_screen = Label(window, text = "0:0:0")
time_screen.place(x = 0, y = 0, width = 500, height = 50)

start_button = Button(window, text = 'Start', command = start)
start_button.place(x = 50, y = 100, width = 75, height = 50)

stop_button = Button(window, text = "Stop", command = stop)
stop_button.place(x = 150, y = 100, width = 75, height = 50)

reset_button = Button(window, text = "Reset", command = reset)
reset_button.place(x = 250, y = 100, width = 75, height = 50)

time = [0, 0, 0]
time_stopped = True

window.mainloop()