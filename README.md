# Web Scraper - Scraping Game Links from MyRient

This Python script is designed to scrape all the game links from the **Myrient website**, extract their `href` (URL) and `title` attributes, and save them into a JSON file. The scraper specifically looks for `<td>` tags with the class `link`, processes the links within them, and returns a list of games with their corresponding URLs.

This scraper is intended to be used as a support tool for other applications that may need to collect game data from MyRient.

## Purpose

The script is tailored to extract game information in a structured format from the **MyRient** website, which will then be saved into a **JSON** file. This output can be utilized by other systems or applications that require access to the list of games and their associated URLs. 

It ensures the links are extracted in the same order they appear on the website.

### Example Output

The scraper will produce a JSON file that contains the following information about the games, according to their order on the site:

```json
[
    {
        "title": "Game Title 1",
        "link": "https://myrient.com/game1"
    },
    {
        "title": "Game Title 2",
        "link": "https://myrient.com/game2"
    }
]
```

### Fields:
- **title**: The `title` attribute of each game link.
- **link**: The full URL (constructed from the base URL and the `href` attribute of the game).

## Features

- Scrapes all game links from the **MyRient website**.
- Extracts `href` and `title` for each game.
- Outputs the data in a JSON file for easy integration with other applications.
- Preserves the order of games as displayed on the site.

## Prerequisites

Before running the script, you need to have the following Python libraries installed:

- **requests**: To send HTTP requests to the website.
- **beautifulsoup4**: To parse HTML and extract the desired data.
- **argparse**: To handle command-line arguments.
- **urllib.parse**: For joining URLs.

You can install the required libraries using `pip`:

```bash
pip install requests beautifulsoup4
```

## Usage

You can run the script directly from the command line and pass the URL of the **MyRient** website and the name of the output JSON file.

### Command-Line Syntax

```bash
python scraper.py <url> <output_filename.json>
```

- **`<url>`**: The URL of the **Myrient** website where the game data is located. Replace this with the link to the page you want to scrape.
- **`<output_filename.json>`**: The name of the JSON file where the scraped data will be saved.

## Error Handling

- If the website is unreachable or returns an HTTP error (e.g., 404, 500), an appropriate error message will be printed.
- If any exception occurs during scraping (such as a parsing error), it will be caught, and an error message will be displayed.

