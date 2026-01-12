from nba_quant.ingestion.odds import fetch_odds
from nba_quant.ingestion.nba import fetch_players, fetch_injuries
from nba_quant.data.storage import save_parquet

def main():
    players = fetch_players()
    injuries = fetch_injuries()
    odds = fetch_odds()

    save_parquet(players, "storage/players.parquet")
    save_parquet(injuries, "storage/injuries.parquet")
    save_parquet(odds, "storage/markets.parquet")

if __name__ == "__main__":
    main()
