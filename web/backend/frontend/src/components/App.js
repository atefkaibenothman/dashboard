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
    var apiURL = "http://localhost:8000/api/films"
    fetch(apiURL)
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
          <li key={actor.film_id}>
            {actor.title}: {actor.release_year}, {actor.rating}
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
