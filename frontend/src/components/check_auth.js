import React, {useState, useEffect} from 'react';
import {useNavigate} from 'react-router-dom';
import {login} from "../api/auth/login";
import {message} from "antd";
import Cookies from 'js-cookie';


import { withRouter } from 'react-router-dom';

const withAuth = (Component) => {
    const WithAuth = (props) => {
        const navigate = useNavigate();
        const isLoggedIn = Cookies.get('token') ? true : false;
        // const isLoggedIn = localStorage.getItem('token') ? true : false;

        useEffect(() => {
            if (!isLoggedIn) {
                // Редиректим на страницу логина, если пользователь не авторизован
                navigate('/start');
            }
        }, [isLoggedIn, navigate]);

        // Возвращаем переданный компонент, если пользователь авторизован
        return isLoggedIn ? <Component {...props} /> : null;
    };

    return WithAuth;
};

// return WithAuth;

export default withAuth;
