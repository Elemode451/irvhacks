import React from "react";
import { BrowserRouter as Router, Route, Routes, Switch, Link } from "react-router-dom";
import "./App.css";
import './output.css';  

// Components: 
import NavBar from "./Components/NavBar";

// Pages:
import About from "./pages/About";
import Doctors from "./pages/Doctors";
import Home from "./pages/Home";
import Search from "./pages/Search";
import Results from "./pages/Results";
import Contact from "./pages/Contact";

function App() {
  return (
    <Router>
      <NavBar />  {/* NavBar is where the links to navigate between pages go */}
      <Routes>
        <Route path="/" element={<Home />} /> {/* Route for homepage */}
        <Route path="/search" element={<Search />} /> {/*Route for search page */}
        <Route path="/about" element={<About />} /> {/* Route for About page */}
        <Route path="/contact-us" element={<Contact />} /> {/* Route for Contact page */}
        <Route path="/results" element={<Results />} /> {/* Route for Results page */}
      </Routes>
    </Router>
  );
}

export default App;