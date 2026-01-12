from nba_api.stats.endpoints import leaguedashplayerstats, injuryreport
import pandas as pd

def fetch_players():
    df = leaguedashplayerstats.LeagueDashPlayerStats().get_data_frames()[0]
    return df

def fetch_injuries():
    df = injuryreport.InjuryReport().get_data_frames()[0]
    return df
