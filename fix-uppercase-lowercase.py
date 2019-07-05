from pathlib import Path


DOC_DIR = Path(__file__).parent / "source"
IMG_DIR = DOC_DIR / "image"


def main():
    images = IMG_DIR.glob("*.*")
    for image in images:
        lowercase_name = str(image).lower()
        if lowercase_name != str(image):
            print("Renaming %s into %s" % (image, lowercase_name))
            image.replace(lowercase_name)


if __name__ == "__main__":
    main()
