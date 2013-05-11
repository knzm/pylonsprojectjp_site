<%inherit file="${ context['main_template'].uri }" />

<div class="row">
  <div class="span8 offset2">
    <h1>${ self.page_title() }</h1>

    <div>
      <span>${ message|h }</span>
    </div>

    <div>
      ${ panel('login_form', form_value=form_value, form_error=form_error) }
    </div>
  </div>
</div>

## <%def name="page_title()">
##   ${ context['page_title']|h }
## </%def>
