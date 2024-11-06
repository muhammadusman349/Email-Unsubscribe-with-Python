def save_links(links):
    with open("links.txt", "w") as f:
        f.write("\n".join(links))
