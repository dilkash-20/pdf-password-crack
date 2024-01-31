import pikepdf
import tkinter as tk
from tkinter import filedialog

def browse_pdf():
    pdf_path = filedialog.askopenfilename()
    pdf_entry.delete(0, tk.END)
    pdf_entry.insert(0, pdf_path)

def browse_wordlist():
    wordlist_path = filedialog.askopenfilename()
    wordlist_entry.delete(0, tk.END)
    wordlist_entry.insert(0, wordlist_path)

def crack_pdf_password():
    pdf_path = pdf_entry.get()
    wordlist_path = wordlist_entry.get()

    with open(wordlist_path, 'r') as wordlist_file:
        for word in wordlist_file:
            word = word.strip()
            try:
                pdf = pikepdf.Pdf.open(pdf_path, password=word)
                success_label.config(text=f"Success! The password is {word}")
                break
            except pikepdf.PasswordError:
                pass

root = tk.Tk()
root.title("PDF Password Cracker")

pdf_label = tk.Label(root, text="PDF file path:")
pdf_label.pack()
pdf_entry = tk.Entry(root, width=50)
pdf_entry.pack()

browse_pdf_button = tk.Button(root, text="Browse", command=browse_pdf)
browse_pdf_button.pack()

wordlist_label = tk.Label(root, text="Wordlist file path:")
wordlist_label.pack()
wordlist_entry = tk.Entry(root, width=50)
wordlist_entry.pack()

browse_wordlist_button = tk.Button(root, text="Browse", command=browse_wordlist)
browse_wordlist_button.pack()

crack_button = tk.Button(root, text="Crack password", command=crack_pdf_password)
crack_button.pack()

success_label = tk.Label(root, text="")
success_label.pack()

root.mainloop()
