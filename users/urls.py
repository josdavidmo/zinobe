import selector

from users import view

urls = selector.Selector()
urls.add('/', GET=view.sign_in_user_get)
urls.add('/', POST=view.sign_in_user_post)
urls.add('/list/', GET=view.list_get)
urls.add('/list/', POST=view.list_post)
urls.add('/sign-up/', GET=view.sign_up_user_get)
urls.add('/sign-up/', POST=view.sign_up_user_post)
