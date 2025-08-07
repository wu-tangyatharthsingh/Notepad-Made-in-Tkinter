def notepad_window():
    import tkinter as tk 
    from tkinter import filedialog

    notepad_window = tk.Tk()
    notepad_window.geometry("500x500")
    notepad_window.title("NotePad")
    notepad_window.resizable(False, False)
    notepad_window.config(bg="pink")

    # Frame for Text widget + Scrollbar
    text_frame = tk.Frame(notepad_window)
    text_frame.place(x=10, y=40, width=480, height=440)

    # Scrollbar
    scrollbar = tk.Scrollbar(text_frame)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    # Textbox with scrolling
    textbox = tk.Text(
        text_frame,
        wrap="word",
        yscrollcommand=scrollbar.set,
        font=("Helvetica", 12),
        fg="black",
        bg="white",
        insertbackground="black",  # Cursor color
        selectbackground="#cceeff",
        selectforeground="black"
    )
    textbox.pack(fill=tk.BOTH, expand=True)
    scrollbar.config(command=textbox.yview)

    def savefile():
        file = filedialog.asksaveasfile(mode='w', defaultextension='.txt')
        if file:
            content = textbox.get(1.0, tk.END)
            file.write(content)
            file.close()

    def openfile():
        file = filedialog.askopenfile(mode='r')
        if file:
            content = file.read()
            textbox.delete(1.0, tk.END)
            textbox.insert(tk.END, content)
            file.close()

    def clearfile():
        textbox.delete(1.0, tk.END)

    # Buttons
    tk.Button(notepad_window, text="Save", command=savefile).place(x=10, y=7)
    tk.Button(notepad_window, text="Open", command=openfile).place(x=60, y=7)
    tk.Button(notepad_window, text="Clear", command=clearfile).place(x=118, y=7)
    notepad_window.mainloop()

notepad_window()