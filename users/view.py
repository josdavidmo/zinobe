import hashlib

from sqlalchemy import func, or_
from sqlalchemy.orm import sessionmaker

from core.renders import JsonResponse, redirect, render
from core.request import GET, POST
from dbconfig import engine
from users.model import User


def sign_in_user_get(environ, start_response):
    """
    Used to render sign in user.

    Renders sign_in.html .

    Parameters
    ----------
    start_response : start_response
        WSGI start_response
    environ : environ
        WSGI python environ

    Returns
    -------
    list
        sign in view

    """
    usr_session = environ['beaker.session']
    usr_session.delete()
    return render(start_response, 'sign_in.html')


def sign_in_user_post(environ, start_response):
    """
    Used to manage sign in user request.

    Manage sign_in.html request.

    Parameters
    ----------
    start_response : start_response
        WSGI start_response
    environ : environ
        WSGI python environ

    Returns
    -------
    list
        sign in view

    """
    request = POST(environ)
    Session = sessionmaker()
    Session.configure(bind=engine)
    session = Session()

    password = hashlib.sha256(request['password'].encode()).hexdigest()
    query = session.query(User).filter(
        User.email == request['email'], User.password == password)
    exists = query.count() == 1
    if exists:
        usr = query[0]
        usr_session = environ['beaker.session']
        usr_session['usr_id'] = usr.id
        usr_session.save()
        return redirect(start_response, '/list/')
    else:
        return redirect(start_response, '/')


def sign_up_user_get(environ, start_response):
    """
    Used to render sign up user.

    Renders sign_up.html .

    Parameters
    ----------
    start_response : start_response
        WSGI start_response
    environ : environ
        WSGI python environ

    Returns
    -------
    list
        sign up view

    """
    return render(start_response, 'sign_up.html')


def sign_up_user_post(environ, start_response):
    """
    Used to manage sign up user request.

    Manage sign_up.html request.

    Parameters
    ----------
    start_response : start_response
        WSGI start_response
    environ : environ
        WSGI python environ

    Returns
    -------
    list
        sign up view

    """
    request = POST(environ)

    fields = set(field for field in User.__dict__)
    dct = {key: value for key, value in request.items() if key in fields}
    user = User(**dct)
    user.password = hashlib.sha256(user.password.encode()).hexdigest()

    try:
        Session = sessionmaker()
        Session.configure(bind=engine)
        session = Session()
        session.add(user)
        session.commit()
        return redirect(start_response, '/')
    except Exception as e:
        return redirect(start_response, '/')


def list_get(environ, start_response):
    """
    Used to render list user.

    Renders list.html .

    Parameters
    ----------
    start_response : start_response
        WSGI start_response
    environ : environ
        WSGI python environ

    Returns
    -------
    list
        list view

    """
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
    """
    Used to manage list user request.

    Manage list.html request.

    Parameters
    ----------
    start_response : start_response
        WSGI start_response
    environ : environ
        WSGI python environ

    Returns
    -------
    list
        list view

    """
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
