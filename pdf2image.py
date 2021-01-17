from pdf2image import convert_from_path, convert_from_bytes
from PIL import Image 
from pdf2image.exceptions import (
    PDFInfoNotInstalledError,
    PDFPageCountError,
    PDFSyntaxError
)
import sys

args = sys.argv

if len(args) != 3:
    print("Specify inputFile and outputDir.")
    exit(1)

inputFile = args[1]
outputFolder = args[2]

print("Reading from "+inputFile)

images_from_path = convert_from_path(inputFile, output_folder=outputFolder)
print("found "+str(len(images_from_path))+" pages.")
print("saving images to "+outputFolder)