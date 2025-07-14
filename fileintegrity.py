import hashlib
import os

# Function to calculate SHA256 hash of a file
def calculate_hash(file_path):
    sha256_hash = hashlib.sha256()
    try:
        with open(file_path, "rb") as f:
            for byte_block in iter(lambda: f.read(4096), b""):
                sha256_hash.update(byte_block)
        return sha256_hash.hexdigest()
    except FileNotFoundError:
        return None

# Function to check file integrity
def check_integrity(original_hash, file_path):
    current_hash = calculate_hash(file_path)
    if not current_hash:
        print("File not found.")
    elif current_hash == original_hash:
        print("✅ File is intact. No changes detected.")
    else:
        print("⚠️ File has been changed!")

# MAIN SCRIPT
if __name__ == "__main__":
    file_path = input("Enter the file path to check integrity: ")
    
    # Initial hash
    original_hash = calculate_hash(file_path)
    if original_hash:
        print(f"Original Hash: {original_hash}")
        
        input("Make a change to the file and press Enter to check again...")

        check_integrity(original_hash, file_path)
    else:
        print("File not found. Please check the path and try again.")
        