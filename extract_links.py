from bs4 import BeautifulSoup


# Extract links from HTML content
def extract_links_from_html(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    links = [link["href"] for link in soup.find_all("a", href=True) if "unsubscribe" in link["href"].lower()]
    return links
