import tkinter as tk

#Handling button click event
def button_click():
    #print("Button clicked!")

    #Show an information message box
    msgbox.showinfo("Info", "Welcome to COS 102 GUT App!\n")

    #Ask for user confirmation 
    result = msgbox.askyesno("Confirmation", "Do you want to continue?")

#Create the main window
root = tk.Tk()
root.title("Home Page")
root.geometry("300x100")

#Add a label widget 
label = tk.Label(root, text ="Hello Friend \n")
label.pack()

#Add a button widget 
button= tk.Button(root, text = "Click Me!", command=button_click)
button.pack()

#Styling the button widget
button.config(fg="red", bg= "yellow")

#start the event loop 
root.mainloop()