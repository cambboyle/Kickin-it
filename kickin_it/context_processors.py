from django.urls import resolve


def is_home(request):
    ''' A context processor that returns \
    whether the current page is the home page '''

    match = resolve(request.path)
    return {
        'is_home': match.url_name == 'home'
    }
