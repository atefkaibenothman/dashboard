import React, { Component } from "react";
import { render } from "react-dom";
import { ApolloClient, InMemoryCache, ApolloProvider, useQuery, gql } from "@apollo/client"

// Components
import Actors from "./Actors"

class App extends Component {
  render() {
    const client = new ApolloClient({
      cache: new InMemoryCache(),
      uri: "http://127.0.0.1:8000/graphql/",
    });
    return (
      <div>
        <ApolloProvider client={client}>
          <h1>Dashboard</h1>
          <Actors />
        </ApolloProvider>
      </div>
    );
  }

}

export default App;

const container = document.getElementById("app");
render(<App/>, container);
