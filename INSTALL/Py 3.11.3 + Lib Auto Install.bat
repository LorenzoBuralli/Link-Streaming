@echo off

REM Richiesta di conferma per avviare l'installazione
set /p choice=Vuoi avviare l'installazione? (y/n): 
if /i "%choice%" neq "y" goto end

rem Verifica se Python è installato nel sistema
python --version >nul 2>&1
if %errorlevel% equ 0 (
    echo Python è già installato nel sistema.
) else (
    echo Python non è installato nel sistema. Installazione in corso...

    rem Scarica l'installer di Python
    curl -o python-installer.exe https://www.python.org/ftp/python/3.11.3/python-3.11.3-amd64.exe

    rem Esegui l'installer di Python
    python-installer.exe /quiet InstallAllUsers=1 PrependPath=1 Include_test=0

    rem Rimuovi l'installer di Python
    del python-installer.exe

    echo Python è stato installato correttamente.
)

rem Verifica e aggiorna pip
python -m pip --version >nul 2>&1
if %errorlevel% equ 0 (
    echo pip è già installato nel sistema. Verifica dell'aggiornamento...

    rem Aggiorna pip
    python -m pip install --upgrade pip
) else (
    echo pip non è installato nel sistema.
    echo Impossibile verificare o eseguire l'aggiornamento di pip.
)

echo Installazione delle librerie in corso...

REM Install win32gui
pip install pywin32==306

REM Install selenium
pip install selenium==4.9.1

echo Installazione completata.

:end
pause
