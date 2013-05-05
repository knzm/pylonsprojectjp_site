from pyramid.security import authenticated_userid
from pyramid_layout.panel import panel_config

@panel_config('welcome', renderer='templates/welcome.jinja2')
def welcome(context, request):
    user_id = authenticated_userid(request)
    return {"user_id": user_id}
