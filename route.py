from controllers.site_controller import SiteController
from controllers.test_controller import TestController
from controllers.article_controller import ArticlesController
from controllers.users_controller import UsersController

routes = {
    r'^/article/(\d+)$': [ArticlesController, ArticlesController.view],
    r'^/article/(\d+)/edit$': [ArticlesController, ArticlesController.edit],
    r'^/article/(\d+)/delete$': [ArticlesController, ArticlesController.delete],
    r'^/articles$': [ArticlesController, ArticlesController.index],
    r'^/articles/add$': [ArticlesController, ArticlesController.add],
    r'^/user/register$': [UsersController, UsersController.sing_up],
    r'^/user/login$': [UsersController, UsersController.sing_in],
    r'^/user/logout$': [UsersController, UsersController.logout],
    # r'^/user/list$': [UsersController, UsersController.user_list],
    r'^/home$': [SiteController, SiteController.index],
    r'^/about$': [SiteController, SiteController.about],
    r'^/hello/(.*)$': [SiteController, SiteController.hello],
    r'^/test$': [TestController, TestController.test],
    r'^/action$': [TestController, TestController.action],
}