# -*- coding:utf-8 -*-

# Количество топиков и статей на одну страницу
PAGINATE_BY = 20

# Базовый шаблон форумов. Вместо тестового нужно нарисовать свой
# и прописать его сюда
TEMPLATE_BASE = 'cicero_test/base.html'

# Директория, в которой лежат сессии OpenID.
# Без нее авторизация по OpenID работать не будет.
OPENID_STORE_ROOT = ''

# URL, который передается на OpenID-сервер для обозначения,
# где будет действовать авторизация. Не должно заканчиваться на '/'.
# Если не задано, передается URL всего сайта
OPENID_TRUST_URL = ''