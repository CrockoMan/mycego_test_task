from typing import Any, Dict, List, Optional

import requests

from constants import URL_PREFIX


def fetch_resources(public_key: str, path: Optional[str] = None) -> List[Dict[str, Any]]:
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
