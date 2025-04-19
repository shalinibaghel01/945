# dramas_html_generator.py

dramas = [
    {"title": "Crash Landing on You", "image": "https://upload.wikimedia.org/wikipedia/en/f/f5/Crash_Landing_on_You_main_poster.jpg"},
    {"title": "Goblin", "image": "https://upload.wikimedia.org/wikipedia/en/f/fc/Guardian_The_Lonely_and_Great_God.jpg"},
    {"title": "Itaewon Class", "image": "https://upload.wikimedia.org/wikipedia/en/9/9c/Itaewon_Class_poster.jpg"},
    {"title": "Vincenzo", "image": "https://upload.wikimedia.org/wikipedia/en/1/17/Vincenzo_2021.jpg"},
    {"title": "True Beauty", "image": "https://upload.wikimedia.org/wikipedia/en/5/53/True_Beauty_%28TV_series%29.jpg"},
]

html_output = ""
for drama in dramas:
    html_output += f'''
    <div class="card">
      <img src="{drama["image"]}" alt="{drama["title"]}">
      <h3>{drama["title"]}</h3>
    </div>
    '''

# Save it to a file OR just print to paste manually
with open("drama_cards.html", "w", encoding="utf-8") as f:
    f.write(html_output)

print("✅ HTML generated! Paste it into your index.html where needed.")
