<p align="right">
  <strong>🇬🇧 English</strong> | <a href="README.tr.md">🇹🇷 Türkçe</a>
</p>

# Auto Backup System

A simple and efficient Python-based automation tool that creates time-stamped backups of a source directory.

## Purpose
This project was developed to automate the manual task of backing up important files. It focuses on **automation, logging, and error handling** to ensure data integrity.

##  Features
- **Automated Backup:** Copies entire directories with a single execution.
- **Smart Naming:** Uses `datetime` for unique folder names (e.g., `backup_2026-05-05_01-15`).
- **Activity Logging:** Records every success and failure in `backup_log.txt`.
- **Cross-Platform:** Works on Windows, macOS, and Linux thanks to `os.path.join`.

##  Tech Stack
- **Language:** Python 3.x
- **Libraries:** `shutil`, `os`, `datetime`

