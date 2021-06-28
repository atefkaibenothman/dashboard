import React from "react";
import { ApolloClient, InMemoryCache, ApolloProvider, useQuery, gql } from "@apollo/client"

const ALL_ACTORS = gql`
  query {
    allFilms {
      title
      fulltext
    }
  }
`;

function Actors() {
  const { loading, error, data } = useQuery(ALL_ACTORS);
  if (loading) {
    return <p>Loading...</p>;
  }
  if (error) {
    return <p>Error</p>;
  }
  console.log(data);
  // return data.allFilms.map(({ title, fulltext }) => (
  //   <div key={title}>
  //     <p>
  //       {title}: {fulltext}
  //     </p>
  //   </div>
  // ));
  return (
    <div>
      <h2>Actors</h2>
    </div>
  )
}

export default Actors;
