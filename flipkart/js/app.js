// simple react component 
import React from 'react';
// import reactdom
import ReactDOM from 'react-dom';
class App extends React.Component {
  render() {
    return (
      <div>
        <h1>React Router Example</h1>
      </div>
    );
  }
}
ReactDOM.render(<App/>, document.getElementById('app'));
// export default App;