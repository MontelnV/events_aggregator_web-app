## FAST-API + JINJA Project
## Description
Веб-приложение "Event Aggregator", создано с использованием Python и фреймворков FAST-API (backend) и Jinja (frontend). Приложение представляет собой агрегатор мероприятий, который позволяет пользователям изучать и просматривать разнообразные события.

На главной странице приложения пользователи могут легко просмотреть доступные мероприятия, ознакомиться с их деталями, такими как дата проведения, место, описание и т.д. Интуитивно понятный интерфейс позволяет пользователям фильтровать мероприятия и находить наиболее подходящий вариант.

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
![image](https://github.com/MontelnV/events_aggregator_web-app/assets/139653630/aa3e117a-7778-4822-ade9-9b1225b6a9bb)
![image](https://github.com/MontelnV/events_aggregator_web-app/assets/139653630/3d135e2a-dd5f-45cf-a08d-bc8483507640)
![image](https://github.com/MontelnV/events_aggregator_web-app/assets/139653630/ed2c89de-9a59-4d5a-bac6-afbc52b3f005)



