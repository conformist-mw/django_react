import React from 'react'
import ReactDOM from 'react-dom'
import axios from 'axios'
import {BrowserRouter as Router, Route, Link} from 'react-router-dom'
import createHistory from 'history/createBrowserHistory'

const history = createHistory()

let getUsers = function(){
  return axios.get('http://localhost:8080/instant/api/?page=' + page)
}

let getUser = function(id){
  return axios.get('http://localhost:8080/instant/api/' + id)
}

let User = function(props){
  return (
    <div className='user'>
      <div>Name: <Link to={'/profile/' + props.user.id}>{props.user.full_name}</Link></div>
    </div>
  )
}

let Users = React.createClass({
  getInitialState: function(){
    return {
      link: 'http://localhost:8080/instant/api',
      users: [],
      previous: '',
      next: '',
      count: 0
    }
  },
  componentDidMount: function(){
    axios.get(this.state.link).then(xhr => {
      this.setState({
        users: xhr.data.results,
        previous: xhr.data.previous,
        next: xhr.data.next,
        count: xhr.data.count
      });
    })
  },
  render: function(){
    return (
      <div>
        <h1>Our users are (overall count: {this.state.count}):</h1>
        <hr />
        {this.state.users.map(user => {
          return <User user={user} key={user.id} />
        })}
      </div>
    );
  }
})

let UserProfile = React.createClass({
  getInitialState: function() {
    return {
      name: null,
      age: null,
      birth: null
    }
  },
  componentDidMount: function() {
    getUser(this.props.match.params.id).then(xhr => {
      this.setState({
        name: xhr.data.full_name,
        age: xhr.data.age,
        birth: xhr.data.birth
      })
    })
  },
  render: function() {
    return (
      <div>
        <h3>User Profile: {this.state.name}</h3>
        <div>Age: {this.state.age}</div>
        <div>Birth: {this.state.birth}</div>
        <div>
          <button onClick={history.goBack}>back</button>
        </div>
      </div>
    )
  }
})

ReactDOM.render((
  <Router>
    <div>
      <Route exact path="/" component={Users} />
      <Route path="/profile/:id" component={UserProfile} />
    </div>
  </Router>
), document.querySelector('#container'))
