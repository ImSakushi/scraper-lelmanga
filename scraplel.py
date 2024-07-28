import sys
import os
import requests
from bs4 import BeautifulSoup
import re

def download_image(url, path):
    response = requests.get(url)
    if response.status_code == 200:
        with open(path, 'wb') as file:
            file.write(response.content)
    else:
        print(f"Erreur lors du téléchargement de {url}")

def scrape_and_download_manga(url):
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Erreur lors de la récupération de la page. Code d'état : {response.status_code}")
        return None

    soup = BeautifulSoup(response.text, 'html.parser')

    manga_title_elem = soup.find('div', class_='allc').find('a')
    if manga_title_elem:
        manga_name = manga_title_elem.text
    else:
        manga_name = "Unknown_Manga"

    chapter_elem = soup.find('div', class_='daw chpnw')
    if chapter_elem:
        chapter_number = re.search(r'\d+', chapter_elem.text).group()
    else:
        chapter_number = "Unknown_Chapter"

    folder_path = os.path.join(manga_name, f"Chapter_{chapter_number}")
    os.makedirs(folder_path, exist_ok=True)

    reader_area = soup.find('div', id='readerarea')
    if not reader_area:
        print("Aucune zone de lecture trouvée sur la page.")
        return None

    img_tags = reader_area.find_all('img')

    for i, img in enumerate(img_tags, 1):
        img_url = img.get('src')
        if img_url:
            file_name = f"page_{i:03d}.jpg"
            file_path = os.path.join(folder_path, file_name)
            print(f"Téléchargement de {img_url}")
            download_image(img_url, file_path)

    return manga_name

def generate_urls(base_url, start_chapter, end_chapter):
    base_parts = base_url.rsplit('-', 1)
    base_url = base_parts[0] + '-'
    for chapter in range(start_chapter, end_chapter + 1):
        yield f"{base_url}{chapter}"

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python scraplel.py [url chap début] [numero chap fin]")
    else:
        start_url = sys.argv[1]
        end_chapter = int(sys.argv[2])

        start_chapter = int(re.search(r'\d+$', start_url).group())

        for url in generate_urls(start_url, start_chapter, end_chapter):
            print(f"Traitement du chapitre : {url}")
            manga_name = scrape_and_download_manga(url)
            if manga_name is None:
                print(f"Échec du traitement pour l'URL : {url}")
                continue

        print("Téléchargement terminé.")
