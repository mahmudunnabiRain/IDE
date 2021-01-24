import tkinter as tk
import tkinter.font as font
from tkinter.filedialog import askopenfilename

window = tk.Tk()
window.title("IDE")

buttonFont = font.Font(weight="bold", size=10)
textBoxFont = font.Font(family="Monaco", size=12)

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


def handle_click_open():
    print("Open button was clicked!")
    """Open a file for editing."""
    filepath = askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if not filepath:
        return
    textBox.delete("1.0", tk.END)
    with open(filepath, "r") as input_file:
        text = input_file.read()
        textBox.insert(tk.END, text)
    window.title(f"Simple Text Editor - {filepath}")


openButton = tk.Button(text="Open",
                       width=6,
                       height=1,
                       bg="orange",
                       fg="Black",
                       font=buttonFont,
                       command=handle_click_open,
                       master=frame1)


def handle_click_save():
    print("Save button was clicked!")


saveButton = tk.Button(text="Save",
                       width=6,
                       height=1,
                       bg="orange",
                       fg="Black",
                       font=buttonFont,
                       command=handle_click_save,
                       master=frame1)


def handle_click_run():
    print("Run button was clicked!")


runButton = tk.Button(text="Run",
                      width=6,
                      height=1,
                      bg="orange",
                      fg="Black",
                      font=buttonFont,
                      command=handle_click_run,
                      master=frame1)

textBox = tk.Text(master=frame2,
                  font=textBoxFont)

frame1.pack(fill=tk.X, side=tk.TOP)
openButton.place(x=0, y=0)
saveButton.place(x=60, y=0)
runButton.place(x=120, y=0)

frame2.pack(fill=tk.BOTH, expand=True)
textBox.pack(fill=tk.BOTH, expand=True)


window.mainloop()
