import urllib.request
import os

os.makedirs('C:/Users/nk/.gemini/antigravity/scratch/drink-cocktail-menu', exist_ok=True)
os.chdir('C:/Users/nk/.gemini/antigravity/scratch/drink-cocktail-menu')

files = {
    'menu.html': 'https://contribution.usercontent.google.com/download?c=CgthaWRhX2NvZGVmeBJ8Eh1hcHBfY29tcGFuaW9uX2dlbmVyYXRlZF9maWxlcxpbCiVodG1sXzZmNjkxMDA5ZDlkMzQ4MzE4NWM3MDg5ZmYxN2E0MTdhEgsSBxDK_s2MlxgYAZIBJAoKcHJvamVjdF9pZBIWQhQxNjI0ODg4MDA0NjU2OTAyODcxNQ&filename=&opi=89354086',
    'index.html': 'https://contribution.usercontent.google.com/download?c=CgthaWRhX2NvZGVmeBJ8Eh1hcHBfY29tcGFuaW9uX2dlbmVyYXRlZF9maWxlcxpbCiVodG1sX2Y3MTk3MTRiMGY3MjRkMTU5ZWExMjlmMzcxNWQzYWE5EgsSBxDK_s2MlxgYAZIBJAoKcHJvamVjdF9pZBIWQhQxNjI0ODg4MDA0NjU2OTAyODcxNQ&filename=&opi=89354086',
    'events.html': 'https://contribution.usercontent.google.com/download?c=CgthaWRhX2NvZGVmeBJ8Eh1hcHBfY29tcGFuaW9uX2dlbmVyYXRlZF9maWxlcxpbCiVodG1sX2M2NGRkOTgwY2Y1OTQ0NjNhOTJlZjEzN2NhMDkzMWU3EgsSBxDK_s2MlxgYAZIBJAoKcHJvamVjdF9pZBIWQhQxNjI0ODg4MDA0NjU2OTAyODcxNQ&filename=&opi=89354086'
}

for name, url in files.items():
    print(f"Downloading {name}...")
    urllib.request.urlretrieve(url, name)
    print(f"Saved {name}")

print("Done downloading screens.")
