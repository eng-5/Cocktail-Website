import os

os.chdir('C:/Users/nk/.gemini/antigravity/scratch/drink-cocktail-menu')

# Patch menu.html
with open('menu.html', 'r', encoding='utf-8') as f:
    menu = f.read()
menu = menu.replace('href="#">Menu</a>', 'href="menu.html">Menu</a>')
menu = menu.replace('href="#">Reservations</a>', 'href="events.html">Reservations</a>')
menu = menu.replace('>Drink</h2>', '><a href="index.html" class="text-inherit">Drink</a></h2>')
with open('menu.html', 'w', encoding='utf-8') as f:
    f.write(menu)

# Patch index.html
with open('index.html', 'r', encoding='utf-8') as f:
    index = f.read()
index = index.replace('href="#">Menu</a>', 'href="menu.html">Menu</a>')
index = index.replace('href="#">Explore Full Menu</a>', 'href="menu.html">Explore Full Menu</a>')
index = index.replace('>Drink</h2>', '><a href="index.html" class="text-inherit">Drink</a></h2>')
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(index)

# Patch events.html
with open('events.html', 'r', encoding='utf-8') as f:
    events = f.read()
events = events.replace('href="#">Menu</a>', 'href="menu.html">Menu</a>')
events = events.replace('href="#">Events</a>', 'href="events.html">Events</a>')
events = events.replace('href="#">Reservations</a>', 'href="events.html">Reservations</a>')
events = events.replace('>DRINK</h2>', '><a href="index.html" class="text-inherit">DRINK</a></h2>')
events = events.replace('>Drink</h2>', '><a href="index.html" class="text-inherit">Drink</a></h2>')
with open('events.html', 'w', encoding='utf-8') as f:
    f.write(events)

print("HTML links patched successfully.")
