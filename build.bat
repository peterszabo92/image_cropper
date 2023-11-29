@echo off
pushd %~dp0
python check_packages.py
python -m PyInstaller --onefile --noconsole --add-data "image_cropper.ui;." image_cropper.py
PAUSE