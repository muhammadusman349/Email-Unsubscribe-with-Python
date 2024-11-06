import pandas as pd


# For save links to Excel file
def save_links_to_excel(links):
    data = [(idx + 1, link_url) for idx, link_url in enumerate(links)]
    df = pd.DataFrame(data, columns=["Link ID", "Link URL"])
    df.to_excel("links.xlsx", index=False)


# For save links to text file
def save_links(links):
    with open("links.txt", "w") as f:
        f.write("\n".join(links))
