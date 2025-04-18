import requests

# Функция для получения случайного изображения кошки через запрос к TheCatAPI
def get_image_cat():
    # Конечный адрес запроса
    url = 'https://api.thecatapi.com/v1/images/search'
    response = requests.get(url)
    # Если запрос успешный, возвращаем ссылку на картинку
    if response.status_code == 200:
        return response.json()[0]['url']
    # Иначе возвращаем None
    else:
        return None
