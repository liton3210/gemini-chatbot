import tkinter as tk

root = tk.Tk()

def show_message() -> None:
    """Print the text typed in the entry box."""
    label.config (text=entry.get())


def close_chat() -> None:
    """Close chat window"""
    root.destroy()
    
    

root.title("Chat bot.")
root.geometry("500x500")

label = tk.Label(root, text="AI chat bot.")
label.place(y=20, x=200)

green_button = tk.Button(root, text="Green", bg="green", fg="black", font=("Arial", 10), command=show_message)
green_button.place(y=35, x=40)

red_button = tk.Button(root, text="Red", bg="red", fg="black", font=("Arial", 10), command=close_chat)
red_button.place(y=35, x=400)

entry = tk.Entry(root, font=("Arial", 10), width=20)
entry.place(y=150, x=180)


root.mainloop()