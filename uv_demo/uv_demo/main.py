"""
A simple demo script that fetches a random fact from an API.
Demonstrates using external dependencies managed by uv.
"""
import requests


def get_random_fact():
    """Fetch a random fact from an API."""
    try:
        response = requests.get("https://uselessfacts.jsph.pl/random.json?language=en")
        response.raise_for_status()
        data = response.json()
        return data.get("text", "No fact found")
    except requests.RequestException as e:
        return f"Error fetching fact: {e}"


def main():
    print("🎲 Random Fact Generator")
    print("-" * 50)
    fact = get_random_fact()
    print(f"\n{fact}\n")


if __name__ == "__main__":
    main()
