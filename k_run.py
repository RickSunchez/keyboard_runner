from tkinter import *
import random

def read_char(event):
	if event.keysym in ["Shift_L", "Shift_R", "Control_L", "Control_L", "Alt_L", "Alt_R"]:
		return False

	alphabet_enEN = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
	alphabet_ruRU = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"

	keyboard_char = event.char
	label_char = char_node["text"]

	if keyboard_char == label_char:
		alp = random.choice([alphabet_enEN, alphabet_ruRU])
		if alp == alphabet_enEN:
			print("EN")
		else:
			print("RU")
		
		char = random.choice(alp)

		char_node["text"] = char
	else:
		print("Ошибочка")

root = Tk()
root.title("Keyboard Runner v 0.1")
root.geometry("300x300")

game_frame = Frame(root)

char_node = Label(game_frame, text="A", justify="center", font="Arial 50")

root.bind("<Key>", read_char)

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

char_node.pack()
game_frame.grid(row=0, column=0)

root.focus_set()

root.mainloop()