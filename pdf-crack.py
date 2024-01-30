import tkinter as tk
from tkinter import filedialog
import pikepdf
import threading

def crack_pdf_password(file_path, wordlist_path):
    with open(wordlist_path, 'r') as wordlist_file:
        for word in wordlist_file:
            word = word.strip()
            try:
                pdf_file = pikepdf.Pdf.open(file_path, password=word)
                print(f"Password cracked: {word}")
                return word
            except pikepdf._qpdf.PasswordError:
                pass
    print("Password not found in wordlist.")
    return None

def browse_file():
    file_path = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
    file_entry.delete(0, tk.END)
    file_entry.insert(0, file_path)

def browse_wordlist():
    wordlist_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    wordlist_entry.delete(0, tk.END)
    wordlist_entry.insert(0, wordlist_path)

def start_cracking():
    file_path = file_entry.get()
    wordlist_path = wordlist_entry.get()
    if file_path and wordlist_path:
        crack_thread = threading.Thread(target=crack_pdf_password, args=(file_path, wordlist_path))
        crack_thread.start()

root = tk.Tk()
root.title("PDF Password Cracker")

file_label = tk.Label(root, text="PDF File:")
file_label.grid(row=0, column=0, padx=10, pady=10)
file_entry = tk.Entry(root, width=50)
file_entry.grid(row=0, column=1, padx=10, pady=10)
file_button = tk.Button(root, text="Browse...", command=browse_file)
file_button.grid(row=0, column=2, padx=10, pady=10)

wordlist_label = tk.Label(root, text="Wordlist File:")
wordlist_label.grid(row=1, column=0, padx=10, pady=10)
wordlist_entry = tk.Entry(root, width=50)
wordlist_entry.grid(row=1, column=1, padx=10, pady=10)
wordlist_button = tk.Button(root, text="Browse...", command=browse_wordlist)
wordlist_button.grid(row=1, column=2, padx=10, pady=10)

crack_button = tk.Button(root, text="Crack Password", command=start_cracking)
crack_button.grid(row=2, column=1, padx=10, pady=10)

root.mainloop()