import os
import requests
import nfl_data_py as nfl
import pandas as pd
import time

# -----------------------------
# Folder Setup
# -----------------------------
BASE_DIR = "data"

PLAYER_WEEKLY_DIR = os.path.join(BASE_DIR, "player_weekly")
PLAYER_SEASON_DIR = os.path.join(BASE_DIR, "player_season")
SALARY_DIR = os.path.join(BASE_DIR, "salary_cap")

os.makedirs(PLAYER_WEEKLY_DIR, exist_ok=True)
os.makedirs(PLAYER_SEASON_DIR, exist_ok=True)
os.makedirs(SALARY_DIR, exist_ok=True)

# nfl_data_py supports 2019–2024
YEARS = list(range(2019, 2025))

TEAMS = [
    "arizona-cardinals", "atlanta-falcons", "baltimore-ravens", "buffalo-bills",
    "carolina-panthers", "chicago-bears", "cincinnati-bengals", "cleveland-browns",
    "dallas-cowboys", "denver-broncos", "detroit-lions", "green-bay-packers",
    "houston-texans", "indianapolis-colts", "jacksonville-jaguars", "kansas-city-chiefs",
    "las-vegas-raiders", "los-angeles-chargers", "los-angeles-rams", "miami-dolphins",
    "minnesota-vikings", "new-england-patriots", "new-orleans-saints", "new-york-giants",
    "new-york-jets", "philadelphia-eagles", "pittsburgh-steelers", "san-francisco-49ers",
    "seattle-seahawks", "tampa-bay-buccaneers", "tennessee-titans", "washington-commanders"
]

def download_salary_cap(year):
    all_players = []

    print(f"\nDownloading player salary cap for {year}...")

    for team in TEAMS:
        url = f"https://www.spotrac.com/nfl/{team}/cap/{year}/"

        headers = {
            "User-Agent": "Mozilla/5.0",
            "Accept": "text/html",
            "Referer": "https://www.spotrac.com/"
        }

        try:
            r = requests.get(url, headers=headers)
            r.raise_for_status()

            # Only take the FIRST table — the real player contract table
            df = pd.read_html(r.text)[0]

            # Rename the first column to player_name
            first_col = df.columns[0]
            df = df.rename(columns={first_col: "player_name"})

            # Keep only relevant columns
            keep_cols = ["player_name", "cap hit", "cap hit pct  league cap"]
            keep_cols = [c for c in keep_cols if c in df.columns]

            df = df[keep_cols]

            df["team"] = team
            df["season"] = year

            all_players.append(df)

            print(f"  ✓ {team} ({len(df)} players)")

            time.sleep(0.5)

        except Exception as e:
            print(f"  ✗ Failed for {team}: {e}")

    return pd.concat(all_players, ignore_index=True)

# -----------------------------
# Main Pipeline
# -----------------------------
def main():

    # -------------------------
    # SEASON STATS (per year)
    # -------------------------
    print("\n=== DOWNLOADING SEASON STATS (2019–2024) ===")
    all_season = []

    for year in YEARS:
        print(f"Importing season stats for {year}...")
        df = nfl.import_seasonal_data([year])
        df.to_csv(os.path.join(PLAYER_SEASON_DIR, f"player_season_{year}.csv"), index=False)
        all_season.append(df)

    # Save combined
    combined_season = pd.concat(all_season, ignore_index=True)
    combined_season.to_csv(os.path.join(PLAYER_SEASON_DIR, "player_season_all.csv"), index=False)
    print("Saved combined season stats.")


    # -------------------------
    # WEEKLY STATS (per year)
    # -------------------------
    print("\n=== DOWNLOADING WEEKLY STATS (2019–2024) ===")
    all_weekly = []

    for year in YEARS:
        print(f"Importing weekly stats for {year}...")
        df = nfl.import_weekly_data([year])
        df.to_csv(os.path.join(PLAYER_WEEKLY_DIR, f"player_weekly_{year}.csv"), index=False)
        all_weekly.append(df)

    # Save combined
    combined_weekly = pd.concat(all_weekly, ignore_index=True)
    combined_weekly.to_csv(os.path.join(PLAYER_WEEKLY_DIR, "player_weekly_all.csv"), index=False)
    print("Saved combined weekly stats.")


    # -------------------------
    # SALARY CAP (per year)
    # -------------------------
    print("\n=== DOWNLOADING PLAYER SALARY CAP (2019–2024) ===")
    all_salary = []

    for year in YEARS:
        df = download_salary_cap(year)
        df.to_csv(os.path.join(SALARY_DIR, f"salary_cap_{year}.csv"), index=False)
        all_salary.append(df)

    combined_salary = pd.concat(all_salary, ignore_index=True)
    combined_salary.to_csv(os.path.join(SALARY_DIR, "salary_cap_all.csv"), index=False)

    print("Saved combined player salary cap data.")


if __name__ == "__main__":
    main()