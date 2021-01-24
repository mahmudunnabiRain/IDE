import tkinter as tk

window = tk.Tk()

frame1 = tk.Frame(master=window,
                  relief=tk.FLAT,
                  borderwidth=1,
                  height=30,
                  width=400,)

frame2 = tk.Frame(master=window,
                  relief=tk.FLAT,
                  borderwidth=1,
                  height=40,
                  width=400,)

greeting = tk.Label(text="Hello World",
                    foreground="white",
                    background="black",
                    width=20,
                    height=1)

fileButton = tk.Button(text="File",
                       width=4,
                       height=1,
                       bg="orange",
                       fg="Black",
                       master=frame1)

editButton = tk.Button(text="Edit",
                       width=4,
                       height=1,
                       bg="orange",
                       fg="Black",
                       master=frame1)

runButton = tk.Button(text="Run",
                      width=4,
                      height=1,
                      bg="orange",
                      fg="Black",
                      master=frame1)


textBox = tk.Text(master=frame2)


frame1.pack(fill=tk.X, side=tk.TOP)
fileButton.place(x=0, y=0)
editButton.place(x=60, y=0)
runButton.place(x=120, y=0)

frame2.pack(fill=tk.BOTH, expand=True)
textBox.pack()

window.mainloop()
