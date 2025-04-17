# -*- coding: utf-8 -*-
"""
Created on Wed Apr 16 20:52:49 2025

@author: adrian
"""
import os

def remove_originals_if_downsampled_exists(directory, extension):
    # Make sure extension starts with a dot
    if not extension.startswith("."):
        extension = "." + extension

    # Get all video files with the given extension
    video_files = [f for f in os.listdir(directory) if f.endswith(extension)]
    to_delete = []

    for filename in video_files:
        if "downsampled" not in filename:
            # Construct expected downsampled name
            base = filename[:-len(extension)]
            expected_downsampled = f"{base}downsampled{extension}"
            if expected_downsampled in video_files:
                original_path = os.path.join(directory, filename)
                to_delete.append(original_path)

    # Delete the original files
    for file_path in to_delete:
        print(f"Deleting original file: {file_path}")
        os.remove(file_path)  # ← UNCOMMENT to actually delete


# Example usage
#Adapt this with path of videos to delete:
directory_path = "/home/yourusername/Documents"

video_extension = ".avi"  # Change this to ".mp4", ".mov", etc. if needed

remove_originals_if_downsampled_exists(directory_path, extension=video_extension)
