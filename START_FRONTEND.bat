@echo off
title BusTrack - React Frontend
color 0B
echo ================================================
echo   BusTrack Frontend - React Dev Server
echo   Running on http://localhost:5173
echo ================================================
echo.
cd /d "%~dp0"
echo [OK] Starting React dev server...
echo.
npm run dev
pause
