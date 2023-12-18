


def url_to_textfile(url: str, filename: str)-> None:
    import requests
    response = requests.get(url)

    if not response.headers['content-type'].startswith("text/"):
        raise Exception("Invalid content type")
    with open(filename, "wt", encoding="utf-8") as soubor:
            soubor.write(response.text)


# Základní operace se souborem

with open("svejk.txt", "rb") as f: #vrací počet bytů
     print(len(f.read()))