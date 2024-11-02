import tkinter as tk
from tkinter import scrolledtext, messagebox
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

# Create the main window
root = tk.Tk()
root.title("HTTP Request Sender")
root.geometry("600x700")

# URL entry
tk.Label(root, text="URL:").pack(anchor="w")
url_entry = tk.Entry(root, width=80)
url_entry.pack(fill="x", padx=10, pady=5)

# Method selection
tk.Label(root, text="HTTP Method:").pack(anchor="w")
method_var = tk.StringVar(value="GET")
method_menu = tk.OptionMenu(root, method_var, "GET", "POST", "PUT", "DELETE")
method_menu.pack(fill="x", padx=10, pady=5)

# Headers entry
tk.Label(root, text="Headers (Key: Value per line):").pack(anchor="w")
headers_text = scrolledtext.ScrolledText(root, width=80, height=5)
headers_text.pack(fill="x", padx=10, pady=5)

# Body entry (for POST/PUT requests)
tk.Label(root, text="Body (for POST/PUT):").pack(anchor="w")
body_text = scrolledtext.ScrolledText(root, width=80, height=10)
body_text.pack(fill="x", padx=10, pady=5)

# Send button
send_button = tk.Button(root, text="Send Request", command=send_request)
send_button.pack(pady=10)

# Response display
tk.Label(root, text="Response:").pack(anchor="w")
response_text = scrolledtext.ScrolledText(root, width=80, height=20)
response_text.pack(fill="x", padx=10, pady=5)

# Run the main loop
root.mainloop()
