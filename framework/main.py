
class PageNotFound:
    def __call__(self, request):
        return '404 WHAT', '404 PAGE Not Found'


class Framework:

    def __init__(self, routes, fronts):
        self.routes = routes
        self.fronts = fronts

    def __call__(self, environ: dict, start_response):
        path: str = environ['PATH_INFO']

        if not path.endswith('/'):
            path = f'{path}/'

        view = self.routes.get(path, PageNotFound())

        request = dict()
        for i in self.fronts:
            i(request)

        code, body = view(request)
        start_response(code, [('Content-Type', 'text/html')])
        return [body.encode('utf-8')]

