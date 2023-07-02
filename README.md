# PDF to MP3 Converter

This is a Python program that converts PDF files into audio MP3 files. It uses the pdfplumber library to extract text from the PDF and the gtts library to generate the audio file.

## Prerequisites

Before using this program, make sure you have the following dependencies installed:
pdfplumber
gtts
You can install these dependencies using pip:
```
pip install pdfplumber gtts
```
## Usage
When you run the program, it will prompt you for the PDF file path, the language for the audio (English or Russian), and the save path for the MP3 file. Once you provide the necessary inputs, the program will convert the PDF to an audio MP3 file and save it at the specified location.

Please note that this program assumes the PDF file contains readable text. It may not work correctly if the PDF contains scanned images or non-text content.
## Limitations
 - This program may not work correctly if the PDF file contains scanned images or non-text content.
 - The accuracy of the text extraction depends on the quality and formatting of the PDF.
 - The program currently supports English and Russian languages only.
