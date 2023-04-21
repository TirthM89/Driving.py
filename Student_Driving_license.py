# Basic tkinter template
from tkinter import *

root = Tk()

root.title("Driving License")

root.configure(bg="white")

root.geometry("200x200")



# Create all the labels required to be displayed


label_heading = Label(root, text = "Driving License", bg = "red", fg = "white")
label_id = Label(root)
label_name = Label(root)
label_dob = Label(root)
label_pin = Label(root)
label_address = Label(root)
label_vehicle_type = Label(root)
# Define the function
def driving():
    print("Driving License")
    id = 7992571108
    print(id)
    label_id["text"]= id
    name = "John Chi"
    print(name)
    label_name["text"]= name
    dob = 22/6/2001
    print(dob)
    label_dob["text"]= dob
    pin = 968642
    print(pin)
    label_pin["text"]= pin
    address = "406 Frankins Street, South Wyoming, Sydney, England"
    print(address)
    label_address["text"]= address
    vt = "Class D"
    print(vt)
    label_vehicle_type["text"]= vt
    
# Create a button

button1 = Button(root, text = "Show Details", command = driving)

button1.configure(width = 20 , activebackground = "#9EC6EE", relief= FLAT)
button1.pack()
label_heading.pack()
label_id.pack()
label_name.pack()
label_dob.pack()
label_pin.pack()
label_address.pack()
label_vehicle_type.pack()
# tkinter basic template end statement
root.mainloop()