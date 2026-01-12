from nba_api.stats.endpoints import leaguedashplayerstats

def main():
    df = leaguedashplayerstats.LeagueDashPlayerStats().get_data_frames()[0]
    top = df.sort_values("PTS", ascending=False).head(10)
    print(top[["PLAYER_NAME", "PTS"]])

if __name__ == "__main__":
    main()
