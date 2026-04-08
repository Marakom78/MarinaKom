from controllers.controller import Controller


class SiteController(Controller):
    def index (self, request, response):

        response.text = self.view.render_html('site/index.html', 
        {
          'title': 'MVC Framework',
          'h1' : 'Main page'
        })

    def about (self, request, response):
        response.text = self.view.render_html('site/about.html', 
        {
          'title': 'MVC Framework - about us',
          'h1' : 'About Us page'
        })

    def hello (self, request, response, user_name):
        response.text = self.view.render_html('site/hello.html', 
        {
          'title': 'MVC Framework - Greetings',
          'h1' : 'Hello!',
          'user' : user_name
        })