import tkinter as tk
from tkinter import scrolledtext, messagebox, font
import requests


# Function to send the HTTP request
def send_request():
    url = url_entry.get()
    method = method_var.get()
    headers = parse_headers(headers_text.get("1.0", tk.END))
    body = body_text.get("1.0", tk.END)

    try:
        # Make the request based on the chosen method
        if method == "GET":
            response = requests.get(url, headers=headers)
        elif method == "POST":
            response = requests.post(url, headers=headers, data=body)
        elif method == "PUT":
            response = requests.put(url, headers=headers, data=body)
        elif method == "DELETE":
            response = requests.delete(url, headers=headers)
        else:
            messagebox.showerror("Error", "Unsupported HTTP method")
            return

        # Display the response
        response_text.delete("1.0", tk.END)
        response_text.insert(tk.END, f"Status Code: {response.status_code}\n\n")
        response_text.insert(tk.END, response.text)

    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")


# Helper function to parse headers from text input
def parse_headers(headers_str):
    headers = {}
    for line in headers_str.strip().split("\n"):
        if ": " in line:
            key, value = line.split(": ", 1)
            headers[key] = value
    return headers


# Set up the main window with a modern look
root = tk.Tk()
root.title("ReqQuest – Your HTTP Companion")
root.geometry("650x800")
root.configure(bg="#2C2F33")  # Dark gray background

# Custom fonts and colors
header_font = font.Font(family="Helvetica", size=14, weight="bold")
label_font = font.Font(family="Helvetica", size=11)
entry_bg = "#23272A"  # Slightly lighter dark gray for entries
entry_fg = "#FFFFFF"  # White text
button_bg = "#7289DA"  # Blue button
button_fg = "#FFFFFF"  # White button text
text_bg = "#1E2124"  # Even darker for response background

# URL entry
tk.Label(root, text="URL:", font=label_font, fg=entry_fg, bg=root["bg"]).pack(
    anchor="w", padx=10, pady=(10, 0)
)
url_entry = tk.Entry(
    root, width=80, bg=entry_bg, fg=entry_fg, insertbackground=entry_fg
)
url_entry.pack(fill="x", padx=10, pady=5)

# HTTP Method Selection
tk.Label(root, text="HTTP Method:", font=label_font, fg=entry_fg, bg=root["bg"]).pack(
    anchor="w", padx=10, pady=(10, 0)
)
method_var = tk.StringVar(value="GET")
method_menu = tk.OptionMenu(root, method_var, "GET", "POST", "PUT", "DELETE")
method_menu.config(
    bg=entry_bg, fg=entry_fg, font=label_font, highlightbackground=entry_bg
)
method_menu["menu"].config(bg=entry_bg, fg=entry_fg)
method_menu.pack(fill="x", padx=10, pady=5)

# Headers entry
tk.Label(
    root,
    text="Headers (Key: Value per line):",
    font=label_font,
    fg=entry_fg,
    bg=root["bg"],
).pack(anchor="w", padx=10, pady=(10, 0))
headers_text = scrolledtext.ScrolledText(
    root, width=80, height=5, bg=entry_bg, fg=entry_fg, insertbackground=entry_fg
)
headers_text.pack(fill="x", padx=10, pady=5)

# Body entry (for POST/PUT requests)
tk.Label(
    root, text="Body (for POST/PUT):", font=label_font, fg=entry_fg, bg=root["bg"]
).pack(anchor="w", padx=10, pady=(10, 0))
body_text = scrolledtext.ScrolledText(
    root, width=80, height=10, bg=entry_bg, fg=entry_fg, insertbackground=entry_fg
)
body_text.pack(fill="x", padx=10, pady=5)

# Send button with styling
send_button = tk.Button(
    root,
    text="Send Request",
    command=send_request,
    font=header_font,
    bg=button_bg,
    fg=button_fg,
    activebackground="#5B6EAE",
)
send_button.pack(pady=20)

# Response display area
tk.Label(root, text="Response:", font=label_font, fg=entry_fg, bg=root["bg"]).pack(
    anchor="w", padx=10, pady=(10, 0)
)
response_text = scrolledtext.ScrolledText(
    root, width=80, height=20, bg=text_bg, fg=entry_fg, insertbackground=entry_fg
)
response_text.pack(fill="x", padx=10, pady=5)

# Start the main loop
root.mainloop()
