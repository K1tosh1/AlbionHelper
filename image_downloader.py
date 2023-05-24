import requests
from PIL import Image
import os
from concurrent.futures import ThreadPoolExecutor
import json

# Создаем папку img, если она не существует
if not os.path.exists('img'):
    os.makedirs('img')

# Функция для загрузки и изменения размера изображения
def download_and_resize_image(name):
    print('downloading', name)
    url = 'https://render.albiononline.com/v1/item/'
    response = requests.get(url + name, stream=True)
    if response.status_code == 200:
        img_path = os.path.join('img', name + '.png')
        with open(img_path, 'wb') as f:
            for chunk in response.iter_content(1024):
                f.write(chunk)

        img = Image.open(img_path)
        img = img.resize((100, 100))
        img.save(img_path)

# Открываем файл JSON
with open('data.json', encoding='utf-8') as json_file:
    data = json.load(json_file)

# Получаем список UniqueName из файла JSON
unique_names = [item['UniqueName'] for item in data]

# Создаем пул потоков с максимальным количеством 10
with ThreadPoolExecutor(max_workers=5) as executor:
    # Запускаем функцию download_and_resize_image для каждого UniqueName
    executor.map(download_and_resize_image, unique_names)
