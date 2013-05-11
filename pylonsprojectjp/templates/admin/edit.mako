<%inherit file="${ context['main_template'].uri }" />

<%def name="page_title()">
${ context['page_title']|h }
</%def>

<form method="POST" enctype="multipart/form-data" action="">
  <div>
    ${ form.display(value) }
  </div>
  <input type="hidden" name="_method" value="PUT" />
  ## <p class="fa_field">
  ##   ${ actions.buttons(request)|n }
  ## </p>
</form>
