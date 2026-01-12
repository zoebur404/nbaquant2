from nba_api.stats.endpoints import leaguedashplayerstats
import pandas as pd

def fetch_players():
    df = leaguedashplayerstats.LeagueDashPlayerStats().get_data_frames()[0]
    return df

def fetch_injuries():
    # Placeholder: nba_api injuryreport endpoint is deprecated or unavailable
    return pd.DataFrame(columns=["PLAYER_NAME", "INJURY_STATUS"])
