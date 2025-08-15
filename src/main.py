import requests
import csv
import os

API_URL = "https://rickandmortyapi.com/api/character"
OUTPUT_FILE = os.path.join("data", "characters.csv")

def fetch_characters():
    characters = []
    url = API_URL

    while url:
        resp = requests.get(url, timeout=20)
        resp.raise_for_status()
        data = resp.json()

        for char in data["results"]:
            if (
                char.get("species") == "Human"
                and char.get("status") == "Alive"
                and char.get("origin", {}).get("name", "").startswith("Earth")
            ):
                characters.append({
                    "Name": char.get("name", ""),
                    "Location": char.get("location", {}).get("name", ""),
                    "Image": char.get("image", "")
                })

        url = data["info"].get("next")

    return characters

def save_to_csv(characters):
    os.makedirs("data", exist_ok=True)
    with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["Name", "Location", "Image"])
        writer.writeheader()
        writer.writerows(characters)

def main():
    print("Fetching data from API...")
    characters = fetch_characters()
    print(f"Found {len(characters)} matching characters.")
    save_to_csv(characters)
    print(f"Data saved to {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
