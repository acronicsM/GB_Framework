from datetime import date
from views import Index, Page, Examples, Contact, Another


def secret_front(request):
    request['date'] = date.today()


def other_front(request):
    request['key'] = 'key'


fronts = [secret_front, other_front]

routes = {
    '/': Index(),
    '/page.html/': Page(),
    '/examples.html/': Examples(),
    '/contact.html/': Contact(),
    '/another_page.html/': Another(),
}
