"""
Fetches all League of Legends champions and their abilities from Riot's
official Data Dragon API (no API key required) and saves them as a
Python-importable list of dicts (JSON file + optional .py file).

Usage:
    pip install requests
    python get_champions.py
"""

import json
import requests

BASE = "https://ddragon.leagueoflegends.com"


def get_latest_version() -> str:
    versions = requests.get(f"{BASE}/api/versions.json").json()
    return versions[0]


def get_champion_ids(version: str) -> list[str]:
    url = f"{BASE}/cdn/{version}/data/en_US/champion.json"
    data = requests.get(url).json()["data"]
    return list(data.keys())


def get_champion_full(version: str, champ_id: str) -> dict:
    """Full data (incl. all spells/abilities) for one champion."""
    url = f"{BASE}/cdn/{version}/data/en_US/champion/{champ_id}.json"
    data = requests.get(url).json()["data"][champ_id]

    abilities = []
    for key, spell in zip(["Q", "W", "E", "R"], data["spells"]):
        abilities.append(
            {
                "key": key,
                "name": spell["name"],
            }
        )

    return {
        "name": data["name"],
        "abilities": abilities,
    }


def build_champion_list() -> list[dict]:
    version = get_latest_version()
    print(f"Using patch {version}")

    champ_ids = get_champion_ids(version)
    print(f"Found {len(champ_ids)} champions")

    champions = []
    for i, champ_id in enumerate(champ_ids, 1):
        print(f"  [{i}/{len(champ_ids)}] {champ_id}")
        champions.append(get_champion_full(version, champ_id))

    return champions


if __name__ == "__main__":
    champions = build_champion_list()

    # Save as JSON (easiest to re-load later without hitting the API again)
    with open("champions.json", "w", encoding="utf-8") as f:
        json.dump(champions, f, ensure_ascii=False, indent=2)

    print(f"\nSaved {len(champions)} champions to champions.json")
    print("\nExample entry:")
    print(json.dumps(champions[0], indent=2, ensure_ascii=False))