import tkinter as tk

# Function to evaluate the expression
def on_click(button_text):
    if button_text == "=":
        try:
            result = str(eval(entry.get()))  #Evaluating expression
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)  #Display result
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")  #Handling errors
    elif button_text == "C":
        entry.delete(0, tk.END)  #Clear the field
    else:
        entry.insert(tk.END, button_text)  #Add the button text to the entry field

# Create main window
root = tk.Tk()
root.title("Calculator")
root.geometry("514x514")

# Create the entry widget
entry = tk.Entry(root, font=("Arial", 24), bg="light gray", bd=10, relief="sunken", justify="right")
entry.grid(row=0, column=0, columnspan=4, ipadx=8, pady=20)

# Define buttons for number and operations
buttons = [
    ("7", "blue"), ("8", "blue"), ("9", "blue"), ("/", "dark blue"),
    ("4", "blue"), ("5", "blue"), ("6", "blue"), ("*", "dark blue"),
    ("1", "red"), ("2", "blue"), ("3", "red"), ("-", "dark blue"),
    ("0", "red"), ("C", "gray"), ("=", "green"), ("+", "dark blue")
]

# Create and place buttons on the calc
row = 1
col = 0
for (text, color) in buttons:
    button = tk.Button(root, text=text, width=10, height=2, font=("Arial", 18),
                       bg=color, command=lambda t=text: on_click(t))
    button.grid(row=row, column=col, padx=5, pady=5)
    
    col += 1
    if col > 3:
        col = 0
        row += 1

# Run the main loop
root.mainloop()
