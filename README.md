# PDF Searcher Script

A small script to search through PDFs.

## Features

1. **PDF Viewer**: Uses **Zathura** as the default PDF reader. This can be changed in the script at **line 23**.
2. **Directory Path**: Specify the path to your directory containing PDFs at **line 9**.
3. **Recursive Search**: To make the script search recursively through all folders inside the directory, modify **line 38** as follows:

   ```python
   pdf_files = glob.glob(os.path.join(PDF_DIRECTORY, '**', '*.pdf'), recursive=True)
   ```

## Requirements

- **Python 3.x**
- **pdfminer.six** library
- **A PDF Viewer** (default is Zathura)

## Installation

1. **Clone or Download the Script**:

   Download the `search_pdfs.py` script to your local machine.

2. **Install Dependencies**:

   Install the required Python package using pip:

   ```bash
   pip install pdfminer.six
   ```

3. **Ensure PDF Viewer is Installed**:

   The script uses Zathura by default. Install it using:

   ```bash
   sudo pacman -S zathura  # For Arch Linux
   ```

   If you're using a different distribution or prefer another PDF viewer, adjust the installation command and update the script accordingly.

## Configuration

1. **Set the Directory Path**:

   In the script, find **line 9** and set `PDF_DIRECTORY` to the path of your PDF files:

   ```python
   PDF_DIRECTORY = '/path/to/your/pdf/directory'
   ```

2. **Change PDF Viewer (Optional)**:

   If you wish to use a different PDF viewer, modify **line 23** in the script:

   ```python
   # Replace 'zathura' with your preferred PDF viewer command
   command = ['zathura', '-P', str(page), pdf_file]
   ```

   Adjust the command options as needed for your chosen PDF viewer.

3. **Enable Recursive Search (Optional)**:

   To search through all subdirectories within your PDF directory, change **line 38** to:

   ```python
   pdf_files = glob.glob(os.path.join(PDF_DIRECTORY, '**', '*.pdf'), recursive=True)
   ```

## Usage

1. **Run the Script**:

   Execute the script using Python:

   ```bash
   python search_pdfs.py
   ```

2. **Interactive Search**:

   - **Prompt**: The script will prompt you to enter a word to search for.

     ```
     Enter the word to search for (or type 'exit' to quit):
     ```

   - **Search**: It will search all PDFs in the specified directory for the word.

   - **Results**: For each occurrence, it will display the PDF file name and the pages where the word was found:

     ```
     Word 'example' found in sample.pdf on pages [2, 5]
     ```

   - **Open PDFs**: The script will open the PDFs at the pages where the word was found.

3. **Exit the Script**:

   - Type `exit` or press `Ctrl+C` to terminate the script.

## Notes

- **Case Insensitivity**: The search is case-insensitive.

- **Multiple Occurrences**: If the word appears on multiple pages within a PDF, the script will open the PDF at each page where it appears.

- **PDF Viewer Compatibility**: Ensure your PDF viewer supports opening at a specific page via command-line options.

## Troubleshooting

- **No PDFs Found**: Verify that `PDF_DIRECTORY` is correctly set and contains PDF files.

- **PDF Viewer Not Opening**: Check that the PDF viewer is installed and that the command in the script is correct.

- **Permission Issues**: Ensure you have read permissions for the PDF files and execute permissions for the script.

## License

This script is provided "as is" without any warranty. Feel free to modify and distribute it according to your needs.
