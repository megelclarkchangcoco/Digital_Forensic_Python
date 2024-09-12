import os
import hashlib
def calculate_hash(file_path):
    sha256_hash = hashlib.sha256()
    with open(file_path, "rb") as f:
     # Read and update hash in chunks
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()

# Example usage
file_path = 'File Analysis Script 3.2/POLISON-MANGONA-ACT1.docx'
file_metadata = os.stat(file_path)
print(f"File: {file_path}")
print(f"Created: {file_metadata.st_ctime}")
print(f"Last Modified: {file_metadata.st_mtime}")
print(f"SHA-256 Hash: {calculate_hash(file_path)}")