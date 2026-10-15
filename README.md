# Python Fake Job Scraper

A beginner-friendly Python web scraping project that collects job listings from the practice website [Fake Jobs](https://realpython.github.io/fake-jobs/) and exports the results to a CSV file.

The project demonstrates how to send an HTTP request, parse HTML with Beautiful Soup, extract structured information from job cards, and save the results for later analysis.

## Features

- Scrapes job listings from the practice website.
- Extracts job title, company name, location, posting date, and application link.
- Parses HTML using Beautiful Soup with the `lxml` parser.
- Exports the collected listings to a CSV file that can be opened in Excel or other spreadsheet tools.
- Uses a request timeout to avoid waiting indefinitely for a response.

## Data collected

| Field | Description |
|---|---|
| Job Title | Title of the advertised role |
| Company Name | Company associated with the listing |
| Location | Location shown on the listing |
| Date Posted | Posting date displayed on the page |
| Apply Link | Link provided by the listing's Apply link |

## Tech stack

- Python 3
- Requests
- Beautiful Soup 4
- lxml
- Python's built-in `csv` module

## Project structure

```text
Python-FakeJob_scraper/
├── Job scraper.py
├── requirement.txt
├── joboutputcsv
└── README.md
```

- `Job scraper.py` — requests the page, extracts job data, and writes the CSV.
- `requirement.txt` — lists the third-party Python dependencies.
- `joboutputcsv` — existing output file included in the repository.

> Note: The script currently writes its results to `job.7_18_2026.csv` in the current working directory. The output filename is hard-coded in the script.

## Getting started

### 1. Clone the repository

```bash
git clone https://github.com/Neerajkumar1272/Python-FakeJob_scraper.git
cd Python-FakeJob_scraper
```

### 2. Create and activate a virtual environment (recommended)

**Windows**
```bash
python -m venv .venv
.venv\\Scripts\\activate
```

**macOS / Linux**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

The dependency file in this repository is named `requirement.txt` (singular):

```bash
python -m pip install -r requirement.txt
```

Alternatively, install the packages directly:

```bash
python -m pip install requests beautifulsoup4 lxml
```

### 4. Run the scraper

Because the script filename contains a space, keep the filename in quotes:

```bash
python "Job scraper.py"
```

When the script completes successfully, it creates `job.7_18_2026.csv` in the directory from which you ran it.

## How it works

1. **Request:** Requests the practice page using the Requests library and a browser-like User-Agent header.
2. **Parse:** Beautiful Soup parses the returned HTML using `lxml`.
3. **Extract:** The script loops through job cards and collects the five fields listed above.
4. **Export:** Python's `csv` module writes a header row and one row per extracted listing.

## Limitations and possible improvements

- The scraper is designed for the static practice website, not for arbitrary job boards.
- The current exception handling can be improved: the script catches request failures broadly and may continue without a valid response.
- It currently uses fixed CSS selectors and assumes the expected elements exist on each job card.
- The output filename is hard-coded instead of being configurable.
- The script does not currently deduplicate listings or provide search filters.
- The current implementation does not check HTTP status codes before parsing the response.

Potential next steps:
- Add clearer error messages and HTTP status checks.
- Handle missing HTML elements safely.
- Allow users to choose the output filename.
- Add keyword, company, or location filters.
- Add logging and tests for extraction and CSV export.

## Responsible use

This repository targets a public practice website built for learning web scraping. Before scraping any other website, review its terms of service, access rules, and applicable policies. Use reasonable request rates and do not collect private or restricted data.

## Author

**Neeraj Kumar**

