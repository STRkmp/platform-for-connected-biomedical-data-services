import './App.css';
import { BrowserRouter, Route, Routes } from 'react-router-dom';
import BasicPage from "./pages/basic";
import React from "react";
import LoginPage from './pages/login';
import RegistrationPage from './pages/registration';


function App() {

  return (
      <BrowserRouter>
          <Routes>
              <Route path="/login" element={<LoginPage />} />
              <Route path="/register" element={<RegistrationPage />} />
              <Route path="/" element={<BasicPage />} />
          </Routes>
      </BrowserRouter>
  );
}

export default App;
