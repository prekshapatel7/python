'''Create a specific subdirectory and copy one file from another subdirectory
to this newly created subdirectory.'''
import os
import shutil

# Define paths
source_dir = "source_folder"              # Existing subdirectory
target_dir = "destination_folder"         # New subdirectory to be created
file_to_copy = "example.txt"              # Name of file to copy

# Create target directory if it doesn't exist
if not os.path.exists(target_dir):
    os.makedirs(target_dir)
    print(f"Created directory: {target_dir}")

# Full paths
source_path = os.path.join(source_dir, file_to_copy)
destination_path = os.path.join(target_dir, file_to_copy)

# Copy file
if os.path.exists(source_path):
    shutil.copy(source_path, destination_path)
    print(f"Copied '{file_to_copy}' from '{source_dir}' to '{target_dir}'")
else:
    print(f"Source file not found: {source_path}")
