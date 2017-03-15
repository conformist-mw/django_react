import React from 'react'
import ReactDOM from 'react-dom'
import axios from 'axios'
import {
  BrowserRouter as Router,
  Route,
  Link
} from 'react-router-dom'

let User = function(props){
  return (
    <div className='user'>
      <div>Full Name: {props.user.full_name}</div>
      <div>Age: {props.user.age}</div>
      <div>Birth: {props.user.birth}</div>
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
      console.log(xhr)
    })
  },
  render: function(){
    return (
      <div>
        <h1>Our users are (overall count: {this.state.count}):</h1>
        <Link to="other">other</Link>
        <a href={this.state.next}>next</a>
        <a href={this.state.previous}>prev</a>
        {this.state.users.map(user => {
          return <User user={user} key={user.id} />
        })}
      </div>
    );
  }
})

let Other = function(){
  return (<div>
            <h1>Other</h1>
            <Link to="/">home</Link>
          </div>
  )
}

ReactDOM.render((
  <Router>
    <div>
      <Route exact path="/" component={Users} />
      <Route strict path="/other" component={Other} />
    </div>
  </Router>
), document.querySelector('#container'))
