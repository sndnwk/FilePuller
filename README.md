# FilePuller

A lightweight Python utility that moves files from nested subfolders into a single parent directory.

FilePuller makes it easy to organize directories by pulling files out of their subfolders and placing them together in one location, without overwriting files that share the same name.

## Features

- Recursively scans folders and subfolders.
- Moves files into the selected parent directory.
- Automatically renames duplicate filenames to prevent overwriting.
- Displays file progress and errors in a coloured terminal interface.
- Shows a summary of moved, renamed, and failed files.
- Simple command-line interface with no complicated configuration.

## Installation

**Requirements:**
- Python 3.x
- Colorama

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/FilePuller.git
cd FilePuller
```

Install the required dependency:

```bash
pip install colorama
```

## Usage

Run the program:

```bash
python FilePuller.py
```

Enter the path to the folder you want to organize when prompted:

```text
Source Folder: C:\Users\Example\Downloads
```

FilePuller will scan all subfolders and move their files into the selected directory.

Enter `Q` at the folder prompt to exit the program.

### Example

**Before:**

```text
Downloads/
├── Folder1/
│   ├── image.png
│   └── document.pdf
├── Folder2/
│   ├── image.png
│   └── video.mp4
└── notes.txt
```

**After:**

```text
Downloads/
├── Folder1/
├── Folder2/
├── image.png
├── image_r1.png
├── document.pdf
├── video.mp4
└── notes.txt
```

Files with identical names are automatically renamed using the `_r1`, `_r2`, etc. suffixes.

### Example Output

```text
----------------------------------------
              FilePuller
----------------------------------------
Pull files from subfolders into one folder.
Enter Q to quit.

Source Folder: C:\Users\Example\Downloads
Folder Found!

Pulling Files From: C:\Users\Example\Downloads
----------------------------------------
[+] image.png
[+] image_r1.png
[+] document.pdf
[+] video.mp4
----------------------------------------
Pulling Complete!

Files Pulled:  4
Files Renamed: 1
Files Failed:  0
----------------------------------------
```

## Important Notes

- Files are **moved, not copied**.
- Original subfolders are not deleted.
- Existing files in the parent directory are preserved.
- The program does not provide an undo function. Back up important files before running it.

## License

FilePuller is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Support

If you find FilePuller useful and would like to support its development, donations are appreciated.

**Bitcoin (BTC):**

```text
bc1qzwsla74pcwrly9yc42n7x7320w2cx5w6y2ua9e
```
