@echo off

REM Richiesta di conferma per avviare la disinstallazione
set /p choice=Vuoi avviare la disinstallazione? (y/n): 
if /i "%choice%" neq "y" goto end

REM Questo script disinstalla completamente Python 3.11.3, pywin32 e selenium dal sistema

REM Verifica se Python 3.11.3 è installato
python --version 2>nul | findstr /C:"Python 3.11.3" >nul
if %errorlevel% equ 0 (
    REM Python 3.11.3 è installato, procedi con la disinstallazione

    REM Disinstalla pywin32
    python -m pip uninstall -y pywin32 >nul

    REM Disinstalla selenium
    python -m pip uninstall -y selenium >nul

    REM Disinstalla Python 3.11.3 usando il programma di installazione
    python -m ensurepip --upgrade --default-pip >nul
    python -m pip uninstall -y pip >nul
    python -m pip uninstall -y setuptools >nul

    REM Rimuovi le voci del registro di sistema associate a Python
    reg delete HKEY_CURRENT_USER\Software\Python /f >nul
    reg delete HKEY_LOCAL_MACHINE\SOFTWARE\Python /f >nul

    REM Rimuovi la cartella di installazione di Python 3.11.3
    rmdir /s /q C:\Python3113 >nul

    echo Python 3.11.3, pywin32 e selenium sono stati disinstallati correttamente.
) else (
    REM Python 3.11.3 non è installato
    echo Python 3.11.3 non è installato nel sistema.
)

:end
REM Pausa lo script per visualizzare l'output
pause

