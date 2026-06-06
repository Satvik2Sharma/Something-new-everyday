import json
import os
import math

INPUT_FILE = "stage1_metadata.json"
OUTPUT_DIR = "chunks"
CHUNK_SIZE = 60

# Load JSON
with open(INPUT_FILE, "r", encoding="utf-8") as f:
    papers = json.load(f)

# Create output directory
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Split into chunks
total_papers = len(papers)
num_chunks = math.ceil(total_papers / CHUNK_SIZE)

for i in range(num_chunks):
    start = i * CHUNK_SIZE
    end = start + CHUNK_SIZE

    chunk = papers[start:end]

    output_file = os.path.join(
        OUTPUT_DIR,
        f"chunk_{i+1:03d}.json"
    )

    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(chunk, f, indent=2, ensure_ascii=False)

    print(f"Saved {output_file} ({len(chunk)} papers)")

print(f"\nDone!")
print(f"Total papers: {total_papers}")
print(f"Chunks created: {num_chunks}")
