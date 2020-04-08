import React, {
  Component
} from 'react';
import {
  BrowserRouter,
  Switch,
  Route,
  Link
} from "react-router-dom";
import Home from './home';
import Header from './header';
import Login from "./login";
import Signup from "./signup";

class App extends Component {

  render() {
    return (
      <BrowserRouter>
        <div>
          <Header />
          <div className="ui container">

            <Switch>
              <Route exact path="/login/" component={Login}/>
              <Route exact path="/signup/" component={Signup}/>
              <Route path="/" render={Home}/>
            </Switch>
          </div>
        </div>
      </BrowserRouter>
    );
  }

}

export default App;