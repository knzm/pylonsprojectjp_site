<%inherit file="${ context['main_template'].uri }" />

<div>
  <table>
    ${ form.render() }
  </table>
</div>
<div>
  <p class="fa_field">
    ${ actions.buttons(request)|n }
  </p>
</div>
