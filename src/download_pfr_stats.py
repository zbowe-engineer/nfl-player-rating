import pandas as pd
import os

# Where to save CSV files
OUTPUT_DIR = "data"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Years you want to download
YEARS = range(2020, 2026)

# Stat categories and their PFR page names
STAT_PAGES = {
    "passing": "passing.htm",
    "rushing": "rushing.htm",
    "receiving": "receiving.htm",
    "defense": "defense.htm",
    "contracts": "salary.htm"
}

BASE_URL = "https://www.pro-football-reference.com/years/{year}/{page}"

def download_table(year, stat_name, page):
    url = BASE_URL.format(year=year, page=page)
    print(f"Downloading {stat_name} {year} from {url}")

    try:
        tables = pd.read_html(url)
        df = tables[0]
        filename = f"{OUTPUT_DIR}/{stat_name}_{year}.csv"
        df.to_csv(filename, index=False)
        print(f"Saved: {filename}")
    except Exception as e:
        print(f"Failed to download {stat_name} {year}: {e}")

def main():
    for year in YEARS:
        for stat_name, page in STAT_PAGES.items():
            download_table(year, stat_name, page)

if __name__ == "__main__":
    main()