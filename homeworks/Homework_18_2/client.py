from pathlib import Path
from urllib.parse import quote

import requests


BASE_URL = "http://127.0.0.1:8080"
IMAGE_PATH = "test_image.jpg"


def upload_image(image_path):
    with open(image_path, "rb") as image_file:
        files = {
            "image": image_file
        }

        response = requests.post(
            url=f"{BASE_URL}/upload",
            files=files,
            timeout=10
        )

    response.raise_for_status()

    data = response.json()

    print("POST status:", response.status_code)
    print("POST response:", data)

    return data["image_url"]


def get_image_url(filename):
    encoded_filename = quote(filename)

    headers = {
        "Content-Type": "text"
    }

    response = requests.get(
        url=f"{BASE_URL}/image/{encoded_filename}",
        headers=headers,
        timeout=10
    )

    response.raise_for_status()

    data = response.json()

    print("GET status:", response.status_code)
    print("GET response:", data)

    return data["image_url"]


def delete_image(filename):
    encoded_filename = quote(filename)

    response = requests.delete(
        url=f"{BASE_URL}/delete/{encoded_filename}",
        timeout=10
    )

    response.raise_for_status()

    data = response.json()

    print("DELETE status:", response.status_code)
    print("DELETE response:", data)


def main():
    filename = Path(IMAGE_PATH).name

    uploaded_url = upload_image(IMAGE_PATH)
    print("Зображення завантажено:", uploaded_url)

    received_url = get_image_url(filename)
    print("Посилання отримано:", received_url)

    delete_image(filename)
    print("Зображення видалено")


if __name__ == "__main__":
    main()