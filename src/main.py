from copystatic import copy_fresh_contents
from gencontent import generate_pages_recursive
import sys

def main():
    copy_fresh_contents("static", "docs")

    if len(sys.argv) < 2:
        basepath = "/"
    else:
        basepath = sys.argv[1]
    
    generate_pages_recursive("content", "template.html", "docs", basepath)


main()