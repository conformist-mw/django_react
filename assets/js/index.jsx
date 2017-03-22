import React from 'react'
import ReactDOM from 'react-dom'
import axios from 'axios'
import {BrowserRouter as Router, Route, Link} from 'react-router-dom'
import createHistory from 'history/createBrowserHistory'

const history = createHistory()

let getPage = function(link){
  if (link.match('.*page') && link != null){
    return link.split('=').pop()
  }else{
    return 1;
  }
}

let getUser = function(id){
  return axios.get('/instant/api/' + id)
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
      link: '/instant/api/?page=',
      users: [],
      current: 1,
      prev: '',
      next: '',
      count: 0
    }
  },
  componentDidMount: function(){
    var link = this.state.link
    if(this.props.match.params.page){
      link = link + this.props.match.params.page 
    }else{
      link = link + this.state.current
    }
    axios.get(link).then(xhr => {
      this.setState({
        users: xhr.data.results,
        prev: (xhr.data.previous) ? getPage(xhr.data.previous) : 1,
        next: (xhr.data.next).split('=').pop(),
        count: xhr.data.count
      });
    })
  },
  componentWillReceiveProps(){
    return;
  },
  componentDidUpdate: function(prevProps, prevState){
    if(this.props.match.params.page){
      if(this.state.current !== this.props.match.params.page){
        var link = '/instant/api/?page=' + this.props.match.params.page
        axios.get(link).then(xhr => {
          this.setState({
            users: xhr.data.results,
            prev: (xhr.data.previous) ? getPage(xhr.data.previous) : 1,
            next: xhr.data.next.split('=').pop(),
            count: xhr.data.count,
            current: this.props.match.params.page
          });
        })
      }
    }
  },
  render: function(){
    return (
      <div>
        <h1>Our users are (overall count: {this.state.count}):</h1>
        <Link to={"/page/" + this.state.prev}>prev</Link>
        <Link to={"/page/" + this.state.next}>next</Link>
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
      <Route path="/page/:page" component={Users} />
    </div>
  </Router>
), document.querySelector('#container'))
