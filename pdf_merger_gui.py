# -*- coding: utf-8 -*-
"""
Created on Sat Dec 11 20:02:37 2021

@author: jefni
"""
import PySimpleGUI as sg # adapted from https://pysimplegui.readthedocs.io/en/latest/
from PyPDF2 import PdfFileMerger 
import os 

sg.theme('Dark Blue 2')   # Add a touch of color
# All the stuff inside your window.


# Create the Window
window = sg.Window('PDF MERGER')

#process "events" and get the "values" of the inputs
event, values = sg.Window('PDF MERGER', 
                          [[sg.Text('Select folder to merge all pdf files within:')], 
                           [sg.Input(), sg.FolderBrowse()], 
                           [sg.Text('Filename of the merged pdf file:')],
                           [sg.Input()],
                           [sg.OK(), sg.Cancel()] ]).read(close=True)

print('You entered', values[0], values[1])

# Declare global vars 
FOLDER = values[0]
OUTPUT_FILE_NAME = values[1]
OUTPUT_FILEPATH = os.path.join(FOLDER, (OUTPUT_FILE_NAME + '.pdf')) 
 
# Get all pdf files in folder 
pdf_files = [] 
for file in os.listdir(FOLDER): 
    if file.endswith(".pdf"): 
        if OUTPUT_FILE_NAME not in file:  
            pdf_files.append(os.path.join(FOLDER, file)) 
         
         
# Start merging files according to list order 
print('Merging files in the following order:') 
sg.popup_scrolled(pdf_files, title='Confirm file merger?')
print(pdf_files) 
merger = PdfFileMerger(strict=False) 
for pdf in pdf_files: 
    merger.append(pdf) 
 
# Save merged file 
merger.write(OUTPUT_FILEPATH) 
merger.close() 
print('\nOutput file saved as:', OUTPUT_FILEPATH)

sg.Popup('Merged file saved as:', OUTPUT_FILEPATH, title='MERGED!')

