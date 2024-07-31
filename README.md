Тестовое задание на позицию Backend-разработчик на языке Python.
Требуется разработать API-сервис для получения данных о первых 10 объявлениях по ссылке https://www.farpost.ru/vladivostok/service/construction/guard/+/Системы+видеонаблюдения/ .
Для решения задачи необходимо:
Разработать модели при помощи фреймворка Django/FastAPI со следующими полями:
1. заголовок объявления;
2. id объявления;
3. автор объявления;
4. количество просмотров объявления;
5. позиция, на которой стоит объявление.

Данные могут быть добавлены в БД вручную или любым удобным для вас способом.
Разработать методы API для обращения к данным моделям. Запрос к API должен иметь параметр ID. При обращении, API должен возвращать информации об объявлении с ID, переданным в запросе, в формате JSON.
Требования к реализации API:
При разработке должен быть использован язык Python и фреймворк Django/FAST Api.
В качестве результата должен быть предоставлен репозиторий на GitHub;
Сервис должен использовать принципы ООП.
Дополнительные требования, не обязательны к выполнению, но будут являться большим плюсом:
Реализована система регистрации и входа (верификации аккаунта) для подключения к API (без функционала смены и/или восстановления пароля);
Все обращения к базе данных должны быть реализованы при помощи ORM запросов.
