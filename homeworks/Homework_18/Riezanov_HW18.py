import requests

BASE_URL = "https://images-api.nasa.gov"

def get_nasa(): #Шукаємо Curiosity повертаємо два nasa_id
    search_url = f"{BASE_URL}/search"

    search_params = {"q": "Curiosity rover Mars",
                     "media_type": "image",
                     "page_size": 20,
                     }
    response = requests.get(url=search_url, params=search_params, timeout=10)

    response.raise_for_status()

    data = response.json()
    items = data["collection"]["items"]

    nasa_ids = []
    for item in items:
        nasa_id = item["data"][0]["nasa_id"]
        nasa_ids.append(nasa_id)

        if len(nasa_ids) == 2:
            break
    return nasa_ids

def get_jpg_url(nasa_id): #Отримує список файлів для nasa_id то повертає посилання
    asset_url = f"{BASE_URL}/asset/{nasa_id}"

    response = requests.get(url=asset_url, timeout=10)

    response.raise_for_status()

    data = response.json()
    items = data["collection"]["items"]

    for item in items:
        file_url = item["href"]

        if file_url.lower().endswith(".jpg"):
            return file_url

    return None

def download_img(image_url, file_name): #Завантажуємо зображення
    response = requests.get(url=image_url, timeout=30)

    response.raise_for_status()

    with open(file_name, "wb") as f:
        f.write(response.content)

def main():
    nasa_ids = get_nasa()

    for number, nasa_id in enumerate(nasa_ids, start=1):
        jpg_url = get_jpg_url(nasa_id)

        if jpg_url is None:
            print(f"JPG для {nasa_id} не знайдено")
            continue

        filename = f"mars_photo{number}.jpg"

        download_img(
            image_url=jpg_url,
            file_name=filename
        )

        print(f"Збережено: {filename}")

if __name__ == "__main__":
    main()
