# ProjectAutotest
## Проект по автоматизации тестирования

### Стек:
- pytest
- selenium
- requests
- _sqlalchemy_
- allure
- config

### Структура:
### ProjectAutotest
- requirements.txt            # зависимости
- pytest.ini                  # настройки pytest
- README.md                   # описание проекта
- API_test
  - api_test

- UI_test
  - config_local.py           # тестовые данные
  - conftest.py               # фикстуры
  - pages/                    # описание страниц
    - base_page.py            # общий функционал для всех страниц
    - main_page.py            # методы работы с главной страницей
    - search_results_page.py  # результаты поиска
    - film_page.py            # страница фильма
    - actor_page.py           # страница актера
  - tests/                        # тесты
    - test_search.py              # тест поиска фильмов/актёров
    - test_film_and_actor_page.py # тест просмотра страниц фильмов и актёров
    - test_advanced_search.py     # тест расширенного поиска
    - test_articles.py            # тест просмотра статей/новостей

### Полезные ссылки
- [Подсказка по markdown](https://www.markdownguide.org/basic-syntax/)
- [Генератор файла .gitignore](https://www.toptal.com/developers/gitignore)

### Библиотеки
- pip install pytest
- pip install selenium
- pip install webdriver-manager
- pip install allure-pytest
- pip install requests

### Шаги
1. Склонировать проект 'git clone https://github.com/имя_пользователя/ pytest_ui_api_template.git'
2. Установить зависимости pip install -r requirements.txt
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