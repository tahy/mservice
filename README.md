# mservice

Тестовый проект

Требования к системе: docker, docker-compose

## Порядок развертывания и запуска

> git clone https://github.com/tahy/mservice.git

> cd mservice

> docker-compose up

джанго сервер висит на 8000 порту

Приложение представляет из себя четыре эндпойнта:

-  /area/
-  /provider/
-  /service/

CRUD-ы для сущностей полигоны, поставщики, услуги соответственно

- /search/ - поиск

Формат поисковой строки: ?service=1&point=12,20 (id услуги и широта,долгота точки в которой ищем поставщиков)