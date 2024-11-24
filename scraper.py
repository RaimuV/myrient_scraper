import requests
from bs4 import BeautifulSoup
import json
import argparse
from urllib.parse import urljoin

def scrape_links_from_table(url, json_filename):
    try:
        # Send a request to the website
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        response = requests.get(url, headers=headers)

        # Check if the request was successful (HTTP status code 200)
        if response.status_code == 200:
            # Parse the HTML response
            soup = BeautifulSoup(response.text, 'html.parser')

            # Find all <td> tags with the class "link"
            table_cells = soup.find_all('td', class_='link')

            # Create a list to store the results
            links_data = []

            # Iterate over each element and extract href and title
            for cell in table_cells:
                link = cell.find('a')  # Find <a> tag inside <td>
                if link:
                    href = link.get('href')  # Extract the href attribute
                    title = link.get('title')  # Extract the title attribute
                    if href and title:
                        # Combine base URL with href to create full URL
                        full_url = urljoin(url, href)
                        # Add the data to the list
                        links_data.append({
                            'title': title,
                            'link': full_url
                        })

            # Save the results to a JSON file
            with open(json_filename, 'w', encoding='utf-8') as json_file:
                json.dump(links_data, json_file, ensure_ascii=False, indent=4)

            print(f"Data saved to the file '{json_filename}'.")

        else:
            print(f"Error: HTTP status code {response.status_code}")
    except Exception as e:
        print(f"Error during scraping: {e}")

def main():
    # Set up argparse to take arguments from the command line
    parser = argparse.ArgumentParser(description="Scrape links from a website and save them in a JSON file.")
    parser.add_argument("url", help="The URL of the website to scrape.")
    parser.add_argument("json_filename", help="The name of the JSON file to save the data.")

    # Parse the arguments from the command line
    args = parser.parse_args()

    # Run the scraping function
    scrape_links_from_table(args.url, args.json_filename)

if __name__ == "__main__":
    main()
