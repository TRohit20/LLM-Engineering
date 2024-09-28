import pandas as pd
from google_play_scraper import Sort, reviews
import time
import random

def scrape_google_play(app_id, country='us', lang='en', count=10000):
    print(f"Scraping Google Play Store reviews for app: {app_id}")
    
    result = []
    while len(result) < count:
        try:
            # Scrape reviews
            reviews_batch, _ = reviews(
                app_id,
                lang=lang,
                country=country,
                sort=Sort.MOST_RELEVANT,
                count=min(10000, count - len(result)),  # Fetch in batches of 10000
            )
            result.extend(reviews_batch)
            print(f"Fetched {len(reviews_batch)} reviews, total: {len(result)}")
            
            # Random delay between requests to avoid IP blocking
            time.sleep(random.uniform(2, 5))  # Delay between 2 to 5 seconds
            
        except Exception as e:
            print(f"Error occurred: {e}")
            break  

    return result

def format_google_play_reviews(reviews):
    return pd.DataFrame(reviews)[['userName', 'content', 'score', 'at']]

def main():
    # Replace this with the app ID
    google_play_app_id = 'com.zeptoconsumerapp'

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
