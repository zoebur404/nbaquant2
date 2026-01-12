import pandas as pd

def main():
    players = pd.read_parquet("storage/players.parquet")
    injuries = pd.read_parquet("storage/injuries.parquet")
    markets = pd.read_parquet("storage/markets.parquet")

    print("Players:", len(players))
    print("Injuries:", len(injuries))
    print("Markets:", len(markets))

if __name__ == "__main__":
    main()
