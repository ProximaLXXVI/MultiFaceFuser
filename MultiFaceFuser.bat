@echo off
cd %FaceFusionInstallationPath%
call venv\Scripts\activate
python face_swapper.py
