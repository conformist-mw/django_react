import React from 'react'
import ReactDOM from 'react-dom'
import axios from 'axios'
import {BrowserRouter as Router, Route, Link} from 'react-router-dom'
import createHistory from 'history/createBrowserHistory'
import bootstrap from 'bootstrap'
const history = createHistory()

let getPage = function(link){
  if (link.match('.*page') && link != null){
    return link.split('=').pop()
  }else{
    return 1;
  }
}

let User = function(props){
  return (
    <div className='user text-center'>
      <Link to={'/profile/' + props.user.id}>{props.user.full_name}</Link>
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
    }else{link = link + this.state.current}
    axios.get(link).then(xhr => {
      this.setState({
        users: xhr.data.results,
        prev: (xhr.data.previous) ? getPage(xhr.data.previous) : 1,
        next: (xhr.data.next).split('=').pop(),
        count: xhr.data.count
      });
    }).catch(error => {
      console.log(error)
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
      <div className="users">
        <h1>Our users are (overall count: {this.state.count}):</h1>
        <Link to={"/page/" + this.state.prev} className="prevLink"><span className="glyphicon glyphicon-chevron-left"></span></Link>
        <Link to={"/page/" + this.state.next} className="nextLink"><span className="glyphicon glyphicon-chevron-right"></span></Link>
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
      link: '/instant/api/',
    }
  },
  componentDidMount: function() {
    var link = this.state.link
    if(this.props.match.params.id){
      link = link + this.props.match.params.id 
    }else{link = link + this.state.current}
    axios.get(link + "/").then(xhr => {
      this.setState({
        name: xhr.data.full_name,
        age: xhr.data.age,
        birth: xhr.data.birth,
        email: xhr.data.email,
        ipv4: xhr.data.ipv4,
        phone: xhr.data.phone,
        street: xhr.data.street,
        city: xhr.data.city
      })
    })
  },
  render: function() {
    return (
      <div className="userProfile">
        <h3 className="text-center">{this.state.name}</h3>
        <p><b>Age</b>: {this.state.age}</p>
        <p><b>Birth</b>: {this.state.birth}</p>
        {this.state.email != null && <p><b>Email</b>: {this.state.email}</p> }
        {this.state.ipv4 != null && <p><b>ipv4</b>: {this.state.ipv4}</p> }
        {this.state.phone != null && <p><b>phone</b>: {this.state.phone}</p> }
        {this.state.street != null && <p><b>street</b>: {this.state.street}</p> }
        {this.state.city != null && <p><b>city</b>: {this.state.city}</p> }
        <div className="text-right div-btn">
          <button type="button" className="btn btn-primary" onClick={history.goBack}> ← Go back</button>
        </div>
      </div>
    )
  }
})

let MainPage = function(){
  return (
    <div className='main'>
      <div id="welcome"><Link to={'/page/1'}>Get started!</Link></div>
    </div>
  )
};

ReactDOM.render((
  <Router>
    <div>
      <Route exact path="/" component={MainPage} />
      <Route path="/profile/:id" component={UserProfile} />
      <Route path="/page/:page" component={Users} />
    </div>
  </Router>
), document.querySelector('#content'))
