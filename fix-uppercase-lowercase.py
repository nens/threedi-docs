from pathlib import Path

import re
import sys

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
    did_something = False
    images = IMAGE_DIR.glob("*.*")
    for image in images:
        lowercase_name = str(image).lower()
        if lowercase_name != str(image):
            did_something = True
            print("Renaming %s into %s" % (image, lowercase_name))
            image.replace(lowercase_name)

    if not did_something:
        print("No uppercase image files found. All is fine.")
    return did_something


def fix_image_links():
    """Check and fix image links in the documentation."""
    did_something = False
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
            did_something = True
            print("Fixing document %s" % doc)
            for old, new in to_replace.items():
                print("    Changing %s into %s" % (old, new))
                contents = contents.replace(old, new)
            doc.write_text(contents)

    if not did_something:
        print("No uppercase image links found in the documentation. All is fine.")
    return did_something


def main():
    did_something1 = fix_image_files()
    did_something2 = fix_image_links()
    if did_something1 or did_something2:
        # Exit with an error code.
        sys.exit(1)


if __name__ == "__main__":
    main()
