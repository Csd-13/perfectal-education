"""
Scrape content from a list of URLs and save the aggregated text to a file.
This script is provided for educational purposes. Before using it,
please review the legal and ethical considerations regarding web scraping.
"""

import requests
from bs4 import BeautifulSoup
import time

def scrape_url(url):
    """
    Fetches a web page and extracts its text content.
    
    Args:
        url (str): The URL of the web page to scrape.
    
    Returns:
        str: The cleaned text from the page, or an empty string if an error occurs.
    """
    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (compatible; AITrainingBot/1.0)"
        }
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        html_content = response.text
        
        # Parse page content with BeautifulSoup
        soup = BeautifulSoup(html_content, 'html.parser')
        
        # Remove unwanted script and style elements
        for unwanted in soup(["script", "style"]):
            unwanted.decompose()
        
        # Get the visible text and clean it up
        text = soup.get_text(separator="\n")
        lines = [line.strip() for line in text.splitlines() if line.strip()]
        clean_text = "\n".join(lines)
        return clean_text
    except Exception as e:
        print(f"Error scraping {url}: {e}")
        return ""

def main():
    # List of URLs to be scraped.
    urls = [
        "https://www.ency-education.com/",
        "https://www.dzexams.com/",
        "https://www.manaradocs.com/",
        "https://eddirasa.com/",
        "https://www.edu-dz.com/",
        "https://www.bac35.com/",
        "https://www.seyf-educ.com/",
        "https://baramjak.com/",
        "https://www.dzetude.com/",
        "https://www.ta3lime.com/",
        "https://etudiant.elkhadra.com/",
        "https://www.stivandz.com/",
        "https://www.selsabil.com/",
        "https://monpdf.weebly.com/",
        "http://elbassair.net/",
        "https://www.staralgeria.net/",
        "https://www.education.gov.dz/%D8%A7%D9%84%D8%A8%D8%B1%D8%A7%D9%85%D8%AC-%D8%A7%D9%84%D8%AA%D8%B9%D9%84%D9%8A%D9%85%D9%8A%D8%A9/"
    ]
    
    all_text = ""

    for url in urls:
        print(f"Scraping {url}...")
        text = scrape_url(url)
        if text:
            # Append a header for clarity in the aggregated output.
            header = f"\n\n{'='*80}\nContent from: {url}\n{'='*80}\n\n"
            all_text += header + text
        # Pause for 1 second between requests to be polite to the server.
        time.sleep(1)
    
    # Save the aggregated text to a file.
    output_file = "training_data.txt"
    try:
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(all_text)
        print(f"Scraping complete. Data saved to {output_file}")
    except Exception as e:
        print(f"Error writing to file: {e}")

if __name__ == "__main__":
    main()