import requests
import allure


@allure.step("GET запрос на {url}")
def get_request(url, headers=None):
    response = requests.get(url, headers=headers)
    allure.attach(
        response.text,
        name="Ответ сервера",
        attachment_type=allure.attachment_type.TEXT
    )
    return response


@allure.feature("Поиск фильмов по ID")
def test_search_movie_by_id(base_url, headers, film_id):
    with allure.step(f"Поиск фильма с ID={film_id}"):
        response = get_request(
            f"{base_url}/v1.4/movie/{film_id}", headers=headers)
        assert response.status_code == 200
        data = response.json()
        assert data.get("id") == film_id
        assert "name" in data


@allure.feature("Поиск по ID без его указания")
def test_search_by_id_without_id(base_url, headers):
    with allure.step("Отправляем запрос без ID"):
        response = get_request(f"{base_url}/v1.4/movie/", headers=headers)
        assert response.status_code in [400, 401]


@allure.feature("Поиск сериалов по сезону и эпизоду")
def test_search_serial_by_season_and_episode(base_url, headers, serial_data):
    with allure.step(
        f"Ищем сериал ID={serial_data['id']}, "
        f"сезон={serial_data['season']}, эпизод={serial_data['episode']}"
    ):
        url = f"{base_url}/v1.4/season?movieId={serial_data['id']}"
        response = get_request(url, headers=headers)
        assert response.status_code == 200, (f"Ожидался 200, получен "
                                             f"{response.status_code}")

        data = response.json()

        found = False
        for season in data.get("docs", []):
            if season["number"] == serial_data["season"]:
                for episode in season.get("episodes", []):
                    if episode["number"] == serial_data["episode"]:
                        found = True
                        allure.attach(
                            f"Найден сезон {season['number']} "
                            f"и эпизод {episode['number']}",
                            name="Результат поиска",
                            attachment_type=allure.attachment_type.TEXT
                        )
                        break

        assert found, (
            f"Сезон {serial_data['season']} и эпизод {serial_data['episode']} "
            f"не найдены в ответе API"
        )


@allure.feature("Неверный вид запроса")
def test_invalid_request_type(base_url, headers, film_id):
    with allure.step("Отправляем POST вместо GET"):
        response = requests.post(
            f"{base_url}/v1.4/movie/{film_id}", headers=headers)
        allure.attach(
            str(response.text), name="Ответ сервера",
            attachment_type=allure.attachment_type.TEXT)
        assert response.status_code in [400, 405]


@allure.feature("Поиск без авторизации")
def test_search_without_auth(base_url, film_id):
    with allure.step("Отправляем запрос без ключа авторизации"):
        response = get_request(f"{base_url}/v1.4/movie/{film_id}")
        assert response.status_code in [401, 403]
