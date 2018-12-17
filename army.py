	elif(button1["text"] == "O" and button2["text"] == "O" and button3["text"] == "O" or
		button4["text"] == "O" and button5["text"] == "O" and button6["text"] == "O" or
		button7["text"] == "O" and button8["text"] == "O" and button9["text"] == "O" or
		button3["text"] == "O" and button5["text"] == "O" and button7["text"] == "O" or
		button1["text"] == "O" and button5["text"] == "O" and button9["text"] == "O" or
		button1["text"] == "O" and button4["text"] == "O" and button7["text"] == "O" or
		button2["text"] == "O" and button5["text"] == "O" and button8["text"] == "O" or
		button3["text"] == "O" and button6["text"] == "O" and button9["text"] == "O"):
		tkinter.messagebox.showinfo("Winner O", "Selamat anda menang, Terima Kasih")
		exit()