from jinja2 import Template
from pathlib import Path

def render(template_name, **kwargs):
    """
    Минимальный пример работы с шаблонизатором
    :param template_name: имя шаблона
    :param kwargs: параметры для передачи в шаблон
    :return:
    """

    file_path = Path.cwd() / 'templates' / template_name
    with open(file_path, encoding='utf-8') as f:
        template = Template(f.read())

    return template.render(**kwargs)

