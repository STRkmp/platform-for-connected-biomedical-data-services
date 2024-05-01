import { Layout } from 'antd';
import {useState, useEffect} from "react";
import './App.css';
import { BrowserRouter, Route, Routes } from 'react-router-dom';
import Cookies from 'js-cookie';

import RegistrationPage from "./pages/register";
import LandingPage from "./pages/start";
import BasicPage from "./pages/basic";
import ReactDOM from 'react-dom';
import React from "react";
import LoginPage from "./pages/login";
import ProfilePage from "./pages/profil";
import ImageCarousel from "./components/carusel";


function App() {
    // const [loggedIn, setLoggedIn] = useState(false);
    // const loggedIn = !!Cookies.get('token');
    // useEffect(() => {
    //     const loggedIn = !!Cookies.get('token');
    //     console.log(loggedIn)
    //     const handleStorageChange = () => {
    //         // setLoggedIn(localStorage.getItem('token'));
    //     };
    //     window.addEventListener('storage', handleStorageChange);
    //     return () => window.removeEventListener('storage', handleStorageChange);
    // }, []);

    // const handleLogin = (token) => {
    //     // Обновление состояния авторизации при успешном входе
    //     localStorage.setItem('token', token);
    //     setLoggedIn(true);
    // };
    //
    // const handleLogout = () => {
    //     // Очистка токена и обновление состояния авторизации при выходе
    //     localStorage.removeItem('token');
    //     setLoggedIn(false);
    // };

  return (
      <BrowserRouter>
          <Routes>
              <Route exact path="/start" element={<LandingPage />} />
              <Route path="/register" element={<RegistrationPage />} />
              <Route path="/login" element={<LoginPage />} />
              {/*<Route path="/" element={loggedIn ? <BasicPage component={<ImageCarousel />} /> : <LandingPage />} /> />*/}
              <Route path="/" element={<BasicPage component={<ImageCarousel />} />} />
              <Route path="/profile" element={<BasicPage component={<ProfilePage />} />} />
          </Routes>
      </BrowserRouter>
      // <Layout className='window'>
      //
      //   <LandingPage />
      //       {/*<BasicPage />*/}
      //  </Layout>
  );
}

export default App;
