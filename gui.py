# gui.py - everything the user sees (Tkinter). Each button calls an on_... function here,
# which reads the fields, calls validation.py and database.py, and shows a messagebox.
# Orthogonality: this file only does the screen, no SQL or checks here.

import tkinter as tk
from tkinter import messagebox
from database import create_table, add_vehicle, plate_exists, delete_vehicle, get_vehicle
from validation import validate_vehicle

create_table()

# 1 - THE WINDOW

root = tk.Tk() # creates the blank window..
root.title('Car Dealership') # creates the title of the window
root.geometry("1200x700") # fixed size of the window
root.resizable(False, False) # can't be resized or maximised -> looks the same on any screen
root.configure(bg="#1c1c1e")

 # keeps the window open at any time... ALWAYS AT THE END!!!!
# 2 - BASIC WIDGETS
# 3 PACK # allocates widget beneath the previous one    

tk.Label(root, text="Car Dealership", font=("Arial", 32, "bold"), width=100, background="#c1121f", fg="white").pack(pady=30) # pady = 20px space between top and bottom.


def on_add():
    win = tk.Toplevel(root) # creates a new window, its parent is root.
    win.title("Add Vehicle")

    win.geometry("600x300")

    #creating FROM
    tk.Label(win, text="PLATE").grid(row=0, column =0) #you create a text label and write plate on it
    plate = tk.Entry(win)
    plate.grid(row=0, column=1, padx=15)

    tk.Label(win, text="BRAND").grid(row=1, column=0)
    brand = tk.Entry(win)
    brand.grid(row=1, column=1, padx=15, pady=15)

    tk.Label(win, text="MODEL").grid(row=2, column=0)
    model = tk.Entry(win) #you create model, which is an entry inside win... an input inside the new window
    model.grid(row=2, column=1, padx=15,)

    tk.Label(win, text="YEAR").grid(row=3, column=0)
    year = tk.Entry(win) # creating a new entry (input). first you create it, then you show it
    year.grid(row=3, column=1, padx=15, pady=15)

    tk.Label(win, text="PRICE").grid(row=4, column=0)
    price = tk.Entry(win) # I create the input and store it in price.
    price.grid(row=4, column=1, padx=15)

    tk.Label(win, text="KMs").grid(row=5, column=0)
    km = tk.Entry(win)
    km.grid(row=5, column=1, padx=15, pady=15)


    def on_save():

        if plate_exists(plate.get()): # if true
            messagebox.showerror("ERROR ","PLATE ALREADY EXISTS")

        else:
            res = validate_vehicle(plate.get(), year.get(), price.get(), km.get())
            if res == True:
                add_vehicle(plate.get(), brand.get(), model.get(), year.get(), price.get(), km.get())
                messagebox.showinfo("Saved", "Vehicle added")
            else:
                messagebox.showerror("ERROR", res)




    tk.Button(win, text="SAVE VEHICLE", width=25, command=on_save ,background="#c1121f", fg="white").grid(row=6, column=0, columnspan=2)


def on_list():

    listwin = tk.Toplevel(root)
    listwin.title("LIST OF VEHICLES")
    listwin.geometry("650x450")

    tk.Label(listwin, text="Insert BRAND OR PLATE to filter the vehicles", font=20).grid(pady=15, columnspan=11)

    filtervehicle = tk.Entry(listwin, width=25, font=20)
    filtervehicle.grid(columnspan=11)


    def on_filter():
       rows = get_vehicle(filtervehicle.get()) # what this function returns is a list of tuples.
       if len(rows) == 0:
            messagebox.showerror("ERROR", "NO RESULTS FOUND")

       else:
        row = 1
        count = 5
        for i in rows: #rows is the list of tuples... [(1, 1, 1, 1, 1, )]
            tk.Label(listwin, text=row).grid(row=count, column=0)
            tk.Label(listwin, text="Plate", width=5, background="#2b2d42", fg="white").grid(row=count, column=1, padx=5)
            tk.Label(listwin, text=i[0]).grid(row=count, column=2)
            tk.Label(listwin, text="Brand", width=5, background="#2b2d42", fg="white").grid(row=count, column=3, padx=5)
            tk.Label(listwin, text=i[1]).grid(row=count, column=4)
            tk.Label(listwin, text="Model", width=5, background="#2b2d42", fg="white").grid(row=count, column=5, padx=5)
            tk.Label(listwin, text=i[2]).grid(row=count, column=6)
            tk.Label(listwin, text="Year", width=5, background="#2b2d42", fg="white").grid(row=count, column=7, padx=5)
            tk.Label(listwin, text=i[3]).grid(row=count, column=8)
            tk.Label(listwin, text="Price", width=5, background="#2b2d42", fg="white").grid(row=count, column=9, padx=5)
            tk.Label(listwin, text=i[4]).grid(row=count, column=10)
            tk.Label(listwin, text="KMs", width=5, background="#2b2d42", fg="white").grid(row=count, column=11, padx=5)
            tk.Label(listwin, text=i[5]).grid(row=count, column=12)

            count = count + 1
            row =row+1
    
    tk.Button(listwin, text="FILTER", width=15, command= on_filter,background="#c1121f", fg="white").grid(padx=15, pady=15, columnspan=11)
    
    on_filter()



def on_delete():

    delwin = tk.Toplevel(root)
    delwin.geometry("350x200")
    delwin.title("ENTER PLATE")
    

    tk.Label(delwin, text="Enter the vehicle plate to DELETE", width=25).grid(padx=15, pady=15)
    delinput = tk.Entry(delwin, width=15, font=("Arial", 14))
    delinput.grid()

    def on_submit():

        if plate_exists(delinput.get()):

            delete_vehicle(delinput.get())
            messagebox.showinfo("SUCCESS", "VEHICLE DELETED SUCCESSFULLY")
        else:
            messagebox.showerror("ERROR", "VEHICLE NOT FOUND")



    tk.Button(delwin, text="SUBMIT",  command = on_submit, background="#c1121f", fg="white", width=15).grid(pady=15)
    


nav = tk.Frame(root, background="#1c1c1e" ,width=100) 
# invisible box (like a <div>) inside the window, to group the buttons
nav.pack()            # shows the box below the title
# Each button: parent = nav (goes inside the box), width=25 = same width for all,
# side="left" = next to the previous one (not below), padx=5 = 5px gap on each side

tk.Button(nav, text="Add Vehicle", command=on_add, width=33,height=3, font=("Arial", 11), background="#c1121f", fg="white", cursor="hand2",).pack(side="left", padx=5)
tk.Button(nav, text="List Vehicles", command=on_list,width=33,height=3, font=("Arial", 11), background="#c1121f", fg="white", cursor="hand2").pack(side="left", padx=5)
tk.Button(nav, text="Delete Vehicle", command=on_delete,width=33,height=3, font=("Arial", 11), background="#c1121f", fg="white", cursor="hand2").pack(side="left", padx=5)

im = tk.Frame(root, bg="#1c1c1e")
im.pack(pady=25)


car_img2 = tk.PhotoImage(file="img/mercedesult.png").subsample(2) # subsample(2) = half the size, so it fits
tk.Label(im, image=car_img2, background="#1c1c1e").pack(side="left", padx=0)
tk.Label(im, image=car_img2, background="#1c1c1e").pack(side="left", padx=0)



















root.mainloop()