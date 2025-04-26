# Imports
import tkinter as tk

# `main` function
def main():
    # Assigning the `Tk` class
    app = tk.Tk()

    # Setting the app resolution
    app.geometry('700x400')

    # `button_1` config
    button_1 = tk.Button(text="Press to say hi to Carol ma'am!", command=lambda: print("Hi ma'am"), relief="sunken")
    button_1.pack()

    # Running the app's mainloop
    app.mainloop()

# Run only if executed from this script
if __name__ == "__main__":
    main()
    