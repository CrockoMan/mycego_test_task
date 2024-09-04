from typing import Optional

import requests

from src.constants import URL_PREFIX


def fetch_resources(
    public_key: str,
    path: Optional[str] = None
) -> list[dict[str, str]]:
    '''
    Получает список файлов и папок по публичной ссылке на Яндекс.Диск.

    :param public_key: Публичная ссылка на ресурсы Яндекс.Диска.
    :param path: Путь к папке (если None, то корневая папка).
    :return: Список файлов и папок в формате JSON.
    '''

    url = f'{URL_PREFIX}{public_key}'
    if path:
        url += f'&path={path}'

    response = requests.get(url)

    if response.status_code == 200:
        return response.json().get('_embedded', {}).get('items', [])

    return []


def get_target_file_name(
    public_key: str,
    target_file_name: str
) -> Optional[str]:
    """
    Получает URL оригинального файла по его имени.

    :param public_key: Публичный ключ для доступа к ресурсам.
    :param target_file_name: Имя файла, который нужно найти.
    :return: Кортеж из двух строк (URL оригинала файла, URL оригинала файла)
             если файл найден, иначе None.
    """

    items = fetch_resources(public_key)  # Получаем все файлы и папки

    # Ищем файл с искомым именем
    file_info = next(
        (item for item in items if item.get('name') == target_file_name),
        None
    )

    if file_info:
        # Извлекаем ссылку на оригинал из sizes
        original_url = file_info['sizes'][0]['url']
        return original_url

    return None
