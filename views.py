from framework.templator import render
from framework.common import FactoryCreate
from patterns.creational_patterns import Engine, Logger

site = Engine()
logger = Logger('main')

class Index:
    def __call__(self, request):
        return '200 OK', render('index.html', date=request.get('date', None))


class Page:
    def __call__(self, request):
        return '200 OK', render('page.html', date=request.get('date', None))


class Examples:

    def __call__(self, request):
        id_category = None
        category = None

        if request['method'] == 'POST':
            data = request['data']
            for k, v in FactoryCreate.items():
                if k in data:
                    v.create(data, site)

        elif request['method'] == 'GET' and request['request_params']:
            category = site.find_category_by_id(int(request['request_params']['id']))
            id_category = category.id

        category_list = []
        for i in site.categories:
            if (id_category is None and i.category == id_category) \
                    or (i.category is not None and i.category.id == id_category):
                category_list.append(i)

        courses_list = [ i for i in site.courses if i.category == category]

        id_category = '' if id_category is None else id_category
        return '200 OK', render('examples.html', objects_list=category_list, courses_list=courses_list,
                                cat_id=id_category)


class Contact:
    def __call__(self, request):
        return '200 OK', render('contact.html', date=request.get('date', None))


class Another:
    def __call__(self, request):
        return '200 OK', render('another_page.html', date=request.get('date', None))

