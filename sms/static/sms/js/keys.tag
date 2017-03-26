<keys>

<h3 class="text-center">Manage your keys</h3>
<div class="text-center">
	<table class="table">
    <thead>
      <tr>
        <th>/url</th>
        <th>key</th>
        <th>active?</th>
        <th> </th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><code class="highligher-rouge">/sms/create</code></td>
        <td><span class="text-success">{key ? key : 'None'}</span></td>
        <td><span class="text-success">{active ? 'yes' : 'no'}<span></td>
        <td><button class="btn btn-success" onclick={createKey}>create key</button></td>
      </tr>
      <tr>
        <td><code class="highligher-rouge">/sms/submit</code></td>
        <td><span class="text-success">{key ? key : 'None'}</span></td>
        <td><span class="text-success">{active ? 'yes' : 'no'}<span></td>
        <td><button class="btn btn-success" onclick={submitKey}>submit key</button></td>
      </tr>
      <tr>
        <td><code class="highligher-rouge">/sms/check</code></td>
        <div class="input-group">
        <td><input class="form-control" id="uniq" type="text" maxlength="4"></td>
        <td><span class="text-success">{active ? 'yes' : 'no'}<span></td>
        <td><button class="btn btn-success" onclick={checkKey}>check key</button></td>
        </div>
      </tr>
      <tr>
        <td><code class="highligher-rouge">/sms/last</code></td>
        <td><span class="text-success">total remaining</span></td>
        <td><span class="text-success">{keys}<span></td>
        <td><button class="btn btn-success" onclick={getLast}>get total</button></td>
      </tr>
    </tbody>
  </table>
</div>
  <script>
  createKey(){
  	$.getJSON('/sms/create/').done(function(data){
  		this.key = data.id
  		this.active = data.active
  		this.update()
  	}.bind(this))
  };
  submitKey(){
  	$.get('/sms/submit/' + this.key + '/').done(function(){
  		this.active = false
  		this.update()
  	}.bind(this))
  };
  checkKey(){
  	$.getJSON('/sms/check/' + $('#uniq').val() + '/').fail(function(){
  		$('#uniq').parent().addClass('has-error')
  	}).done(function(data){
  		$('#uniq').parent().removeClass('has-error')
  		$('#uniq').parent().addClass('has-success')
  		this.key = data.id
  		this.active = data.active
  		this.update()
  	}.bind(this))
  };
  getLast(){
	$.getJSON('/sms/last/').done(function(data){
		this.keys = data.last
		this.update()
	}.bind(this))
};
  </script>
</keys>