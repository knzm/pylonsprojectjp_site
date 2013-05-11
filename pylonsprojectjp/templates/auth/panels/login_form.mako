<form action="${ login_url|h }" method="post" class="well form-horizontal">
  <input type="hidden" name="location" value="${ location|h }"/>
  <div class="control-group">
    <label class="control-label" for="username">username</label>
    <div class="controls">
      <input id="username" type="text" name="username" value="${ username|h }"/><br/>
    </div>
  </div>
  <div class="control-group">
    <label class="control-label" for="password">password</label>
    <div class="controls">
      <input id="password" type="password" name="password" value="${ password|h }"/><br/>
    </div>
  </div>
  <div class="form-actions">
    <input type="submit" value="Log In" class="btn btn-primary" />
  </div>
</form>
