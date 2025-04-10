@echo off
echo Creating Python virtual environment...
python -m venv venv
echo.
echo Activating virtual environment...
call venv\Scripts\activate.bat
echo.
echo Installing dependencies...
python -m pip install --upgrade pip
pip install -r requirements.txt
pip install -e .
echo.
echo Virtual environment setup complete!
echo.
echo To activate the virtual environment in the future, run:
echo   venv\Scripts\activate.bat
echo.
echo To deactivate the virtual environment, run:
echo   deactivate
echo.