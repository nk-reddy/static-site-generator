from markdown_blocks import markdown_to_html_node
import os


def extract_title(markdown):
    lines = markdown.split("\n")
    for line in lines:
        line = line.strip()
        if line.startswith("# "):
            return line[2:]
    raise Exception("no h1 header found")


def generate_page(from_path, template_path, dest_path, basepath):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path) as f:
        user_markdown = f.read()
    with open(template_path) as f:
        user_template = f.read()
    
    user_html = markdown_to_html_node(user_markdown).to_html()
    user_title = extract_title(user_markdown)
    user_template = user_template.replace("{{ Title }}", user_title)
    user_template = user_template.replace("{{ Content }}", user_html)
    user_template = user_template.replace('href="/', f'href="{basepath}')
    user_template = user_template.replace('src="/', f'src="{basepath}')

    dest_dir_path = os.path.dirname(dest_path)
    if dest_dir_path != "" and not os.path.exists(dest_dir_path):
        os.makedirs(dest_dir_path)

    with open(dest_path, "w") as f:
        f.write(user_template)


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    inner_paths = os.listdir(dir_path_content)
    for path in inner_paths:
        combined_path = os.path.join(dir_path_content, path)
        if os.path.isfile(combined_path):
            if path.endswith(".md"):
                destination_path = os.path.join(dest_dir_path, path.replace(".md", ".html"))
                generate_page(combined_path, template_path, destination_path, basepath)
        else:
            destination_path = os.path.join(dest_dir_path, path)
            generate_pages_recursive(combined_path, template_path, destination_path, basepath)


