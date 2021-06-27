import React, { Component } from "react";
import { render } from "react-dom";
import Actors from "./Actors"

class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      data: [],
    };
  }

  render() {
    return (
      <div>
        <h3>Dashboard</h3>
        <Actors />
      </div>
    );
  }

}

export default App;

const container = document.getElementById("app");
render(<App/>, container);
