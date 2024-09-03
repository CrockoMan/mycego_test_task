from flask import Flask, render_template, request, send_file
import requests
from typing import List, Dict, Any

from utils import fetch_resources

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index() -> str:
    '''
    Главная страница приложения, отображает форму для ввода публичной ссылки
    и список файлов, если они были получены.

    :return: HTML-шаблон главной страницы.
    '''
    files: List[Dict[str, Any]] = []
    public_key = None
    path = None

    if request.method == 'POST':
        public_key = request.form.get('public_key')
        path = request.form.get('path')  # Получаем путь к папке, если он есть
        files = fetch_resources(public_key, path)

    return render_template(
        'index.html',
        files=files,
        public_key=public_key
    )


@app.route('/download', methods=['POST'])
def download():
    '''
    Обрабатывает запрос на скачивание файла по указанному пути.
    :return: Файл для скачивания или сообщение об ошибке.
    '''
    public_key = request.form.get('public_key')
    target_file_name = request.form.get('file_name')[1:]  # Имя нужного файла

    items = fetch_resources(public_key)  # Получаем все файлы и папки

    # Ищем файл с искомым именем
    file_info = next(
        (item for item in items if item.get('name') == target_file_name),
        None
    )

    if file_info:
        # Извлекаем ссылку на оригинал из sizes
        original_url = file_info['sizes'][0]['url']
        print(original_url)

        # Отправляем файл напрямую
        return send_file(
            requests.get(original_url, stream=True).raw,
            as_attachment=True,
            download_name=target_file_name
        )

    return 'File not found', 404


if __name__ == '__main__':
    app.run(debug=True)
