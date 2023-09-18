import requests
import csv

def get_links(filename):
    if not os.path.exists(filename) or os.stat(filename).st_size == 0:
        raise Exception("O arquivo `links.txt` não existe ou está vazio.")
    
def get_links(filename):
    with open(filename, "r") as f:
        reader = csv.reader(f)
        links = [row[0] for row in reader]
    return links

def main():
    filename = "links.txt"
    links = get_links(filename)

    # Cria o arquivo HTML de importação de favoritos
    with open("import.html", "w") as f:
        f.write("<bookmarks>\n")
        for link in links:
            f.write(f"\t<bookmark href=\"{link}\" title=\"{link}\" bookmark=\"true\">\n")
        f.write("</bookmarks>\n")

if __name__ == "__main__":
    main()