import tkinter as tk
from tkinter import messagebox, ttk
import sqlite3

class SnippetManager:
    def __init__(self, root):
        self.root = root
        self.root.title("Code Snippet Manager")

        self.conn = sqlite3.connect("snippet_manager.db")
        self.cursor = self.conn.cursor()
        self.create_table()

        self.snippets_listbox = tk.Listbox(root, width=80, height=20)
        self.snippets_listbox.pack(pady=10)

        self.load_snippets()

        add_button = tk.Button(root, text="Add Snippet", command=self.add_snippet)
        add_button.pack(side=tk.LEFT, padx=10)

        edit_button = tk.Button(root, text="Edit Snippet", command=self.edit_snippet)
        edit_button.pack(side=tk.LEFT, padx=10)

        delete_button = tk.Button(root, text="Delete Snippet", command=self.delete_snippet)
        delete_button.pack(side=tk.LEFT, padx=10)

        search_label = tk.Label(root, text="Search:")
        search_label.pack(side=tk.LEFT, padx=10)

        self.search_entry = tk.Entry(root, width=30)
        self.search_entry.pack(side=tk.LEFT)

        search_button = tk.Button(root, text="Search", command=self.search_snippets)
        search_button.pack(side=tk.LEFT, padx=10)

    def create_table(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS snippets (
                id INTEGER PRIMARY KEY,
                title TEXT,
                language TEXT,
                category TEXT,
                code TEXT
            )
        """)
        self.conn.commit()

    def load_snippets(self):
        self.snippets_listbox.delete(0, tk.END)
        self.cursor.execute("SELECT * FROM snippets")
        rows = self.cursor.fetchall()
        for row in rows:
            self.snippets_listbox.insert(tk.END, row[1])

    def add_snippet(self):
        
        pass

    def edit_snippet(self):
        
        pass

    def delete_snippet(self):
         
        pass

    def search_snippets(self):
        
        pass

if __name__ == "__main__":
    root = tk.Tk()
    app = SnippetManager(root)
    root.mainloop()
