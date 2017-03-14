var React = require('react')
var ReactDOM = require('react-dom')

var UsersList = React.createClass({
	loadUsersFromServer: function(){
		$.ajax({
			url: this.props.url,
			datatype: 'json',
			cache: false,
			success: function(data){
				this.setState({data: data});
			}.bind(this)
		})
	},
	getInitialState: function(){
	    return {data: []};
	},
	componetDidMount: function(){
		this.loadUsersFromServer();
		setInterval(this.loadUsersFromServer, this.props.pollInterval)
	},
	render: function(){
		if (this.state.data){
			console.log('DATA!')
			var userNodes = this.state.data.map(function(user){
				return <li> {user.full_name} </li>
			})
		}
		return (
			<div>
				<h1>Hello React!</h1>
				<ul>
					{userNodes}
				</ul>
			</div>
		)
	}
})
ReactDOM.render(<UsersList url='/instant/api/' pollInterval={1000} />, document.getElementById('container'))