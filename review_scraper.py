import pandas as pd
from google_play_scraper import Sort, reviews

def scrape_google_play(app_id, country='us', lang='en', count=500000):
    print(f"Scraping Google Play Store reviews for app: {app_id}")
    result, _ = reviews(
        app_id,
        lang=lang,
        country=country,
        sort=Sort.MOST_RELEVANT,
        count=count
    )
    return result

def format_google_play_reviews(reviews):
    return pd.DataFrame(reviews)[['userName', 'content', 'score', 'at']]

def main():
    # Replace this with the actual app ID
    google_play_app_id = 'com.zeptoconsumerapp'

    # Scrape reviews
    google_play_reviews = scrape_google_play(google_play_app_id)

    # Format reviews
    df = format_google_play_reviews(google_play_reviews)

    # Add source column
    df['source'] = 'Google Play'

    # Export to Excel
    output_file = 'google_play_reviews.xlsx'
    df.to_excel(output_file, index=False)
    print(f"Reviews exported to {output_file}")

if __name__ == "__main__":
    main()
