#Program to keep track of the hired item in Julie's party store
#Created 29 Oct 2020
#Author: Celine Bui

from tkinter import *

def quit():
    main_window.destroy()

def setup_buttons():
    #all buttons used in the program - to the right of the entry boxes
    #Append Details, Print Details, Quit buttons are on the same row
    #Delete Row button is in the same column as quit
    Button(main_window, text="Quit", command=quit).grid(column=4, row=0)
    Button(main_window, text="Print Details", command=quit).grid(column=3, row=0)
    Button(main_window, text="Append Details", command=quit).grid(column=2, row=0)
    Button(main_window, text="Delete Row", command=quit).grid(column=4, row=2)

    #headings for entry boxes - Same column different rows, except for the Row heading                                                                                                                                                 
    Label(main_window, text="Customer Name").grid(column=0, row=0, sticky=W)
    Label(main_window, text="Receipt Number").grid(column=0, row=1, sticky=W)
    Label(main_window, text="Item Hired").grid(column=0, row=2, sticky=W)
    Label(main_window, text="Number Hired").grid(column=0, row=3, sticky=W)
    Label(main_window, text="Row").grid(column=2, row=2, sticky=W)

    #entry boxes
    entry_customer = Entry(main_window)
    entry_customer.grid(column=1, row=0, padx=10, pady=5)
    entry_receipt_number = Entry(main_window)
    entry_receipt_number.grid(column=1, row=1, padx=10, pady=5)
    entry_item = Entry(main_window)
    entry_item.grid(column=1, row=2, padx=10, pady=5)
    entry_number_hired = Entry(main_window)
    entry_number_hired.grid(column=1, row=3, padx=10, pady=5)
    entry_row = Entry(main_window)
    entry_row.grid(column=3, row=2, padx=10, pady=5)
    

#run the program
main_window = Tk()
setup_buttons()
main_window.mainloop()



