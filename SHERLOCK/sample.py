import customtkinter as ctk
import requests
from bs4 import BeautifulSoup
import webbrowser
import tkinter as tk


def get_social(username):
    urls = {
    'Facebook': f'https://www.facebook.com/{username}',
    'Twitter': f'https://www.twitter.com/{username}',
    'Instagram': f'https://www.instagram.com/{username}',
    'LinkedIn': f'https://www.linkedin.com/in/{username}',
    'GitHub': f'https://www.github.com/{username}',
    'Pinterest': f'https://www.pinterest.com/{username}',
    'TikTok': f'https://www.tiktok.com/@{username}',
    'Snapchat': f'https://www.snapchat.com/add/{username}',
    'YouTube': f'https://www.youtube.com/{username}',
    'Medium': f'https://www.medium.com/@{username}',
    'Reddit': f'https://www.reddit.com/user/{username}',
    'Tumblr': f'https://{username}.tumblr.com',
    'Flickr': f'https://www.flickr.com/people/{username}',
    'Dribbble': f'https://www.dribbble.com/{username}',
    'Behance': f'https://www.behance.net/{username}',
    'Vimeo': f'https://vimeo.com/{username}',
    'SoundCloud': f'https://soundcloud.com/{username}',
    'DeviantArt': f'https://www.deviantart.com/{username}',
    'WordPress': f'https://{username}.wordpress.com',
    'Blogspot': f'https://{username}.blogspot.com',
    'Quora': f'https://www.quora.com/profile/{username}',
    'Goodreads': f'https://www.goodreads.com/{username}',
    'Patreon': f'https://www.patreon.com/{username}',
    'Twitch': f'https://www.twitch.tv/{username}',
    'Kickstarter': f'https://www.kickstarter.com/profile/{username}',
    'AngelList': f'https://angel.co/{username}',
    'Mixcloud': f'https://www.mixcloud.com/{username}',
    'VK': f'https://vk.com/{username}',
    'Steam': f'https://steamcommunity.com/id/{username}',
    'Discord': f'https://discord.com/users/{username}',
    'Spotify': f'https://open.spotify.com/user/{username}',
    'StackOverflow': f'https://stackoverflow.com/users/{username}',
    'Xing': f'https://www.xing.com/profile/{username}',
    'ResearchGate': f'https://www.researchgate.net/profile/{username}',
    'GitLab': f'https://gitlab.com/{username}',
    'Kaggle': f'https://www.kaggle.com/{username}',
    'CodePen': f'https://codepen.io/{username}',
    'Strava': f'https://www.strava.com/athletes/{username}',
    'TripAdvisor': f'https://www.tripadvisor.com/members/{username}',
    'Weibo': f'https://weibo.com/{username}',
    'Riot Games': f'https://euw.op.gg/summoner/userName={username}',  
    }
    profiles = {}
    for name, url in urls.items():
        try:
            response = requests.get(url)
            response.raise_for_status()
            soup = BeautifulSoup(response.content, 'html.parser')
            if soup.title and 'Page not found' in soup.title.text:
                continue
            profiles[name] = url
        except:
            continue
    return profiles

def search_profiles(event=None):
    username = search_bar.get()
    profiles = get_social(username)
    result_text.delete(1.0, tk.END)
    
    if profiles:
        for name, url in profiles.items():
            tag_name = f"url_{name}"
            result_text.insert(tk.END, f"{name}: ")
            result_text.insert(tk.END, f"{url}\n", (tag_name,))  
        
          
            result_text.tag_bind(tag_name, "<Button-1>", lambda e, u=url: open_url(u))
            result_text.tag_bind(tag_name, "<Enter>", lambda e: result_text.config(cursor="hand2"))
            result_text.tag_bind(tag_name, "<Leave>", lambda e: result_text.config(cursor=""))
    else:
        result_text.insert(tk.END, "No profiles found.")


def open_url(url):
    webbrowser.open(url)

def clear_search():
    search_bar.delete(0, tk.END)
    result_text.delete(1.0, tk.END)

def toggle_mode():
    if root._get_appearance_mode() == "dark":
        ctk.set_appearance_mode("light")
    else:
        ctk.set_appearance_mode("dark")

ctk.set_appearance_mode("system")
ctk.set_default_color_theme("blue")
root = ctk.CTk()
root.title("SHERLOCK GAZE")
root.geometry("400x450")
root.resizable(False,False)


root.grid_rowconfigure(0, weight=0)
root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(0, weight=1)

top_frame = ctk.CTkFrame(root, corner_radius=10)
top_frame.grid(row=0, column=0, sticky="ew", padx=10, pady=10)

top_frame.grid_columnconfigure(0, weight=0)
top_frame.grid_columnconfigure(1, weight=1)
top_frame.grid_columnconfigure(2, weight=0)
top_frame.grid_columnconfigure(3, weight=0)
top_frame.grid_columnconfigure(4, weight=0)
top_frame.grid_columnconfigure(5, weight=0)


photo_icon = ctk.CTkButton(top_frame,  text="SHERLOCK", width=30)
photo_icon.grid(row=0, column=0, padx=5)

search_bar = ctk.CTkEntry(top_frame, width=50)
search_bar.grid(row=0, column=1, padx=5, sticky="ew")

search_icon = ctk.CTkButton(top_frame, text="🔍", width=30, command=search_profiles)
search_icon.grid(row=0, column=2, padx=5)

clear_button = ctk.CTkButton(top_frame, text="Clear", width=35, command=clear_search)
clear_button.grid(row=0, column=3, padx=5)

dark_mode_icon = ctk.CTkButton(top_frame, text="🌙", width=30, command=toggle_mode)
dark_mode_icon.grid(row=0, column=4, padx=5)

light_mode_icon = ctk.CTkButton(top_frame, text="🌞", width=30, command=toggle_mode)
light_mode_icon.grid(row=0, column=5, padx=5)

bottom_frame = ctk.CTkFrame(root, corner_radius=10)
bottom_frame.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)

bottom_frame.grid_rowconfigure(0, weight=1)
bottom_frame.grid_columnconfigure(0, weight=1)

result_text = tk.Text(bottom_frame, wrap="word", bg="#2e2e2e", fg="white", insertbackground="white", highlightthickness=0, borderwidth=0)
result_text.grid(row=0, column=0, sticky="nsew")

result_text.tag_configure("url", foreground="blue", underline=True)

root.bind('<Return>', search_profiles) 


root.mainloop()
