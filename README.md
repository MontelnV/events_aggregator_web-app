## FAST-API + JINJA Project
## Description
Веб-приложение "Events Aggregator", создано с использованием Python и фреймворков FAST-API (backend) и JINJA2+HTML+CSS+JS (frontend). Приложение представляет собой агрегатор мероприятий, который позволяет пользователям изучать и просматривать разнообразные события.

На главной странице приложения пользователи могут легко просмотреть доступные мероприятия, ознакомиться с их деталями, такими как дата проведения, место, описание и т.д. В зависимости от тега события выводится собственная обложка события (для IT - фоновое изображение с кодом, для других свои)

Для администраторов предусмотрен личный кабинет, где они могут вносить изменения в информацию о мероприятиях, добавлять новые события и удалять устаревшие. Пользователи с правами администратора имеют полный контроль над содержимым приложения и могут эффективно управлять всеми аспектами мероприятий.
P.S. Приложение находится еще в разработке и имеет неполный функционал)
### build
```
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
```
### run
```
uvicorn main:app --reload
```
### docker build
```
docker build . --tag events
docker run -d -p 8081:8081 events
```
<img src="https://github.com/MontelnV/events_aggregator_web-app/assets/139653630/346f9a33-4327-4c8d-8c1d-6c36a04acfba" width="200" />
<img src="https://github.com/MontelnV/events_aggregator_web-app/assets/139653630/d7744820-4314-4bdc-aab0-5b72ed71826c" width="200" />
<img src="https://github.com/MontelnV/events_aggregator_web-app/assets/139653630/0bc0dcfe-253b-400b-883d-7269661c630a" width="200" />
<img src="https://github.com/MontelnV/events_aggregator_web-app/assets/139653630/9aad0cb3-a0ef-4dd5-ad67-42c8cd30f599" width="200" />






