import requests

api_key = "3b7878e0ce404ac6ad0b3917422faa7b"
url = "https://newsapi.org/v2/everything?q=tesla&" \
      "from=2022-10-19&sortBy=publishedAt&apiKey=" \
      "3b7878e0ce404ac6ad0b3917422faa7b"

# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the article titles and description
for article in content["articles"]:
    print(article["title"])
    print(article[["description"]])
