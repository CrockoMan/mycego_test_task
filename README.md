## Mycego Тестовое задание Python-разработчик 
Тестовое задание. </br>
Описание задания

![image](https://github.com/user-attachments/assets/72c52215-6a8b-4231-b576-6331d037516d)

##### Стек: Pyton, Flask

Клонировать репозиторий и перейти в него в командной строке:

```
git clone git@github.com:CrockoMan/mycego_test_task.git
```

```
cd mycego_test_task
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv venv
```

* Если у вас Linux/macOS

    ```
    source venv/bin/activate
    ```

* Если у вас windows

    ```
    source venv/scripts/activate
    ```

Установить зависимости из файла requirements.txt:
* Если у вас Linux/macOS

    ```
    python3 -m pip install --upgrade pip
    ```
* Если у вас windows
* 
    ```
    pip install -r requirements.txt
    ```

Запустить проект:

```
python app.py
```

Для разворачивания проекта с помощью Docker требуется компьютер с 
предустановленным 
Docker и Docker-Compose. Инструкция по установке: https://docs.docker.com/  </br>
Сборка Docker-образа  </br>

```
docker compose -f docker-compose.yml up --build 
```

Для работы с проектом перейти по локальному адресу:

```
http://127.0.0.1:5000
```

Работа с проектом:  </br>
Введите публичную ссылку на ЯндексДиск в поле ввода  </br>
Нажмите "Получить файлы"  </br>
Отобразятся файлы и папки находящиеся на ЯндексДиске  </br>
Для перехода в папку нажмите "Открыть"  </br>
Для скачивания файла нажмите "Скачать", укажите путь для сохранения файла </br>

![image](https://github.com/user-attachments/assets/501b29c8-dc9f-4e2c-8b26-716b61756962)


Автор: [К.Гурашкин](https://github.com/CrockoMan)
