from nba_api.stats.endpoints import injuryreport

def main():
    df = injuryreport.InjuryReport().get_data_frames()[0]
    print(df)

if __name__ == "__main__":
    main()
