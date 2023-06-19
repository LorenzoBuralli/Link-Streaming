import time
import threading
import webbrowser
import win32gui
import win32con
import os

def main():
    # Websites to open
    site_web = [
        "https://www.netflix.com",
        "https://www.primevideo.com",
        "https://www.disneyplus.com",
        "https://www.timvision.it"
    ]

    # Open the websites in separate tabs using the default browser
    for site in site_web:
        webbrowser.open_new_tab(site)

    # Continua l'esecuzione dello script fintanto che la finestra del browser è aperta
    while True:
        try:
            # Verifica lo stato della finestra
            if win32gui.GetWindowText(win32gui.GetForegroundWindow()) == "":
                break  # Esci dal ciclo se la finestra è stata chiusa
        except win32gui.error:
            break  # Esci dal ciclo se la finestra è stata chiusa

    # Chiudi la finestra del browser
    os.system("taskkill /im msedge.exe /f")  # Modifica "msedge.exe" con il processo del tuo browser

if __name__ == "__main__":
    # Hide the console
    hide_console = win32gui.GetForegroundWindow()
    win32gui.ShowWindow(hide_console, win32con.SW_HIDE)

    # Execute the main script
    main()
