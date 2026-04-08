from controllers.controller import Controller

class TestController(Controller):
    def test (self, request, response):
        response.text = self.view.render_html('test/test.html', 
        {
          'title': 'MVC Framework - test',
          'h1' : 'Test page'
        })

    def action (self, request, response):
        response.text = self.view.render_html('test/action.html', 
        {
          'title': 'MVC Framework - action',
          'h1' : 'Action page',
          'action' : 'click'
        })