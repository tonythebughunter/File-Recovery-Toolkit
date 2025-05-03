# File-Recovery-Toolkit
An advanced file recovery tool that extracts and restores lost or deleted files (JPEG, PNG, PDF, TXT, ZIP, and more) from raw disk dumps. Supports automatic file signature detection and recovery across multiple formats. Built for digital forensics and data recovery enthusiasts.
## Features
Recovers various file types including:

JPEG, PNG, GIF, PDF, TXT, ZIP, PY, DOCX, and more.

Works with raw disk dumps or binary files.

Automatically creates a "recovered" folder to store the recovered files.

Supports cross-platform compatibility (Linux, Windows, macOS).

Handles files based on known file signatures.

## Installation
Prerequisites : Python 3.x (make sure it is installed on your system).
    git clone https://github.com/tonythebughunter/File-Recovery-Toolkit
## Naviagte to the directory
    cd File-Recovery-Toolkit
## Usage
Once installed, the tool can be run directly from the command line (Linux, macOS, or Windows).
    python recover_files.py <path_to_your_raw_disk_dump_file>
## Example Usage:
    python recover_files.py my_raw_binary_with_deleted_files.bin
## This command will:

Read the provided binary disk dump file (my_raw_binary_with_deleted_files.bin).

Automatically scan for known file signatures.

Recover all detected files (such as JPEG, PNG, PDF, etc.).

Save the recovered files in a folder named recovered.
