import webbrowser
from AppOpener import open
from customtkinter import CTk
from customtkinter import CTk, CTkLabel, CTkButton, CTkEntry, CTkComboBox, CTkFrame
from design.py import design

def app_automation():
    user_input = input("What app you want to open (can be more than one must be separated by comma and space) ")
    apps = user_input.split(',')

    def open_app(user_app):
        for app in user_app:
            open(app)

    open_app(apps)


def browser_automation():
    URLS = {
        "Work": ["https://www.fiverr.com/mateo_wes?up_rollout=true", "https://chatgpt.com/", "https://gemini.google.com/app", "https://www.youtube.com/"],
        "Pratice": ["https://www.fiverr.com/mateo_wes?up_rollout=true", "https://chatgpt.com/", "https://gemini.google.com/app", "https://exercism.org/tracks/python", "https://www.codewars.com/dashboard", "https://customtkinter.tomschimansky.com/tutorial/"],
        "Personal": ["https://www.fiverr.com/mateo_wes?up_rollout=true", "https://aniwatchtv.to/home", "https://zty.pe/"]
    }

    def open_tab(urls):
        for url in urls:
            webbrowser.open_new_tab(url)

    print("\nTab List:")

    for key, value in URLS.items():
        print(key)

    urls_name = input("What Would You Do today? ").title()
    urls = URLS[urls_name]
    open_tab(urls)


design()
browser_automation()
app_automation()