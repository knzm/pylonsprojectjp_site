<%inherit file="${ context['main_template'].uri }" />

<form method="POST" enctype="multipart/form-data" action="">
  <div>
    ${ form.display(value) }
  </div>
  ## <p class="fa_field">
  ##   ${ actions.buttons(request)|n }
  ## </p>
</form>
