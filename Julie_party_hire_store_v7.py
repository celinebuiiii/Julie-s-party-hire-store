#Program to keep track of the hired item in Julie's party store
#Created 29 Oct 2020
#Author: Celine Bui

#import Tkinter to make GUI
from tkinter import *

#subroutine to quit window
def quit(): #brackets are empty due to no input
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

    #add row for every time new entry is added
    while name_count < total_entries :
        Label(main_window, text=name_count).grid(column=0, row=name_count+6)
        Label(main_window, text=(hire_details[name_count][0])).grid(column=1, row=name_count+6)
        Label(main_window, text=(hire_details[name_count][1])).grid(column=2, row=name_count+6)
        Label(main_window, text=(hire_details[name_count][2])).grid(column=3, row=name_count+6)
        Label(main_window, text=(hire_details[name_count][3])).grid(column=4, row=name_count+6)
        name_count += 1 

def check_inputs():
    global hire_details, entry_customer, entry_receipt, entry_item, entry_number_hired, delete_input
    input_check = 0
    #messages appear next to entry boxes
    Label(main_window, text="               ") .grid(column=2,row=0)
    Label(main_window, text="               ") .grid(column=2,row=1)
    Label(main_window, text="               ") .grid(column=2,row=2)
    Label(main_window, text="               ") .grid(column=2,row=3)
    #Check that customer's name entry is not blank, set error text if blank
    if len(entry_customer.get()) == 0 :
        Label(main_window, fg="red", text="Required") .grid(column=2, row=0)
        input_check = 1
    #Check that receipt number entry is not blank, set error text if blank
    if len(entry_receipt.get()) == 0 :
        Label(main_window, fg="red", text="Required") .grid(column=2, row=1)
        input_check = 1
    #Check that receipt number entry is a number, set error text if text
    elif (entry_receipt.get().isdigit()):
        input_check = 0
    else :
        Label(main_window, fg="red", text="Numbers") .grid(column=2, row=1)
        input_check = 1
    #Check that item entry is a not blank, set error text if blank
    if len(entry_item.get()) == 0 :
        Label(main_window, fg="red", text="Required") .grid(column=2, row=2)
        input_check = 1
    #Check that number of item hired entry is between 1 and 500, set error text if not
    if (entry_number_hired.get().isdigit()) :
        if int(entry_number_hired.get()) < 1 or int(entry_number_hired.get()) > 500:
            Label(main_window, fg="red", text="1-500 only") .grid(column=2, row=3)
            input_check = 1
    #Check that number of item hired entry is a number, set error text if text
    else :
        Label(main_window, fg="red", text="1-500 only") .grid(column=2, row=3)
        input_check = 1
    if input_check == 0 : append_details()

def append_details():
    global total_entries, hire_details, entry_customer, entry_receipt, entry_item, entry_number_hired
    #retain the info of each new entry - variables must be in order to be under correct headings
    hire_details.append([entry_customer.get(), entry_receipt.get(), entry_item.get(), entry_number_hired.get()])

    #clear the boxes
    entry_customer.delete(0,'end')
    entry_receipt.delete(0,'end')
    entry_item.delete(0,'end')
    entry_number_hired.delete(0,'end')
    total_entries += 1

def delete_row():
    global hire_details, total_entries, delete_item, name_count
    try:
        del hire_details[int(delete_item.get())]
        total_entries = total_entries - 1
        Label(main_window, text="                  ").grid(column=4, row=3)

    except IndexError:
        Label(main_window, fg="red", text="Invalid Row Number").grid(column=4, row=3)
    except ValueError:
        Label(main_window, fg="red", text="No text or blank").grid(column=4, row=3)  

    #clear the item displayed
    Label(main_window, text="       ").grid(column=0,row=name_count+5) 
    Label(main_window, text="       ").grid(column=1,row=name_count+5)
    Label(main_window, text="       ").grid(column=2,row=name_count+5)
    Label(main_window, text="       ").grid(column=3,row=name_count+5)
    Label(main_window, text="       ").grid(column=4,row=name_count+5)
    #print all the items in the list
    print_hire_details()


def setup_buttons():
    global entry_customer, entry_receipt, entry_item, entry_number_hired, total_entries, delete_item

    #all buttons used in the program - to the right of the entry boxes
    #Append Details, Print Details, Quit buttons are on the same row
    #Delete Row button is in the same column as quit
    Button(main_window, text="Quit", command=quit).grid(column=5, row=0)
    Button(main_window, text="Append Details", command=check_inputs).grid(column=3, row=0)
    Button(main_window, text="Print Details", command=print_hire_details).grid(column=4, row=0)
    Button(main_window, text="Delete Row", command=delete_row).grid(column=5, row=2)

    #headings for entry boxes - Same column different rows, except for the Row heading                                                                                                                                                 
    Label(main_window, text="Customer Name").grid(column=0, row=0, sticky=W)
    Label(main_window, text="Receipt Number").grid(column=0, row=1, sticky=W)
    Label(main_window, text="Item Hired").grid(column=0, row=2, sticky=W)
    Label(main_window, text="Number Hired").grid(column=0, row=3, sticky=W)
    Label(main_window, text="Row #").grid(column=3, row=2, sticky=W)

    #Empty column 2 for error messages
    Label(main_window, text="           ").grid(column=2, row=0, sticky=W)
    Label(main_window, text="           ").grid(column=2, row=1, sticky=W)
    Label(main_window, text="           ").grid(column=2, row=2, sticky=W)
    Label(main_window, text="           ").grid(column=2, row=3, sticky=W)

    #entry boxes
    entry_customer = Entry(main_window)
    entry_customer.grid(column=1, row=0, padx=10, pady=5)
    entry_receipt = Entry(main_window)
    entry_receipt.grid(column=1, row=1, padx=10, pady=5)
    entry_item = Entry(main_window)
    entry_item.grid(column=1, row=2, padx=10, pady=5)
    entry_number_hired = Entry(main_window)
    entry_number_hired.grid(column=1, row=3, padx=10, pady=5)

    #delete entry boxes
    delete_item = Entry(main_window)
    delete_item.grid(column=4, row=2, padx=10, pady=5)
    

#run the program
def main():
    global main_window, total_entries, hire_details
    total_entries = 0
    hire_details = [] #empty list for program to add details from each entry
    main_window = Tk()
    setup_buttons()
    main_window.mainloop()

main()


