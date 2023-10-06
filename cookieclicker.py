import tkinter as tk

# Initialize variables
cookie_count = 0

# Function to increase cookie count when the button is clicked
def click_cookie():
    global cookie_count
    cookie_count += 1
    cookie_label.config(text=f"Cookies: {cookie_count}")

# Create the main window
root = tk.Tk()
root.title("Cookie Clicker")

# Create and configure a label to display the cookie count
cookie_label = tk.Label(root, text=f"Cookies: {cookie_count}", font=("Helvetica", 24))
cookie_label.pack(pady=20)

# Create a button to click and earn cookies
cookie_button = tk.Button(root, text="Click me!", command=click_cookie, font=("Helvetica", 18))
cookie_button.pack()

# Run the main loop
root.mainloop()
