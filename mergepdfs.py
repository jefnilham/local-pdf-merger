# Import libraries 
from PyPDF2 import PdfFileMerger 
import os 
 
# Declare global vars 
FOLDER = r'<folder path>' 
OUTPUT_FILE_NAME = '<output filename>' 
OUTPUT_FILEPATH = os.path.join(FOLDER, (OUTPUT_FILE_NAME + '.pdf')) 
 
# Get all pdf files in folder 
pdf_files = [] 
for file in os.listdir(FOLDER): 
    if file.endswith(".pdf"): 
        if OUTPUT_FILE_NAME not in file:  
            pdf_files.append(os.path.join(FOLDER, file)) 
         
         
# Start merging files according to list order 
print('Merging files in the following order:') 
print(pdf_files) 
merger = PdfFileMerger(strict=False) 
for pdf in pdf_files: 
    merger.append(pdf) 
 
# Save merged file 
merger.write(OUTPUT_FILEPATH) 
merger.close() 
print('\nOutput file saved as: ', OUTPUT_FILEPATH)
