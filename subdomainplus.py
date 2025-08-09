import tkinter as tk
from tkinter import scrolledtext, messagebox
import asyncio
import aiohttp
import threading

def append_text(text_widget, text):
    text_widget.after(0, lambda: text_widget.insert(tk.END, text))
    text_widget.after(0, lambda: text_widget.see(tk.END))

async def scan(subdomain, text_widget, done_callback):
    target_input = subdomain.lower() + ".com"
    async with aiohttp.ClientSession() as session:
        with open("subdomainlist.txt", "r") as file:
            for word in file:
                word = word.strip()
                url = f"http://{word}.{target_input}"
                try:
                    async with session.get(url, timeout=3) as resp:
                        if resp.status in [200,201,202,203]:
                            append_text(text_widget, f"(+) Found: {url}\n")
                except:
                    pass
    append_text(text_widget, "\nAlright, here’s what we’ve found\n")
    done_callback()

def start_scan(entry, text_widget, scan_btn, retry_btn):
    subdomain = entry.get().strip()
    if not subdomain:
        append_text(text_widget, "Please enter a subdomain.\n")
        return
    text_widget.delete(1.0, tk.END)
    append_text(text_widget, f"Starting scan for: {subdomain}.com\n")
    scan_btn.config(state=tk.DISABLED)
    retry_btn.config(state=tk.DISABLED)

    def done():
        scan_btn.config(state=tk.NORMAL)
        retry_btn.config(state=tk.NORMAL)
        messagebox.showinfo("Scan Complete", "Alright, here’s what we’ve found")

    threading.Thread(target=lambda: asyncio.run(scan(subdomain, text_widget, done)), daemon=True).start()

root = tk.Tk()
root.title("Subdomain Scanner")

tk.Label(root, text="Enter a subdomain (without .com):").pack(pady=5)
entry = tk.Entry(root, width=40)
entry.pack(pady=5)

frame = tk.Frame(root)
frame.pack(pady=5)

scan_button = tk.Button(frame, text="Start Scan")
scan_button.pack(side=tk.LEFT, padx=5)

retry_button = tk.Button(frame, text="Retry Scan", state=tk.DISABLED)
retry_button.pack(side=tk.LEFT, padx=5)

text_widget = scrolledtext.ScrolledText(root, width=60, height=20)
text_widget.pack(pady=10)

scan_button.config(command=lambda: start_scan(entry, text_widget, scan_button, retry_button))
retry_button.config(command=lambda: start_scan(entry, text_widget, scan_button, retry_button))

root.mainloop()
