@echo off
echo Starting Logo Turtle Build Process...

REM Variables
SET VENV_DIR=venv_build
SET PYTHON_EXE=%VENV_DIR%\Scripts\python.exe
SET PIP_EXE=%VENV_DIR%\Scripts\pip.exe
SET PYINSTALLER_EXE=%VENV_DIR%\Scripts\pyinstaller.exe
SET MAIN_SCRIPT=logo_turtle\main.py
SET APP_NAME=LogoTurtle
REM ICON_PATH=assets\icon.ico # Optional: Uncomment and set path if you have an icon

echo.
echo [1/4] Checking for Python...
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Python is not found in PATH. Please install Python and ensure it's in PATH.
    goto :eof
)
python --version

echo.
echo [2/4] Creating/Updating Virtual Environment (%VENV_DIR%)...
if not exist %VENV_DIR% (
    python -m venv %VENV_DIR%
    if %errorlevel% neq 0 (
        echo Failed to create virtual environment.
        goto :eof
    )
    echo Virtual environment created.
) else (
    echo Virtual environment already exists. Skipping creation.
)

echo.
echo [3/4] Installing Dependencies...
%PIP_EXE% install -r requirements.txt
if %errorlevel% neq 0 (
    echo Failed to install requirements from requirements.txt.
    goto :eof
)
%PIP_EXE% install -r requirements-dev.txt
if %errorlevel% neq 0 (
    echo Failed to install requirements from requirements-dev.txt.
    goto :eof
)
echo Dependencies installed.

echo.
echo [4/4] Running PyInstaller...
REM PyInstaller options:
REM   --name: Name of the application
REM   --onedir: Create a one-folder bundle (vs --onefile)
REM   --windowed: Prevent console window for GUI apps
REM   --clean: Clean PyInstaller cache and remove temporary files before building
REM   --noconfirm: Replace output directory without asking for confirmation
REM   Optional: --icon=%ICON_PATH% (if you have an icon)

%PYINSTALLER_EXE% --name %APP_NAME% --onedir --windowed --clean --noconfirm %MAIN_SCRIPT%
REM For a single file executable (can be slower to start, might have issues with some libs):
REM %PYINSTALLER_EXE% --name %APP_NAME% --onefile --windowed --clean --noconfirm -m logo_turtle.main

if %errorlevel% neq 0 (
    echo PyInstaller failed to build the executable.
    goto :eof
)

echo.
echo Build successful!
echo Executable and associated files are in the 'dist\%APP_NAME%' folder.
echo You can run the application by executing 'dist\%APP_NAME%\%APP_NAME%.exe'.

goto :eof

:error
echo An error occurred. Build failed.
pause

:eof
echo.
