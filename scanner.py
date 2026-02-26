import hashlib
import os

# Load virus database
def load_virus_hashes():
    with open("virus_db.txt", "r") as f:
        return [line.strip() for line in f]

# Generate file hash
def get_file_hash(filepath):
    hasher = hashlib.md5()
    with open(filepath, "rb") as file:
        buf = file.read()
        hasher.update(buf)
    return hasher.hexdigest()

# Scan folder
def scan_folder(folder):
    virus_hashes = load_virus_hashes()
    
    for root, dirs, files in os.walk(folder):
        for file in files:
            path = os.path.join(root, file)
            file_hash = get_file_hash(path)

            print(f"Scanning: {file}")
            
            if file_hash in virus_hashes:
                print("⚠️ MALWARE DETECTED!")
            else:
                print("✅ Safe")

# Run scan
scan_folder("test_files")