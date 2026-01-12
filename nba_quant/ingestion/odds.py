import requests
import pandas as pd
from nba_quant.config import ODDS_API_KEY, BOOKS

def fetch_odds():
    url = f"https://api.the-odds-api.com/v4/sports/basketball_nba/odds?apiKey={ODDS_API_KEY}&regions=us&markets=player_props"
    r = requests.get(url)
    data = r.json()

    rows = []
    for game in data:
        for bookmaker in game.get("bookmakers", []):
            if bookmaker["key"] not in BOOKS:
                continue
            for market in bookmaker.get("markets", []):
                for outcome in market.get("outcomes", []):
                    rows.append({
                        "player": outcome.get("description"),
                        "market": market.get("key"),
                        "line": outcome.get("point"),
                        "price": outcome.get("price"),
                        "book": bookmaker["key"]
                    })
    return pd.DataFrame(rows)
