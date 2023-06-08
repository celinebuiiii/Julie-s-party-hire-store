#Program to keep track of the hired item in Julie's party store
#Created 29 Oct 2020
#Author: Celine Bui

from tkinter import *

def quit():
    main_window.destroy()

def print_hire_details():
    #global variables used
    global name_count, total_entries
    name_count=0

    #column headings -  row value is the same while column increases
    Label(main_window, font=("Helvetica 15 bold"), text="Row").grid(column=0, row=5)
    Label(main_window, font=("Helvetica 15 bold"), text="Customer").grid(column=1, row=5)
    Label(main_window, font=("Helvetica 15 bold"), text="Receipt No.").grid(column=2, row=5)
    Label(main_window, font=("Helvetica 15 bold"), text="Item Hired").grid(column=3, row=5)
    Label(main_window, font=("Helvetica 15 bold"), text="No. Hired").grid(column=4, row=5)

    while name_count < total_entries :
        Label(main_window, text=name_count).grid(column=0, row=name_count+6)
        Label(main_window, text=(hire_details[name_count][0])).grid(column=1, row=name_count+6)
        Label(main_window, text=(hire_details[name_count][1])).grid(column=2, row=name_count+6)
        Label(main_window, text=(hire_details[name_count][2])).grid(column=3, row=name_count+6)
        Label(main_window, text=(hire_details[name_count][3])).grid(column=4, row=name_count+6)
        name_count += 1 

def append_details():
    global total_entries, hire_details, entry_customer, entry_receipt_number, entry_item, entry_number_hired

    #retain the info of each new entry - variables must be in order to be under correct headings
    hire_details.append([entry_customer.get(), entry_receipt_number.get(), entry_item.get(), entry_number_hired.get()])
    total_entries += 1
    

def setup_buttons():
    global entry_customer, entry_receipt_number, entry_item, entry_number_hired
    #all buttons used in the program - to the right of the entry boxes
    #Append Details, Print Details, Quit buttons are on the same row
    #Delete Row button is in the same column as quit
    Button(main_window, text="Quit", command=quit).grid(column=4, row=0)
    Button(main_window, text="Print Details", command=print_hire_details).grid(column=3, row=0)
    Button(main_window, text="Append Details", command=append_details).grid(column=2, row=0)
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
def main():
    global main_window, total_entries, hire_details
    total_entries = 0
    hire_details = [] #empty list for program to add details from each entry
    main_window = Tk()
    setup_buttons()
    main_window.mainloop()

main()


