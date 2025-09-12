import os

def save_translation(text: str, filename: str):
    folder = "translations"
    os.makedirs(folder, exist_ok=True)
    filepath = os.path.join(folder, filename)

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(text)
    return filepath
