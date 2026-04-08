from controllers.controller import Controller
from models.user import User
from models.user_auth_service import UserAuthService
from exceptions import InvalidArgumentException

class UsersController(Controller):

   def sing_up(self, request, response):


      if request.method == 'POST':
         try:
            user = User.sing_up(request.POST)
            if isinstance(user, User):
               response.text = self.view.render_html('users/sing_up_seccess.html')
               return
         
         except InvalidArgumentException as e:
            response.text = self.view.render_html('users/sing_up.html', {'title' : 'MVC Framework - регистрация', 'user_data' : request.POST, 'error' : e})
            return

         
      response.text = self.view.render_html('users/sing_up.html', {'title': 'MVC Framework - регистрация'})

   
   def sing_in(self, request, response):
      if request.method == 'POST':
         try:
            user = User.sing_in(request.POST)
            if isinstance(user, User):
               token = UserAuthService.create_token(user)
               response.set_cookie('token', token, 500, '/', False, httponly = True)
               response.status_code = 302
               response.location = '/articles'
               return
         
         except InvalidArgumentException as e:
            response.text = self.view.render_html('users/sing_in.html', {'title' : 'MVC Framework - вход n', 'user_data' : request.POST, 'error' : e})
            return
      
      
      response.text = self.view.render_html('users/sing_in.html', {'title': 'MVC Framework - вход'})


   def logout(self, request, response):
      response.set_cookie('token', '', -1, '/')
      response.status_code = 302
      response.location = request.referer


   # def user_list(self, request, response):
   #    if user 


   