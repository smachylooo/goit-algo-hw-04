import shutil
from pathlib import Path
import argparse

def copy_files(source, destination):
    try:
        for item in source.iterdir():
            if item.is_dir():
                copy_files(item, destination)
            else:
                extension = item.suffix[1:] if item.suffix else "unknown"
                target_folder = destination / extension
                target_folder.mkdir(parents=True, exist_ok=True)

                shutil.copy2(item, target_folder / item.name)

    except Exception as e:
        print(f"Error: {e}")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("source")
    parser.add_argument("destination", nargs="?", default="dist")

    args = parser.parse_args()

    source = Path(args.source)
    destination = Path(args.destination)

    destination.mkdir(parents=True, exist_ok=True)

    copy_files(source, destination)

if __name__ == "__main__":
    main()