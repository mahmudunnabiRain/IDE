import tkinter as tk
import tkinter.font as font
from tkinter.filedialog import askopenfilename, asksaveasfilename

window = tk.Tk()
window.title("Python IDE - Untitled")
window.iconbitmap("python_icon.ico")

buttonFont = font.Font(weight="bold", size=10)
textBoxFont = font.Font(family="Monaco", size=12)
terminalFont = font.Font(family="Monaco", size=10)


frame1 = tk.Frame(master=window,
                  relief=tk.FLAT,
                  borderwidth=1,
                  height=30,)

frame2 = tk.Frame(master=window,
                  relief=tk.FLAT,
                  borderwidth=1
                  )


def handle_click_open():
    """Open a file for editing."""
    filepath = askopenfilename(
        filetypes=[("Python Files", "*.py"), ("All Files", "*.*")]
    )
    if not filepath:
        return
    textBox.delete("1.0", tk.END)
    with open(filepath, "r") as input_file:
        text = input_file.read()
        textBox.insert(tk.END, text)
    window.title(f"Python IDE - {filepath}")


openButton = tk.Button(text="Open",
                       width=6,
                       height=1,
                       bg="orange",
                       fg="Black",
                       font=buttonFont,
                       command=handle_click_open,
                       master=frame1)


def handle_click_save():
    """Save the current file as a new file."""
    filepath = window.title()[13:len(window.title())]
    if filepath == "Untitled":
        filepath = asksaveasfilename(
            defaultextension="py",
            filetypes=[("Python Files", "*.py"), ("All Files", "*.*")],
        )
        if not filepath:
            return
    else:
        filepath = window.title()[13:len(window.title())]
    with open(filepath, "w") as output_file:
        text = textBox.get("1.0", tk.END)
        output_file.write(text)
    window.title(f"Python IDE - {filepath}")


saveButton = tk.Button(text="Save",
                       width=6,
                       height=1,
                       bg="orange",
                       fg="Black",
                       font=buttonFont,
                       command=handle_click_save,
                       master=frame1)


def handle_click_run():
    handle_click_save()
    filepath = window.title()[13:len(window.title())]
    if filepath != "Untitled":
        command = 'cmd /c "py {}"' .format(filepath)
        print(command)
        # os.system(command)


runButton = tk.Button(text="Run",
                      width=6,
                      height=1,
                      bg="orange",
                      fg="Black",
                      font=buttonFont,
                      command=handle_click_run,
                      master=frame1)


def handle_click_close():
    textBox.delete("1.0", tk.END)
    window.title("Python IDE - Untitled")


closeButton = tk.Button(text="Close",
                        width=6,
                        height=1,
                        bg="orange",
                        fg="Black",
                        font=buttonFont,
                        command=handle_click_close,
                        master=frame1)


textBox = tk.Text(master=frame2,
                  font=textBoxFont,
                  height=24,
                  width=60)

terminal = tk.Text(master=frame2,
                   font=terminalFont,
                   height=8,
                   width=60)


frame1.pack(fill=tk.X, side=tk.TOP)
openButton.place(x=0, y=0)
saveButton.place(x=60, y=0)
runButton.place(x=120, y=0)
closeButton.place(x=180, y=0)

textBox.pack(fill=tk.BOTH, expand=True)
terminal.pack(fill=tk.BOTH, expand=True)
frame2.pack(fill=tk.BOTH, expand=True)

window.update()
window.minsize(window.winfo_width(), window.winfo_height())
window.mainloop()
