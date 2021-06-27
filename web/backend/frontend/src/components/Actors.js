import React, { Component } from "react";
import { render } from "react-dom";

class Actors extends Component {
  constructor(props) {
    super(props);
    this.state = {
      data: [],
    };
  }

  render() {
    return (
      <div>
        <h4>Actors</h4>
      </div>
    );
  }

}

export default Actors;
