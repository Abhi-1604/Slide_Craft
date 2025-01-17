import requests
from pptx.util import Inches, Pt
from PIL import Image

google_api_key = "AIzaSyBInlUrGeNjRINe2Y5hMBBvza4ttfvBb70"
google_search_engine_id = "2298640b4e33b402a"

def search_google_images(query):
    url = "https://www.googleapis.com/customsearch/v1"
    num_images=1
    params = {
        "q": query,
        "num": num_images,
        "cx": google_search_engine_id,
        "key": google_api_key,
        "searchType": "image"
    }
    response = requests.get(url, params=params)
    data = response.json()
    image_urls = [item["link"] for item in data.get("items", [])]
    return image_urls