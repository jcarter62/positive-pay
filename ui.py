import os.path
import sys
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter import messagebox
from reg import REG
from process import PROCESS

root = tk.Tk()
root.title('Positive Pay - File Converter')

try:
    ico_path = os.path.dirname(sys.argv[0])
    ico_path = ico_path + os.path.sep + 'positive-pay-color.ico'
    root.iconbitmap(ico_path)
except:
    pass

root.resizable(True, True)
root.geometry('575x250')

inp_file_name = ''
out_file_name = ''
account_no = ''


def row_y(row):
    return ((row - 1) * 33) + 10


def select_input_file():
    global input_file
    global inp_file_name
    key = 'initial_directory'
    result = ''
    filetypes = (
        ('text files', '*.ext'),
        ('All files', '*.*')
    )

    r = REG()
    initial_directory = r.load_str(key=key).strip()

    filename = fd.askopenfilename(title='File', initialdir=initial_directory, filetypes=filetypes)
    input_file.set(value=filename)

    if len(filename) > 0:
        initial_directory = os.path.dirname(filename)
        r.save_str(key=key, value=initial_directory)

    inp_file_name = filename


def select_output_file():
    global output_file
    global out_file_name
    key = 'output_file'
    filetypes = (('text files', '*.csv'), ('All files', '*.*'))
    r = REG()
    initial_directory = r.load_str(key=key).strip()

    filename = fd.asksaveasfilename(title='Destination File', initialdir=initial_directory, filetypes=filetypes)
    output_file.set(value=filename)

    if len(filename) > 0:
        initial_directory = os.path.dirname(filename)
        r.save_str(key=key, value=initial_directory)

    out_file_name = filename


def account_validate():
    global account_no
    account_no = account_no_inp.get()
    return True


def process_file():
    global inp_file_name
    global out_file_name
    global account_no

    save_inputs()

    PROCESS(input_file_name=inp_file_name, output_file_name=out_file_name, account=account_no)
    messagebox.showinfo('Process', 'Process completed.')
    return


def save_inputs():
    global inp_file_name
    global out_file_name
    global account_no

    r = REG()
    r.save_str(key='Input_File_Name', value=inp_file_name)
    r.save_str(key='Output_File_Name', value=out_file_name)
    r.save_str(key='account_no', value=account_no)
    return


def load_inputs():
    global inp_file_name
    global out_file_name
    global account_no

    r = REG()
    inp_file_name = r.load_str(key='Input_File_Name')
    out_file_name = r.load_str(key='Output_File_Name')
    account_no = r.load_str(key='account_no')
    return


load_inputs()

lbl_title = tk.Label(root, text='Positive Pay - File Converter')
lbl_title.place(x=10, y=row_y(1))

# Input File
lbl_input_file = tk.Label(root, text='Input File:')
lbl_input_file.place(x=10, y=row_y(2))

input_file = StringVar()
input_file.set(value=inp_file_name)
inp_entry = tk.Entry(root, textvariable=input_file)
inp_entry.place(x=70, y=row_y(2), width=350)

inp_button = ttk.Button(root, text='browse', command=select_input_file)
inp_button.place(x=470, y=row_y(2), height=22)

# Output File
lbl_output_file = tk.Label(root, text='Output File:')
lbl_output_file.place(x=10, y=row_y(3))

output_file = StringVar()
output_file.set(value=out_file_name)
out_entry = tk.Entry(root, textvariable=output_file)
out_entry.place(x=90, y=row_y(3), width=330)

out_button = ttk.Button(root, text='browse', command=select_output_file)
out_button.place(x=470, y=row_y(3), height=22)

# Account
lbl_account = tk.Label(root, text='Account No:')
lbl_account.place(x=10, y=row_y(4))

account_no_inp = StringVar()
account_no_inp.set(value=account_no)
account_no_entry = tk.Entry(root, textvariable=account_no_inp, validate='focusout', validatecommand=account_validate)
account_no_entry.place(x=90, y=row_y(4), width=300)

# Save Button
save_btn = ttk.Button(root, text="Save", command=save_inputs)
save_btn.place(x=10, y=row_y(6), height=22)

# Process Button
process_btn = ttk.Button(root, text="Process", command=process_file)
process_btn.place(x=450, y=row_y(6), height=22)


#
# Setup window resize event, so we can keep buttons near lower edge of
# application window.
#
# ref: https://pythonguides.com/python-tkinter-events/
def root_event(event):
    if str(event.widget) == '.':
        # Position Process Button
        xval = event.width - (event.width / 20) - process_btn.winfo_width()
        yval = event.height - (event.height / 20) - process_btn.winfo_height()
        process_btn.place(x=xval, y=yval)

        # Position Save Button
        xval = 10
        yval = event.height - (event.height / 20) - save_btn.winfo_height()
        save_btn.place(x=xval, y=yval)


root.bind('<Configure>', root_event)

root.mainloop()
