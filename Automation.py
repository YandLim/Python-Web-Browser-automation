import webbrowser
from customtkinter import CTk, CTkLabel, CTkButton, CTkEntry, CTkComboBox, CTkFrame
from AppOpener import open

# Define URLS globally
URLS = {
    "Work": [
        "https://www.fiverr.com/mateo_wes?up_rollout=true", 
        "https://www.upwork.com/nx/find-work/best-matches",
        "https://github.com/MrAnon89/MrAnon89",
        "https://chatgpt.com/", 
        "https://gemini.google.com/app", 
        "https://www.youtube.com/"
    ],
    "Practice": [
        "https://www.fiverr.com/mateo_wes?up_rollout=true", 
        "https://www.upwork.com/nx/find-work/best-matches",
        "https://chatgpt.com/", 
        "https://gemini.google.com/app", 
        "https://exercism.org/tracks/python", 
        "https://www.codewars.com/dashboard", 
        "https://customtkinter.tomschimansky.com/tutorial/"
    ],
    "Personal": [
        "https://www.fiverr.com/mateo_wes?up_rollout=true", 
        "https://www.upwork.com/nx/find-work/best-matches",
        "https://aniwatchtv.to/home", 
        "https://zty.pe/"
    ]
}

def design():
    # Define colors
    dark_theme = "#282c34"
    light_text = "#ffffff"
    accent_color = "#007bff"  # Optional accent color
    button_bg_color = "#3a3f47"  # Background color for buttons
    border_color = "#007bff"  # Border color for widgets
    border_width = 5  # Border width
    entry_bg_color = "#1e1e1e"  # Background color for entry and dropdown
    button_frame_bg_color = "#2e3440"  # Background color for the frame around buttons
    label_border_color = "#ffffff"  # Border color for the label

    # Create the main window
    app = CTk()
    app.geometry("500x500")
    app.title("AutoApp")

    # App Name with border
    border_frame = CTkFrame(
        master=app,
        width=400,
        height=80,
        corner_radius=10,
        fg_color=dark_theme,  # Background color for border frame
        border_color=label_border_color,
        border_width=3  # Border width around the label
    )
    border_frame.pack(pady=20)
    
    app_name = CTkLabel(
        master=border_frame,
        text="AutoApp",
        font=("Roboto", 50),
        text_color=light_text
    )
    app_name.pack(pady=10)

    # Button Functions
    def open_apps_button_clicked():
        user_input = apps_entry.get()  # Get app names from entry field
        apps = [app.strip() for app in user_input.split(",")]
        for app in apps:
            try:
                open(app)
            except Exception as e:
                status_bar.configure(text=f"Error opening {app}: {e}")

    def open_browsers_button_clicked():
        selected_category = category_dropdown.get()
        urls = URLS.get(selected_category, [])
        if urls:
            open_tab(urls)
        else:
            status_bar.configure(text="Invalid category selected")

    def open_tab(urls):
        for url in urls:
            try:
                webbrowser.open_new_tab(url)
            except Exception as e:
                status_bar.configure(text=f"Error opening {url}: {e}")

    def open_all_button_clicked():
        open_apps_button_clicked()
        open_browsers_button_clicked()

    # Content Area
    content_frame = CTkFrame(
        master=app,
        width=400,
        height=250,
        corner_radius=10,
        fg_color=dark_theme,  # Set the background color of the frame
        border_color=border_color,
        border_width=border_width
    )

    # App Entry Field
    apps_entry = CTkEntry(
        master=content_frame,
        placeholder_text="Enter App Names (separated by commas)",
        width=300,
        height=40,
        corner_radius=10,
        fg_color=entry_bg_color,  # Set background color
        text_color=light_text  # Ensure the text color is white
    )
    apps_entry.pack(pady=20)

    # Category Dropdown Menu
    category_options = list(URLS.keys())
    category_dropdown = CTkComboBox(
        master=content_frame,
        values=category_options,
        width=200,
        height=35,
        corner_radius=10,
        fg_color=entry_bg_color,  # Set background color
        text_color=light_text  # Ensure the text color is white
    )
    category_dropdown.pack(pady=20)

    # Create button frame with background color
    button_frame = CTkFrame(
        master=content_frame,
        width=350,
        height=150,
        corner_radius=10,
        fg_color=button_frame_bg_color,  # Background color for button frame
        border_color=border_color,
        border_width=border_width
    )
    button_frame.pack(pady=10, fill="both")

    # Open Apps Button
    open_apps_button = CTkButton(
        master=button_frame,
        text="Open Apps",
        command=open_apps_button_clicked,
        hover_color=accent_color,
        corner_radius=10,
        width=300,
        height=30
    )
    open_apps_button.pack(pady=10, padx=10, fill="x")

    # Open Browsers Button
    open_browsers_button = CTkButton(
        master=button_frame,
        text="Open Browsers",
        command=open_browsers_button_clicked,
        hover_color=accent_color,
        corner_radius=10,
        width=300,
        height=30
    )
    open_browsers_button.pack(pady=10, padx=10, fill="x")

    # Open All Button
    open_all_button = CTkButton(
        master=button_frame,
        text="Open All",
        command=open_all_button_clicked,
        hover_color=accent_color,
        corner_radius=10,
        width=300,
        height=30
    )
    open_all_button.pack(pady=10, padx=10, fill="x")

    # Status Bar
    status_bar = CTkLabel(
        master=app,
        text="",
        text_color=light_text
    )

    # Layout
    content_frame.pack(pady=20)
    status_bar.pack(pady=10)

    # Styling
    app.configure(fg_color=dark_theme)  # Set background color for the main window
    for widget in content_frame.winfo_children():
        widget.configure(fg_color=dark_theme)  # Apply styling to widgets in content_frame

    return app

# The design function will return the created app window
