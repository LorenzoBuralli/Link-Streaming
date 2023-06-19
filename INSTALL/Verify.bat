@echo off

echo Verifica versione Python
python --version

echo Verifica versione PyWin32
pip show pywin32

echo.
echo Verifica versione Selenium
pip show selenium

pause
