import os
from typing import Optional

import requests
from flask import Flask, render_template, request, send_file

from src.utils import fetch_resources, get_target_file_name

app = Flask(
    __name__,
    template_folder=os.path.join(os.path.dirname(__file__), '..', 'templates')
)


@app.route('/', methods=['GET', 'POST'])
def index() -> str:
    '''
    Главная страница приложения, отображает форму для ввода публичной ссылки
    и список файлов, если они были получены.

    :return: HTML-шаблон главной страницы.
    '''

    files: list[dict[str, str]] = []
    public_key: Optional[str] = None
    path: Optional[str] = None

    if request.method == 'POST':
        public_key = request.form.get('public_key')
        path = request.form.get('path')
        files: list[dict[str, str]] = fetch_resources(public_key, path)

    return render_template(
        './index.html',
        files=files,
        public_key=public_key
    )


@app.route('/download', methods=['POST'])
def download():
    '''
    Обрабатывает запрос на скачивание файла по указанному пути.
    :return: Файл для скачивания или сообщение об ошибке.
    '''

    public_key: Optional[str] = request.form.get('public_key')
    target_file_name: str = request.form.get('file_name')[1:]  # Имя файла

    original_url: Optional[str] = get_target_file_name(
        public_key,
        target_file_name
    )

    if original_url:

        # Отправляем файл
        return send_file(
            requests.get(original_url, stream=True).raw,
            as_attachment=True,
            download_name=target_file_name
        )

    return 'File not found', 404
