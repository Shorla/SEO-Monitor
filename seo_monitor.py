# seo_monitor.py
# Python CLI tool to monitor top Google search results using SerpApi
# Tracks ranking changes over time

import os
import pandas as pd
from serpapi import GoogleSearch
from tabulate import tabulate

# Get SerpApi API key from environment variable
API_KEY = os.getenv("SERPAPI_API_KEY")

if not API_KEY:
    print("Please set your SerpApi API key in SERPAPI_API_KEY environment variable.")
    exit()

# CSV file to store historical search results
CSV_FILE = "seo_monitor_history.csv"

# Function to fetch top search results for a keyword
def fetch_top_results(keyword, num_results=10):
    """
    Fetch top search results from Google using SerpApi.

    Args:
        keyword (str): Search keyword
        num_results (int): Number of results to fetch (default 10)

    Returns:
        List[dict]: Structured search results with position, title, link, snippet
    """
    params = {
        "engine": "google",
        "q": keyword,
        "num": num_results,
        "api_key": API_KEY
    }

    search = GoogleSearch(params)
    results = search.get_dict()

    # Extract relevant info from organic results
    structured_results = []
    for i, r in enumerate(results.get("organic_results", []), 1):
        structured_results.append({
            "position": i,
            "title": r.get("title"),
            "link": r.get("link"),
            "snippet": r.get("snippet"),
            "keyword": keyword
        })
    return structured_results

# Function to load historical results from CSV
def load_history():
    """
    Load previous search results from CSV if exists.

    Returns:
        pandas.DataFrame: Historical search data
    """
    if os.path.exists(CSV_FILE):
        return pd.read_csv(CSV_FILE)
    # Return empty DataFrame if file doesn't exist
    return pd.DataFrame(columns=["keyword", "position", "title", "link", "snippet"])

# Function to save updated results to CSV
def save_history(df):
    """
    Save updated search results to CSV.

    Args:
        df (pandas.DataFrame): DataFrame containing current and past results
    """
    df.to_csv(CSV_FILE, index=False)

# Function to compare previous results with current
def compare_results(old_df, new_df):
    """
    Compare old and new search results to highlight ranking changes.

    Args:
        old_df (pandas.DataFrame): Previous results
        new_df (pandas.DataFrame): Current results

    Returns:
        List[dict]: List containing position, title, link, and change info
    """
    comparison = []
    # Map old links to their positions
    old_links = old_df.set_index("link")["position"].to_dict()
    for _, row in new_df.iterrows():
        old_pos = old_links.get(row["link"])
        if old_pos:
            change = old_pos - row["position"]  # Positive = moved up, Negative = moved down
        else:
            change = "New"  # New URL in top results
        comparison.append({
            "Position": row["position"],
            "Title": row["title"],
            "Link": row["link"],
            "Change": change
        })
    return comparison

# Main function to run CLI
def main():
    keyword = input("Enter keyword to monitor: ").strip()
    print(f"\nFetching top 10 results for '{keyword}'...\n")
    
    # Fetch current results from SerpApi
    new_results = pd.DataFrame(fetch_top_results(keyword))
    
    # Load historical results
    history = load_history()
    previous = history[history["keyword"] == keyword]

    # Compare new results with previous results
    comparison = compare_results(previous, new_results)

    # Display results nicely in the terminal
    print(tabulate(comparison, headers="keys", tablefmt="grid"))

    # Ask user if they want to save results to CSV
    save_csv = input("Save results to CSV? (y/n): ").lower()
    if save_csv == "y":
        # Append current results to historical data
        updated_history = pd.concat([history, new_results], ignore_index=True)
        save_history(updated_history)
        print(f"\nResults saved to {CSV_FILE}")

# Run CLI
if __name__ == "__main__":
    main()
