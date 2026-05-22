@echo off
title BusTrack - Flask Backend
color 0A
echo ================================================
echo   BusTrack Backend - Flask API Server
echo   Running on http://localhost:5000
echo ================================================
echo.
cd /d "%~dp0"
call venv\Scripts\activate
echo [OK] Virtual environment activated
echo [OK] Starting Flask server...
echo.
python app.py
pause
