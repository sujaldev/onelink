import { BrowserRouter as Router, Routes, Route } from "react-router-dom";

// COMPONENTS
import Settings from "./Components/Settings";
import TakeMeToTheLink from "./Components/TakeMeToTheLink";
import ErrorPage from "./Components/ErrorPage";

const App = () => {
  return (
    <Router>
      <div className="App">
        <Routes>
          <Route exact path="/error" element={<ErrorPage err={1} />} />
          <Route exact path="/:id/settings" element={<Settings />}></Route>
          <Route exact path="/:id" element={<TakeMeToTheLink />} />
          <Route path="*" element={<ErrorPage err={2} />} />
        </Routes>
      </div>
    </Router>
  );
};

export default App;
