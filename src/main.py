from copystatic import copy_fresh_contents
from gencontent import generate_page

def main():
    copy_fresh_contents("static", "public")
    generate_page("content/index.md", "template.html", "public/index.html")

main()