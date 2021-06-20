import React, { Component } from "react";
import { render } from "react-dom";

class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      data: [],
      loaded: false,
      placeholder: "Loading",
    };
  }

  componentDidMount() {
    fetch("api/actors")
      .then(response => {
        if (response.status > 400) {
          return this.setState(() => {
            return { placeholder: "something went wrong!" };
          });
        }
        return response.json();
      })
      .then(data => {
        this.setState(() => {
          return {
            data,
            loaded: true
          };
        });
      });
  }

  render() {
    return (
      <ul>
      {this.state.data.map(actor => {
        return (
          <li key={actor.id}>
            {actor.last_name}, {actor.first_name}
          </li>
        );
      })}
      </ul>
    );
  }

}

export default App;

const container = document.getElementById("app");
render(<App/>, container);
