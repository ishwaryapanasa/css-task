import requests

def fetch_poetry_data(author_name):
    # Define the URL for the PoetryDB API request
    url = f"http://poetrydb.org/author/{author_name}/title,linecount"
    
    # Make the HTTP request to the PoetryDB API
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code != 200:
        print("Failed to fetch data.")
        return None
    
    # Return the JSON response data
    return response.json()

def analyze_poetry_data(poetry_data):
    # Check if there are any poems returned
    if not poetry_data:
        print("0")
        return
    
    # Initialize variables to find the poem with the least number of lines
    min_lines = float('inf')
    min_line_poems = []
    total_lines = 0

    # Process each poem's data
    for poem in poetry_data:
        title = poem['title']
        lines = poem['linecount']
        
        # Update total lines count
        total_lines += lines
        
        # Update the minimum lines and corresponding poems
        if lines < min_lines:
            min_lines = lines
            min_line_poems = [title]
        elif lines == min_lines:
            min_line_poems.append(title)
    
    # Output the total number of lines
    print(total_lines)
    
    # Output the titles of the poem(s) with the least number of lines
    for title in min_line_poems:
        print(title)

def main():
    # Ask the user for the author's name
    author_name = input("Enter the author's name: ").strip()
    
    # Fetch poetry data for the given author
    poetry_data = fetch_poetry_data(author_name)
    
    # Analyze and output the poetry data
    analyze_poetry_data(poetry_data)

if __name__ == "__main__":
    main()
i