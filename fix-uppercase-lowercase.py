from pathlib import Path

import re

DOC_DIR = Path(__file__).parent / "source"
IMAGE_DIR = DOC_DIR / "image"
IMAGE_LINK_REGEX = re.compile(r"""
image/       # image/ prefix
\S+          # some chars/numbers
\.           # a dot
[jpngJPGN]+  # .jpg, .png, .PNG, .JPG
""", re.VERBOSE)


def fix_image_files():
    """Rename any offending file to its lowercase version."""
    nothing_to_be_done = True
    images = IMAGE_DIR.glob("*.*")
    for image in images:
        lowercase_name = str(image).lower()
        if lowercase_name != str(image):
            nothing_to_be_done = False
            print("Renaming %s into %s" % (image, lowercase_name))
            image.replace(lowercase_name)

    if nothing_to_be_done:
        print("No uppercase image files found. All is fine.")


def fix_image_links():
    """Check and fix image links in the documentation."""
    nothing_to_be_done = True
    docs = DOC_DIR.glob("*.rst")
    for doc in docs:
        to_replace = {}  # old: new
        contents = doc.read_text()
        image_links = IMAGE_LINK_REGEX.findall(contents)
        for image_link in image_links:
            lowercase_image_link = image_link.lower()
            if image_link != lowercase_image_link:
                to_replace[image_link] = lowercase_image_link

        if to_replace:
            nothing_to_be_done = False
            print("Fixing document %s" % doc)
            for old, new in to_replace.items():
                print("    Changing %s into %s" % (old, new))
                contents = contents.replace(old, new)
            doc.write_text(contents)

    if nothing_to_be_done:
        print("No uppercase image links found in the documentation. All is fine.")


def main():
    fix_image_files()
    fix_image_links()


if __name__ == "__main__":
    main()
