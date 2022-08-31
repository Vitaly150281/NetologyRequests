import requests

url = "https://akabab.github.io/superhero-api/api/all.json"

resp = requests.get(url)
data = resp.json()

hero_dict = {}
hero_list = ['Hulk', 'Thanos', 'Captain America']

for hero in data:
    if hero['name'] in hero_list:
        hero_dict[hero['name']] = hero['powerstats']['intelligence']

print(max(hero_dict, key=hero_dict.get))

# №2
import json
import os

class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        """Метод загружает файл на яндекс диск"""
        upload_url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        filename = file_path.split('\ ')[-1]
        headers = {'Content-Type': 'application/json', 'Authorization': f'OAuth {self.token}'}
        params = {"path": f'{upload_url}?path={filename}', "overwrite": "true"}
        _response = requests.get(upload_url, headers=headers, params=params).json()
        href = _response.get("href", "")
        responce = requests.put(href, data=open(file_path, 'rb'))

        responce.raise_for_status()
        if responce.status_code == 201:
            return 'Успешно'
        else:
            return f"Ошибка загрузки! Код ошибки: {responce.status_code}"


if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    path_to_file = os.path.abspath('test.txt')
    token = ''
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)