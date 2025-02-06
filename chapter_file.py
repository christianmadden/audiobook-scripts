import os
import sys
import subprocess

def get_audio_duration(file_path):
    result = subprocess.run(
        ["ffprobe", "-i", file_path, "-show_entries", "format=duration", "-v", "quiet", "-of", "csv=p=0"],
        capture_output=True, text=True, check=True
    )
    return float(result.stdout.strip())

def generate_chapter_file(folder_path, output_m4a):
    """Creates chapters.txt based on MP3 files and durations."""
    chapter_file_path = os.path.join(folder_path, "chapters.txt")
    if os.path.exists(chapter_file_path):
        print(f"✅ Chapters file already exists: {chapter_file_path}. Skipping.")
        return

    total_seconds = 0
    mp3_files = sorted([f for f in os.listdir(folder_path) if f.endswith(".mp3")])

    with open(chapter_file_path, "w") as f:
        for idx, file in enumerate(mp3_files, start=1):
            file_path = os.path.join(folder_path, file)
            hours, remainder = divmod(int(total_seconds), 3600)
            minutes, seconds = divmod(remainder, 60)
            f.write(f"{hours:02}:{minutes:02}:{seconds:02} Chapter {idx}\n")
            total_seconds += get_audio_duration(file_path)

    print(f"✅ Chapters file created: {chapter_file_path}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 chapter_file.py <book_folder>")
        sys.exit(1)

    generate_chapter_file(sys.argv[1], os.path.join(sys.argv[1], os.path.basename(sys.argv[1]) + ".m4a"))