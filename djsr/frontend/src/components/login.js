import React, {
  Component
} from "react";

class Login extends Component {
  constructor(props) {
    super(props);
    this.state = {
      username: "",
      password: ""
    };

    this.handleChange = this.handleChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
  }

  handleChange(event) {
    this.setState({
      [event.target.name]: event.target.value
    });
  }

  handleSubmit(event) {
    event.preventDefault();
    alert('You have been logged in.');
  }

  render() {
    return (
      <div>
        Login
        <form
          className="ui form"
          onSubmit={this.handleSubmit}
        >
          <label>
            Username:
            <input name="username" type="text" value={this.state.username} onChange={this.handleChange}/>
          </label>
          <label>
            Password:
            <input name="password" type="password" value={this.state.password} onChange={this.handleChange}/>
          </label>
          <button className="ui button primary">Submit</button>
        </form>
      </div>
    )
  }
}
export default Login;