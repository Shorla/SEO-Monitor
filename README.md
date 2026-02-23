# SEO Monitor CLI – SerpApi Demo

A Python CLI tool to fetch and monitor top Google search results using [SerpApi](https://serpapi.com/).  
Tracks changes in rankings over time and outputs results in a readable table or CSV.

---

## Features

- Input a keyword and fetch the top 10 Google search results
- Track changes in ranking since the last fetch
- Save results to CSV for historical tracking
- Lightweight and easy-to-use CLI

---

## Installation

1. **Clone the repository:**

```bash
git clone https://github.com/<your-username>/seo-monitor-cli.git
cd seo-monitor-cli

```
2. Install dependencies:

  ```bash
git clone https://github.com/<your-username>/seo-monitor-cli.git
cd seo-monitor-cli

```
3. Set your SerpApi API key:

Create a free SerpApi account: https://serpapi.com

Set your API key as an environment variable:

```bash
export SERPAPI_API_KEY="your_serpapi_api_key"  # macOS/Linux
set SERPAPI_API_KEY="your_serpapi_api_key"     # Windows

```

## Usage

Run the CLI script:

```bash
python seo_monitor.py

```
1. Enter a keyword when prompted.
2. View the top 10 search results in a neat table.
3. Optionally save results to CSV for tracking changes over time.

## Example Output
╒══════════╤════════════════════════════╤════════════════════════════════════════════╤════════╕
│ Position │ Title                      │ Link                                       │ Change │
╞══════════╪════════════════════════════╪════════════════════════════════════════════╪════════╡
│ 1        │ Example Title 1            │ https://example.com/article1               │ New    │
├──────────┼────────────────────────────┼────────────────────────────────────────────┼────────┤
│ 2        │ Example Title 2            │ https://example.com/article2               │ 1      │
├──────────┼────────────────────────────┼────────────────────────────────────────────┼────────┤
│ 3        │ Example Title 3            │ https://example.com/article3               │ -1     │
╘══════════╧════════════════════════════╧════════════════════════════════════════════╧════════╛

(Screenshot available in /screenshots/cli_output.png)
