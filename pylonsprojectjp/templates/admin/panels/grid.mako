<table border="1">
<tr>
% for column in grid.columns:
  <th>${ column.label }</th>
% endfor
</tr>
% for item in grid.itemlist:
  <tr>
  % for column in grid.columns:
    <td>
      ${ column.render(item) }
    </td>
  % endfor
  </tr>
% endfor
</table>
