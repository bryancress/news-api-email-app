import requests
import os
from send_email import send_email

topic = "tesla"

news_api_key = os.getenv("NEWS_API_KEY")
url = "https://newsapi.org/v2/everything?" \
      f"q={topic}&" \
      "from=2022-11-22&" \
      "sortBy=publishedAt&" \
      "language=en&" \
      "pageSize=20&" \
      f"apiKey={news_api_key}" \

# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the article titles and description
body = "Subject: Today's News" + "\n"
for article in content["articles"]:
    if article["title"] is not None:
        body = body + article["title"] + "\n" \
                    + article["description"] + "\n" \
                    + article["url"] + 2*"\n"

body = body.encode("utf-8")
send_email(message=body)
