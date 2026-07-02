from copystatic import copy_fresh_contents
from gencontent import generate_pages_recursive

def main():
    copy_fresh_contents("static", "public")
    generate_pages_recursive("content", "template.html", "public")

main()