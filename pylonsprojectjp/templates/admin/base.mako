<!DOCTYPE html>
<!--[if lt IE 7]>      <html class="no-js lt-ie9 lt-ie8 lt-ie7"> <![endif]-->
<!--[if IE 7]>         <html class="no-js lt-ie9 lt-ie8"> <![endif]-->
<!--[if IE 8]>         <html class="no-js lt-ie9"> <![endif]-->
<!--[if gt IE 8]><!--> <html class="no-js"> <!--<![endif]-->
<head>
  <meta charset="utf-8" />
  <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
  <title>${ self.page_title() }</title>
  <meta name="viewport" content="width=device-width">
  <link rel="shortcut icon" href="/favicon.ico" />
  <link rel="stylesheet" href="/static/css/normalize.css">
  <link rel="stylesheet" href="/static/css/admin.css">
  ${ self.extra_head() }
</head>
  <body>
    <div class="navbar">
      <div class="navbar-inner">
        <div class="container">
          % if layout.project_url and layout.project_name:
          <a class="brand" href="${ layout.project_url }">${ layout.project_name }</a>
          % endif
          <ul class="nav">
            <li>
              <a href="${ request.route_url('admin_dashboard') }">Home</a>
            </li>
            <li class="dropdown">
              <a href="#" class="dropdown-toggle" data-toggle="dropdown">Menu<b class="caret"></b></a>
              <ul class="dropdown-menu">
                ${ panel('admin_menu') }
              </ul>
            </li>
            ## <li class="divider-vertical"></li>
            ## <%
            ##    if request.current_user:
            ##        username = request.current_user.username
            ##    else:
            ##        username = "guest"
            ##  %>\
            ## <li><p class="navbar-text">Hello! ${ username|h }</p></li>
          </ul>
          <%
             try:
                 logout_url = request.route_url('logout')
             except KeyError:
                 logout_url = None
           %>
          % if logout_url:
          <ul class="nav pull-right">
            <li><a href="${ logout_url }">Logout</a></li>
          </ul>
          % endif
        </div>
      </div>
    </div>
    <div class="container">
      <h1>${ self.page_title() }</h1>
      ${ next.body() }
    </div>
  </body>
</html>

<%def name="page_title()">
${ layout.page_title|h }
</%def>

<%def name="extra_head()">
</%def>
