# dirsort

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

## 사용법

```bash
# 현재 디렉토리 정리
dirsort

# 특정 디렉토리 정리
dirsort ~/Downloads

# 미리보기 (실제 이동 없음)
dirsort --dry-run
```

## 설치

```bash
# alias 등록 (~/.zshrc 등)
alias dirsort='python3 /path/to/organize_docs.py'
```
