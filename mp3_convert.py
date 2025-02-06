import os
import sys
import subprocess

def run_script(script, *args):
    """Runs a script with arguments."""
    print(f"▶ Running {script}...")
    command = ["python3", script] + list(args)
    subprocess.run(command, check=True)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 mp3_convert.py <book_folder>")
        sys.exit(1)

    folder = sys.argv[1]
    run_script("mp3_to_m4a.py", folder)
    run_script("chapter_file.py", folder)
    run_script("m4a_to_m4b.py", folder)
    run_script("embed_cover.py", os.path.join(folder, folder + ".m4b"), os.path.join(folder, "cover.jpg"))