<html>
  <head>
    <title>${ self.page_title() }</title>
  </head>
  <body>
    <div class="navbar">
      <div class="navbar-inner">
        <div class="container">
          % if layout.project_url and layout.project_name:
          <a class="brand" href="${ layout.project_url|h }">${ layout.project_name|h }</a>
          % endif
        </div>
      </div>
    </div>
    <div class="container">
      ${ next.body() }
    </div>
  </body>
</html>

<%def name="page_title()">
  ${ layout.page_title|h }
</%def>
