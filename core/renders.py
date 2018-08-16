import os

from jinja2 import Environment, FileSystemLoader

EXTENSIONS = {
    'html': 'text/html'
}

PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

TEMPLATE_ENVIRONMENT = Environment(
    autoescape=False,
    loader=FileSystemLoader(os.path.join(PATH, 'templates')),
    trim_blocks=False)


def render(start_response, template_file, context={}):
    """
    Renders a template.

    It takes and html file writing in jinja2 and render the context.

    Parameters
    ----------
    start_response : start_response
        WSGI start_response
    template_file : str
        path to template
    context : dict
        dictionary

    Returns
    -------
    list
        list render template with code 200

    """
    ext = template_file.rsplit(".")
    contenttype = "text/html"
    if len(ext) > 1 and (ext[1] in EXTENSIONS):
        contenttype = EXTENSIONS[ext[1]]

    body = TEMPLATE_ENVIRONMENT.get_template(
        template_file).render(**context).encode('utf8')

    start_response("200 OK", [('Content-Type', contenttype)])
    return [body]


def JsonResponse(start_response, json):
    """
    JsonResponse.

    Used to response a json.

    Parameters
    ----------
    start_response : start_response
        WSGI start_response
    json : dict
        dictionary

    Returns
    -------
    list
        list render json with code 200

    """
    start_response(
        "200 OK", [('Content-Type', 'application/json;charset=utf-8')])
    return [json.replace("'", '"').encode('utf-8')]


def redirect(start_response, url):
    """
    Redirect to url.

    Used to redirect.

    Parameters
    ----------
    start_response : start_response
        WSGI start_response
    url : string
        string defined in url file

    Returns
    -------
    list
        list render 1 with code 200

    """
    start_response('301 Moved Permanently', [('Location', url)])
    return ['1']
