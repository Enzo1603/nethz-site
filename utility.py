import os


def template_finder(folder_path) -> set[str]:
    valid_template_names = set()

    files_and_folders = os.listdir(folder_path)
    html_files = filter(lambda x: x.endswith(".html"), files_and_folders)

    for file in html_files:
        file = file.rstrip(".html")
        valid_template_names.add(file)

    return valid_template_names
