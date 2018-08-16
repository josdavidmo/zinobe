import hashlib

from sqlalchemy import func, or_
from sqlalchemy.orm import sessionmaker

from core.renders import JsonResponse, redirect, render
from core.request import GET, POST
from dbconfig import engine
from users.model import User


def list_get(environ, start_response):
    usr_session = environ['beaker.session']
    if usr_session.get('usr_id'):
        Session = sessionmaker()
        Session.configure(bind=engine)
        session = Session()
        usr = session.query(User).get(usr_session.get('usr_id'))
        context = {'usr': usr}
        return render(start_response, 'list.html', context)
    else:
        return redirect(start_response, '/')


def list_post(environ, start_response):
    usr_session = environ['beaker.session']
    if usr_session.get('usr_id'):
        Session = sessionmaker()
        Session.configure(bind=engine)
        session = Session()
        request = POST(environ)
        if request.get("search[value]"):
            query = session.query(User.name, User.email, User.country).filter(or_(
                User.email.contains(request.get("search[value]")),
                User.name.contains(request.get("search[value]"))))
        else:
            query = session.query(User.name, User.email, User.country)
        users = [[str(user.name), str(user.email), str(user.country)]
                 for user in query]
        response = {
            "draw": int(request["draw"]),
            "recordsTotal": len(users),
            "recordsFiltered": len(users),
            "data": users
        }
        return JsonResponse(start_response, str(response))
    else:
        return redirect(start_response, '/')
