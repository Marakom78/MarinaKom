def home(request, response):
    response.text = "Привет с домашней страницы"


def about(request, response):
    response.text = "Привет со страницы about"

