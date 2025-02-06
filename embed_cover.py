import os
import sys
import subprocess

def embed_cover(m4b_file, cover_image):
    """Embeds a cover into an M4B file using MP4Box."""
    if not os.path.exists(m4b_file):
        print(f"❌ M4B file '{m4b_file}' not found. Skipping cover embedding.")
        return

    output_m4b_with_cover = m4b_file.replace(".m4b", "_with_cover.m4b")

    print(f"🔄 Embedding cover: {cover_image} into {m4b_file}...")
    command = ["MP4Box", "-itags", f"cover={cover_image}", "-add", m4b_file, "-new", output_m4b_with_cover]

    try:
        subprocess.run(command, check=True)
        os.rename(output_m4b_with_cover, m4b_file)
        print(f"✅ Cover embedded: {m4b_file}")
    except subprocess.CalledProcessError as e:
        print(f"❌ MP4Box failed. Error:\n{e.stderr}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 embed_cover.py <m4b_file> <cover.jpg/png>")
        sys.exit(1)

    embed_cover(sys.argv[1], sys.argv[2])