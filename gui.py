import customtkinter as ctk
from tkinter import filedialog
import threading
import main
import config  

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

running = False


def start_monitoring():
    global running

    if running:
        return

    running = True
    status_label.configure(text="Status: Running", text_color="green")

    def run():
        main.monitor_directory()

    thread = threading.Thread(target=run)
    thread.daemon = True
    thread.start()


def stop_monitoring():
    global running
    running = False
    main.stop_monitor()
    status_label.configure(text="Status: Stopped", text_color="red")


def browse_folder():
    folder = filedialog.askdirectory()

    if folder:
        # update label
        folder_label.configure(text=f"Selected: {folder}")

        # update backend directory
        config.set_watched_directory(folder)

        # enable start button
        start_btn.configure(state="normal")


# App window
app = ctk.CTk()
app.title("AI Directory Manager")
app.geometry("700x550")

# Title
title = ctk.CTkLabel(app, text="AI Powered Directory Manager", font=("Arial", 20, "bold"))
title.pack(pady=15)

# Folder Section
frame_folder = ctk.CTkFrame(app)
frame_folder.pack(pady=10, padx=20, fill="x")

folder_label = ctk.CTkLabel(
    frame_folder,
    text=f"Default: {config.WATCHED_DIRECTORY}"
)
folder_label.pack(side="left", padx=10)

browse_btn = ctk.CTkButton(frame_folder, text="Browse", command=browse_folder)
browse_btn.pack(side="right", padx=10)

# Status
status_label = ctk.CTkLabel(app, text="Status: Stopped", text_color="red", font=("Arial", 14))
status_label.pack(pady=10)

# Buttons
frame_buttons = ctk.CTkFrame(app)
frame_buttons.pack(pady=10)

start_btn = ctk.CTkButton(
    frame_buttons,
    text="Start Monitoring",
    command=start_monitoring,
    width=180,
    state="disabled"   # disabled until folder selected
)
start_btn.grid(row=0, column=0, padx=10, pady=10)

stop_btn = ctk.CTkButton(
    frame_buttons,
    text="Stop Monitoring",
    command=stop_monitoring,
    width=180,
    fg_color="gray"
)
stop_btn.grid(row=0, column=1, padx=10, pady=10)

# Log Box
log_box = ctk.CTkTextbox(app, width=650, height=300)
log_box.pack(pady=15, padx=20)

try:
    with open("logs/system.log", "r") as f:
        f.seek(0, 2)  # move to end of file
        log_position = f.tell()
except:
    log_position = 0

def update_logs():
    global log_position

    try:
        with open("logs/system.log", "r") as f:
            f.seek(log_position)   # move to last read position
            new_data = f.read()    # read only new logs

            if new_data:
                log_box.insert("end", new_data)
                log_box.see("end")  # auto scroll

                log_position = f.tell()  # update pointer

    except:
        pass

    app.after(2000, update_logs)

update_logs()

app.mainloop()