# GUI Calculator App
import tkinter as tk

# App window
win = tk.Tk()

# Screen size of the Application window
win.geometry("400x380")

# Disable resizing the app window
win.resizable(0, 0)

# Specify application name
win.title("Calculator")

# Required functions

input_value = ""

# Initialize StringVar
display_text = tk.StringVar()


# Function to continuously updates input field whenever you click a button
def click_button_action(item):
    global input_value
    input_value = input_value + str(item)
    display_text.set(input_value)


# Function to clear the display
def clear_button_action():
    global input_value
    input_value = ""
    display_text.set("")


# Function to calculate input values
def equal_button_action():
    global input_value
    result = str(eval(input_value))
    display_text.set(result)
    input_value = ""


# ----------------------------------------------------
# Frame for the display field

input_frame = tk.Frame(win, width=312, height=50, bd=0, highlightbackground="black", highlightcolor="black",
                       highlightthickness=3)

input_frame.pack(side=tk.TOP)

# Input field inside the 'Frame'

input_field = tk.Entry(input_frame, font=('arial', 18, 'bold'), textvariable=display_text, width=50, fg="white", bg="black", bd=0,
                       justify=tk.RIGHT)

input_field.grid(row=0, column=0)

input_field.pack(ipady=10)

# Frame for buttons

btns_frame = tk.Frame(win, width=312, height=272.5, bg="black")

btns_frame.pack()

# 1st row

tk.Button(btns_frame, text="Clear", fg="black", background='#eee', width=32, height=3, bd=0, cursor="hand2",
          command=lambda: clear_button_action()).grid(row=0, column=0, columnspan=3, padx=1, pady=1)

tk.Button(btns_frame, text="/", fg="black", width=10, height=3, bd=0, bg="red", cursor="hand2",
          command=lambda: click_button_action("/")).grid(row=0, column=3, padx=1, pady=1)

# 2nd row

tk.Button(btns_frame, text="7", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
          command=lambda: click_button_action(7)).grid(row=1, column=0, padx=1, pady=1)

tk.Button(btns_frame, text="8", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
          command=lambda: click_button_action(8)).grid(row=1, column=1, padx=1, pady=1)

tk.Button(btns_frame, text="9", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
          command=lambda: click_button_action(9)).grid(row=1, column=2, padx=1, pady=1)

tk.Button(btns_frame, text="X", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2",
          command=lambda: click_button_action("*")).grid(row=1, column=3, padx=1, pady=1)

# 3rd row

tk.Button(btns_frame, text="4", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
          command=lambda: click_button_action(4)).grid(row=2, column=0, padx=1, pady=1)

tk.Button(btns_frame, text="5", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
          command=lambda: click_button_action(5)).grid(row=2, column=1, padx=1, pady=1)

tk.Button(btns_frame, text="6", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
          command=lambda: click_button_action(6)).grid(row=2, column=2, padx=1, pady=1)

tk.Button(btns_frame, text="-", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2",
          command=lambda: click_button_action("-")).grid(row=2, column=3, padx=1, pady=1)

# 4th row

tk.Button(btns_frame, text="1", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
          command=lambda: click_button_action(1)).grid(row=3, column=0, padx=1, pady=1)

tk.Button(btns_frame, text="2", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
          command=lambda: click_button_action(2)).grid(row=3, column=1, padx=1, pady=1)

tk.Button(btns_frame, text="3", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
          command=lambda: click_button_action(3)).grid(row=3, column=2, padx=1, pady=1)

tk.Button(btns_frame, text="+", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2",
          command=lambda: click_button_action("+")).grid(row=3, column=3, padx=1, pady=1)

# 5th row

tk.Button(btns_frame, text="0", fg="black", width=21, height=3, bd=0, bg="#fff", cursor="hand2",
          command=lambda: click_button_action(0)).grid(row=4, column=0, columnspan=2, padx=1, pady=1)

tk.Button(btns_frame, text=".", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2",
          command=lambda: click_button_action(".")).grid(row=4, column=2, padx=1, pady=1)

tk.Button(btns_frame, text="=", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2",
          command=lambda: equal_button_action()).grid(row=4, column=3, padx=1, pady=1)

# Run main loop
win.mainloop()
