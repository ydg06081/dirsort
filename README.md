# dirsort

**한국어** | [English](README_EN.md)

디렉토리 내 파일을 확장자별로 자동 분류하는 CLI 도구.

최상위 파일만 정리하며, 하위 디렉토리는 건드리지 않습니다.

자신의 상황에 맞게 마음껏 수정해서 사용하세요.

당신의 어지러운 디렉토리를 정리합니다.

## 카테고리

| 폴더 | 확장자 |
|------|--------|
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

## 설치

### 요구사항

- Python 3.9 이상
- pip (Python 패키지 관리자)

### pip으로 설치 (모든 OS 공통)

```bash
pip install git+https://github.com/ydg06081/dirsort.git
```

설치 후 터미널에서 바로 `dirsort` 명령어를 사용할 수 있습니다.

### OS별 상세 안내

<details>
<summary><b>macOS</b></summary>

```bash
# Python이 없다면 Homebrew로 설치
brew install python

# dirsort 설치
pip3 install git+https://github.com/ydg06081/dirsort.git
```

> `pip3: command not found` 오류가 나면 `python3 -m pip` 으로 대체하세요:
> ```bash
> python3 -m pip install git+https://github.com/ydg06081/dirsort.git
> ```

</details>

<details>
<summary><b>Windows</b></summary>

```powershell
# Python이 없다면 https://www.python.org/downloads/ 에서 설치
# 설치 시 "Add Python to PATH" 체크 필수!

# PowerShell 또는 CMD에서 실행
pip install git+https://github.com/ydg06081/dirsort.git
```

> `pip`이 안 되면:
> ```powershell
> python -m pip install git+https://github.com/ydg06081/dirsort.git
> ```

**WSL(Windows Subsystem for Linux) 사용 중이라면**

WSL은 Linux 환경이므로 `externally-managed-environment` 오류가 발생할 수 있습니다. pipx를 사용하세요:

```bash
sudo apt install pipx
pipx install git+https://github.com/ydg06081/dirsort.git
```

</details>

<details>
<summary><b>Linux (Ubuntu/Debian)</b></summary>

```bash
# Python과 pip 설치
sudo apt update
sudo apt install python3 python3-pip

# dirsort 설치
pip3 install git+https://github.com/ydg06081/dirsort.git
```

> `externally-managed-environment` 오류가 나면 pipx를 사용하세요:
> ```bash
> sudo apt install pipx
> pipx install git+https://github.com/ydg06081/dirsort.git
> ```

</details>

### 업데이트

```bash
pip install --upgrade git+https://github.com/ydg06081/dirsort.git
```

### 제거

```bash
pip uninstall dirsort
```

## 사용법

```bash
# 현재 디렉토리 정리
dirsort

# 특정 디렉토리 정리
dirsort ~/Downloads

# 미리보기 (실제 이동 없음)
dirsort --dry-run
```
