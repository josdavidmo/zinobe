import selector

from users import view

urls = selector.Selector()
urls.add('/list/', GET=view.list_get)
urls.add('/list/', POST=view.list_post)
