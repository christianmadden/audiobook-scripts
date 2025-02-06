import os
import sys
import subprocess

def add_chapters_to_m4b(folder_path, output_m4a, output_m4b, chapter_file):
    """Adds chapters to M4A and converts it to M4B."""
    if os.path.exists(output_m4b):
        print(f"✅ M4B file already exists: {output_m4b}. Skipping conversion.")
        return

    print("🔄 Converting M4A to M4B and adding chapters...")
    command = ["MP4Box", "-add", output_m4a, "-chap", chapter_file, "-new", output_m4b]
    subprocess.run(command, check=True)
    print(f"✅ M4B created: {output_m4b}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 m4a_to_m4b.py <book_folder>")
        sys.exit(1)

    folder = sys.argv[1]
    add_chapters_to_m4b(folder, os.path.join(folder, folder + ".m4a"), os.path.join(folder, folder + ".m4b"), os.path.join(folder, "chapters.txt"))