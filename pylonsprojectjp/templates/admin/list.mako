<%inherit file="${ context['main_template'].uri }" />

<%def name="page_title()">
${ context['page_title']|h }
</%def>

<%def name="extra_head()">
  <link rel="stylesheet" type="text/css" href="/static/admin/css/list.css">
</%def>

<div class="ui-pager">
   ${ panel('pager', page=page) }
</div>
${ panel('grid', data=grid_data)|n }
<p class="fa_field">
  ${ panel('admin_buttons')|n }
</p>
