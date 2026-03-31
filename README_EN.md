# dirsort

[한국어](README.md) | **English**

A CLI tool that automatically organizes files by extension.

Only organizes top-level files — subdirectories are left untouched.

Feel free to modify it to suit your needs.

Tidy up your messy directories.

## Categories

| Folder | Extensions |
|--------|-----------|
| `00_pdf` | `.pdf` |
| `01_image` | `.jpg`, `.jpeg`, `.png`, `.gif`, `.bmp`, `.tif`, `.tiff`, `.webp`, `.heic`, `.heif` |
| `02_doc` | `.hwp`, `.hwpx`, `.doc`, `.docx`, `.txt`, `.rtf`, `.odt` |
| `03_excel` | `.xls`, `.xlsx`, `.xlsm`, `.xlsb`, `.csv` |
| `04_ppt` | `.ppt`, `.pptx` |
| `05_video` | `.mp4`, `.avi`, `.mkv`, `.mov`, `.wmv`, `.flv`, `.webm` |
| `06_audio` | `.mp3`, `.wav`, `.flac`, `.aac`, `.ogg`, `.wma`, `.m4a` |
| `07_archive` | `.zip`, `.rar`, `.7z`, `.tar`, `.gz`, `.bz2` |
| `08_ebook` | `.epub`, `.mobi` |
| `09_font` | `.ttf`, `.otf`, `.woff`, `.woff2` |
| `10_code` | `.py`, `.js`, `.ts`, `.java`, `.c`, `.cpp`, `.html`, `.css`, `.json`, `.xml`, `.yaml`, `.yml` |
| `11_executable` | `.exe`, `.dmg`, `.pkg`, `.deb`, `.msi`, `.app` |

## Installation

### Requirements

- Python 3.9 or higher
- pip (Python package manager)

### Install via pip (all platforms)

```bash
pip install git+https://github.com/ydg06081/dirsort.git --break-system-packages
```

After installation, the `dirsort` command is available directly in your terminal.

### OS-specific instructions

<details>
<summary><b>macOS</b></summary>

```bash
# Install Python via Homebrew if not already installed
brew install python

# Install dirsort
pip3 install git+https://github.com/ydg06081/dirsort.git --break-system-packages
```

> If you get `pip3: command not found`, use `python3 -m pip` instead:
> ```bash
> python3 -m pip install git+https://github.com/ydg06081/dirsort.git --break-system-packages
> ```

</details>

<details>
<summary><b>Windows</b></summary>

```powershell
# Install Python from https://www.python.org/downloads/
# Make sure to check "Add Python to PATH" during installation!

# Run in PowerShell or CMD
pip install git+https://github.com/ydg06081/dirsort.git --break-system-packages
```

> If `pip` doesn't work:
> ```powershell
> python -m pip install git+https://github.com/ydg06081/dirsort.git --break-system-packages
> ```

**If you're using WSL (Windows Subsystem for Linux)**

WSL runs as a Linux environment — follow the Linux instructions below.

</details>

<details>
<summary><b>Linux / WSL (Ubuntu/Debian)</b></summary>

```bash
# Install Python and pip
sudo apt update
sudo apt install python3 python3-pip

# Install dirsort
pip3 install git+https://github.com/ydg06081/dirsort.git --break-system-packages
```

</details>

### Update

```bash
pip install --upgrade git+https://github.com/ydg06081/dirsort.git --break-system-packages
```

### Uninstall

```bash
pip uninstall dirsort
```

## Usage

```bash
# Organize the current directory
dirsort

# Organize a specific directory
dirsort ~/Downloads

# Preview changes without moving files
dirsort --dry-run
```
