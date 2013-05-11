# -*- coding: utf-8 -*-

def get_login_form_value(request):
    login_url = request.route_url('login')
    referrer = request.url
    if referrer == login_url:
        # never use the login form itself as came_from
        referrer = request.route_url('admin_dashboard')
    location = request.params.get('location', referrer)

    username = request.params.get('username', "")
    password = request.params.get('password', "")

    return {
        'location': location,
        'username': username,
        'password': password,
        }
