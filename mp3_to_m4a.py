import os
import sys
import subprocess

def merge_mp3_to_m4a(folder_path, output_m4a):
    """Merges all MP3 files in the folder into a single M4A file."""
    if os.path.exists(output_m4a):
        print(f"✅ M4A file already exists: {output_m4a}. Skipping merge.")
        return

    mp3_files = sorted([f for f in os.listdir(folder_path) if f.endswith(".mp3")])
    if not mp3_files:
        print(f"❌ No MP3 files found in '{folder_path}'. Exiting.")
        sys.exit(1)

    concat_list_path = os.path.join(folder_path, "concat_list.txt")

    with open(concat_list_path, "w") as f:
        for file in mp3_files:
            f.write(f"file '{file}'\n")

    print("🔄 Merging MP3 files into M4A...")
    command = [
        "ffmpeg", "-f", "concat", "-safe", "0", "-i", concat_list_path,
        "-vn", "-c:a", "aac", "-b:a", "128k", output_m4a
    ]
    subprocess.run(command, check=True)
    os.remove(concat_list_path)

    print(f"✅ Merged M4A created: {output_m4a}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 mp3_to_m4a.py <book_folder>")
        sys.exit(1)

    folder = sys.argv[1]
    merge_mp3_to_m4a(folder, os.path.join(folder, os.path.basename(folder) + ".m4a"))