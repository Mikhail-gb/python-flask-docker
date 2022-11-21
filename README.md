# python-flask-docker
Итоговый проект (пример) курса "Машинное обучение в бизнесе"

Стек:

ML: sklearn, pandas, numpy
API: flask
Данные: sklearn.datasets.load_iris

Задача: предсказать тип Ириса

Используемые признаки:

- sepal length (text)
- sepal width (text)
- petal length (text)
- petal width (text)


Модель: xgboost

### Клонируем репозиторий и создаем образ
```
$ git clone https://github.com/Mikhail-gb/python-flask-docker.git
$ cd python-flask-docker
$ docker build -t gb/lesson_9 .
```

### Запускаем контейнер

Здесь Вам нужно создать каталог локально и сохранить туда предобученную модель (<your_local_path_to_pretrained_models> нужно заменить на полный путь к этому каталогу)
```
$ docker run -d -p 8180:8180 -p 8181:8181 -v <your_local_path_to_pretrained_models>:/app/app/models gb/lesson_9
```

### Переходим на localhost:8181
