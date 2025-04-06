import tkinter as tk
from tkinter import ttk, messagebox
import requests

API_KEY = "enter your API_KEY here"
URL = "https://newsapi.org/v2/top-headlines"

def fetch_news(category):
    params = {
        'country': 'us',
        'category': category,
        'apiKey': API_KEY,
        'pageSize': 5
    }

    response = requests.get(URL, params=params)
    
    if response.status_code == 200:
        data = response.json()
        if data['status'] == 'ok' and len(data['articles']) > 0:
            news_output.delete("1.0", tk.END)  # Clear previous news
            for ind, article in enumerate(data['articles'], start=1):
                news_output.insert(tk.END, f"{ind}. {article['title']}\n")
                news_output.insert(tk.END, f"   Source: {article['source']['name']}\n")
                news_output.insert(tk.END, f"   {article['description']}\n\n")
        else:
            messagebox.showinfo("No News", "No articles found for this category.")
    else:
        messagebox.showerror("Error", f"Failed to fetch data. Status code: {response.status_code}")

# GUI setup
root = tk.Tk()
root.title("News App")
root.geometry("600x500")

label = tk.Label(root, text="Select News Category", font=("Arial", 14))
label.pack(pady=10)

# Category buttons
categories = {
    "Technology": "technology",
    "Business": "business",
    "General": "general",
    "Sports": "sports"
}

for text, category in categories.items():
    btn = ttk.Button(root, text=text, command=lambda c=category: fetch_news(c))
    btn.pack(pady=5)

# Text area for news
news_output = tk.Text(root, wrap=tk.WORD, height=20)
news_output.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

root.mainloop()
