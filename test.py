import pytest
from main import get_image_cat

# Тест для проверки успешного запроса
def test_get_image_cat_success(mocker):
    # Создаем мок-объект
    mock_get = mocker.patch('main.requests.get')
    # Создаем мок-ответ для успешного запроса
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = [{'url': 'https://cdn2.thecatapi.com/images/21s.jpg'}]

    # Создаем переменную url_image, в которую будет сохраняться информация, полученная с помощью функции get_image_cat
    url_image = get_image_cat()

    # Сравниваем полученные данные с ожидаемыми
    assert url_image == 'https://cdn2.thecatapi.com/images/21s.jpg'

# Тест для проверки неуспешного запроса
def test_get_image_cat_with_error(mocker):
    # Создаем мок-объект
    mock_get = mocker.patch('main.requests.get')
    # Создаем мок-ответ для неуспешного запроса
    mock_get.return_value.status_code = 404

    # Создаем переменную url_image, в которую будет сохраняться информация, полученная с помощью функции get_image_cat
    url_image = get_image_cat()

    # Сравниваем полученные данные с ожидаемыми
    assert url_image == None