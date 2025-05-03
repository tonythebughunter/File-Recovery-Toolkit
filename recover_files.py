import sys
import os

# Define file signatures for various file types
FILE_SIGNATURES = {
    'jpg': {'start': b'\xFF\xD8\xFF', 'end': b'\xFF\xD9'},
    'png': {'start': b'\x89PNG\r\n\x1a\n', 'end': b'IEND\xaeB`\x82'},
    'pdf': {'start': b'%PDF', 'end': b'\r\n%%EOF'},
    'txt': {'start': b'', 'end': b''},  # handled differently
    'gif': {'start': b'GIF87a', 'end': b'GIF89a'},
    'zip': {'start': b'PK\x03\x04', 'end': b'PK\x05\x06'},
    'py': {'start': b'#!', 'end': b''},  # Python script starts with a shebang
    # Add more known types here...
}

CHUNK_LIMIT = 1024 * 1024  # 1MB max for files with no clear end

def recover_files(input_file_path, output_folder):
    # Open the raw binary data
    with open(input_file_path, 'rb') as file:
        data = file.read()

    recovered_count = 0

    # Loop through all file types
    for ext, sig in FILE_SIGNATURES.items():
        start_sig = sig['start']
        end_sig = sig['end']

        pos = 0

        while pos < len(data):
            # Find the start of the file based on signature
            if start_sig:
                start = data.find(start_sig, pos)
                if start == -1:
                    break
            else:
                start = pos  # for files like .txt with no header

            # Find the end of the file based on signature
            if end_sig:
                end = data.find(end_sig, start)
                if end == -1:
                    break
                end += len(end_sig)
                end = min(end + 20, len(data))  # optional padding
            else:
                end = min(start + CHUNK_LIMIT, len(data))

            # Extract the file data
            file_data = data[start:end]

            # Ensure the output folder exists
            if not os.path.exists(output_folder):
                os.makedirs(output_folder)

            # Save the recovered file into the 'recovered' folder
            filename = f"{output_folder}/recovered_{recovered_count}.{ext}"
            with open(filename, 'wb') as out_file:
                out_file.write(file_data)
                print(f"Recovered: {filename}")

            recovered_count += 1
            pos = end

    print(f"\nTotal files recovered: {recovered_count}")


if __name__ == "__main__":
    # Check if correct number of arguments are passed
    if len(sys.argv) < 2:
        print("Usage: python recover_files.py <binary_dump_file>")
        sys.exit(1)

    input_file_path = sys.argv[1]

    # Check if the input file exists
    if not os.path.exists(input_file_path):
        print(f"Error: File not found: {input_file_path}")
        sys.exit(1)

    # Define the output folder
    output_folder = "recovered"  # Set a static output folder name

    # Call the recovery function
    recover_files(input_file_path, output_folder)
