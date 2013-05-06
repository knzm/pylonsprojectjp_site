<table class="table table-bordered tablesorter">
  <thead>
    <tr>
      % for field in grid.render_fields.itervalues():
      <th>${ field.label() }</th>
      % endfor
    </tr>
  </thead>
  <tbody>
    % for row in grid.rows:
    <tr>
       <% grid._set_active(row) %>
       % for field in grid.render_fields.itervalues():
       <td>${ field.render_readonly()|n }</td>
       % endfor
     </tr>
     % endfor
  </tbody>
</table>
## <script>
##   $(function() {
##     $('table.tablesorter').tablesorter();
##   });
## </script>
