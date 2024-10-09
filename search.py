import os
import sys
import glob
import subprocess
from pdfminer.high_level import extract_pages
from pdfminer.layout import LTTextContainer

# Specify the directory containing the PDF files
PDF_DIRECTORY = './pdf-test/'

def search_word_in_pdf(pdf_path, word):
    pages_with_word = []
    for page_num, page_layout in enumerate(extract_pages(pdf_path), start=1):
        page_text = ''
        for element in page_layout:
            if isinstance(element, LTTextContainer):
                page_text += element.get_text()
        if word.lower() in page_text.lower():
            pages_with_word.append(page_num)
    return pages_with_word

def open_pdf_at_page(pdf_file, page):
    command = ['zathura', '-P', str(page), pdf_file]
    subprocess.Popen(
        command,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        stdin=subprocess.DEVNULL
    )

def main():
    # Check if the specified directory exists
    if not os.path.isdir(PDF_DIRECTORY):
        print(f"The directory '{PDF_DIRECTORY}' does not exist.")
        sys.exit(1)

    # Get the list of PDF files in the specified directory
    pdf_files = glob.glob(os.path.join(PDF_DIRECTORY, '*.pdf'))
    if not pdf_files:
        print(f"No PDF files found in the directory '{PDF_DIRECTORY}'.")
        sys.exit(1)

    while True:
        try:
            word = input("Enter the word to search for (or type 'exit' to quit): ").strip()
            if word.lower() == 'exit':
                print("Exiting the script.")
                break
            for pdf_file in pdf_files:
                pages = search_word_in_pdf(pdf_file, word)
                if pages:
                    print(f"Word '{word}' found in {os.path.basename(pdf_file)} on pages {pages}")
                    for page in pages:
                        open_pdf_at_page(pdf_file, page)
                else:
                    print(f"Word '{word}' not found in {os.path.basename(pdf_file)}")
        except KeyboardInterrupt:
            print("\nScript interrupted by user. Exiting.")
            break

if __name__ == "__main__":
    main()
