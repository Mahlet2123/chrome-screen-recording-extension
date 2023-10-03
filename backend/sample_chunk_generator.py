import os

# Define the file path and name
file_path = "sample_video_chunk.bin"

# Define the size of the binary data chunk (in bytes)
chunk_size = 1024  # You can adjust this as needed

# Generate random binary data
random_data = os.urandom(chunk_size)

# Write the data to the binary file
with open(file_path, "wb") as binary_file:
    binary_file.write(random_data)

print(f"Sample binary data saved to {file_path}")
