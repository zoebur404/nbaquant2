from nba_api.stats.endpoints import leaguedashplayerstats
from requests.exceptions import ReadTimeout, RequestException
import pandas as pd
import time

def fetch_players(max_retries: int = 3, sleep_seconds: int = 3) -> pd.DataFrame:
    """
    Fetch league-wide player stats with simple retry + graceful fallback.
    Returns an empty DataFrame if stats.nba.com keeps timing out.
    """
    last_err = None
    for attempt in range(1, max_retries + 1):
        try:
            df = leaguedashplayerstats.LeagueDashPlayerStats(timeout=30).get_data_frames()[0]
            return df
        except (ReadTimeout, RequestException) as e:
            last_err = e
            print(f"[fetch_players] Attempt {attempt}/{max_retries} failed: {e}")
            if attempt < max_retries:
                time.sleep(sleep_seconds)

    # Graceful fallback: don't kill the pipeline
    print(f"[fetch_players] All {max_retries} attempts failed. Returning empty DataFrame.")
    return pd.DataFrame()

def fetch_injuries() -> pd.DataFrame:
    """
    Placeholder injuries fetch: nba_api no longer exposes a stable live injury endpoint.
    Returns an empty DataFrame so the pipeline stays non-breaking.
    """
    return pd.DataFrame(columns=["PLAYER_NAME", "INJURY_STATUS"])
