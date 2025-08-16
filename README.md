# ProjectAutotest
## Проект по автоматизации тестирования
В рамках данного проекта были написаны автотесты для тестирования сервиса Кинопоиск

### Стек:
- pytest
- selenium
- webdriver manager
- requests
- _sqlalchemy_
- allure
- config
- json

### Структура:

#### ProjectAutotest
- requirements.txt            # зависимости
- pytest.ini                  # настройки pytest
- README.md                   # описание проекта
- conftest.py                 # фикстуры 
- config_local.py             # тестовые данные 

- API_test                    # папка для API тестов
  - test_api.py               # тесты API  
- UI_test                     # папка для UI тестов
  - pages/                    # папка со страницами
    - base_page.py            # общий функционал для всех страниц
    - main_page.py            # методы работы с главной страницей
    - film_and_actor_page.py  # страница фильма и страница актера
    - advanced_search_page    # расширенный поиск
    - articles_page.py        # страница статьи
    - search_results_page.py  # результаты поиска
  - tests/                        # папка с тестами UI
    - test_search.py              # тест поиска фильмов/актёров
    - test_film_and_actor_page.py # тест просмотра страниц фильмов и актёров
    - test_advanced_search.py     # тест расширенного поиска
    - test_articles.py            # тест просмотра статей/новостей

### Полезные ссылки
- [Подсказка по markdown](https://www.markdownguide.org/basic-syntax/)
- [Генератор файла .gitignore](https://www.toptal.com/developers/gitignore)
- [Про pip freeze](https://pip.pypa.io/en/stable/cli/pip_freeze/)
- [Cайт Кинопоиска](https://www.kinopoisk.ru/)
- [Документация для API Кинопоиска](https://api.kinopoisk.dev/documentation#/)

- [Финальный проект по ручному тестированию](https://an-rummo.yonote.ru/doc/avtotesty-mZfnaGKIAg)

### Шаги
1. Склонировать проект 'git clone https://github.com/имя_пользователя/ pytest_ui_api_template.git'
2. Установить зависимости pip3 install > -r requirements.txt
3. Запустить тесты 'pytest -s -v'
4. Сгенерировать отчет: 
   - перейти в нужную директорию для сохранения отчета
   - ввести команду 'allure generate allure-files -o allure-report'
5. Открыть отчет 'allure open allure-report'

### В UI-тесты входят:
- Простой поиск фильмов по названию 
- Простой поиск фильмов по актеру 
- Просмотр страницы фильма 
- Поиск информации про актера по фио 
- Просмотр страницы актера 
- Расширенный поиск 
- Просмотр статьи

### В API-тесты входят:
- Поиск фильмов по ID
- Поиск по ID без его указания
- Поиск сериалов по сезону и эпизоду
- Неверный вид запроса
- Поиск без авторизации
