# PDF Merger Script

This Python script uses PySimpleGUI and PyPDF2 to merge multiple PDF files into a single PDF file.

## Prerequisites

Make sure you have the following libraries installed:

- PySimpleGUI
- PyPDF2

You can install them using the following command:

```bash
pip install PySimpleGUI PyPDF2
```

## Running the Script (GUI)

1. Run the script using the following command:

   ```bash
   ./pdf_merger_gui.py
   ```

2. The script will prompt you to select a folder containing PDF files to merge.

3. Enter the desired filename for the merged PDF file.

4. Click on the "OK" button to start the merging process.

## Running the Script (CLI)

1. The script will use the predefined folder path (`FOLDER`) and output filename (`OUTPUT_FILE_NAME`) to merge PDF files. Ensure to customize these variables in the script according to your requirements.

2. Open a terminal or command prompt.

3. Execute the script using the following command:

   ```bash
   ./mergepdfs.py
   ```

4. The merged PDF file will be saved in the specified folder with the specified filename.

## Important Notes

- The script can only select PDF Files in an selected Folder
- The PDF order will be based on the filename
- The script will not check if the selected folder contains PDF files or not
- The script runs as intended when the selected folder contains other files (e.g. images, text files, etc.) as long as there are PDF files in the folder
- The merged PDF file will be saved in the selected folder with the specified filename
- If the exported PDF file has the same filename as an existing file in the selected folder, nothing will happen
