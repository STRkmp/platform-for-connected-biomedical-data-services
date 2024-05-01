import React from 'react';
import { Button } from 'antd';
import { Link } from "react-router-dom";

const LandingPage = () => {
    return (
        <div style={{ display: 'flex', justifyContent: 'center', alignItems: 'center', height: '100vh' }}>
            <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'center' }}>
                <h1>Добро пожаловать!</h1>
                <div style={{ marginBottom: '24px' }}>
                        <Link to='/login' className="profile-button" style={{color: 'white'}}>
                            <Button type="primary" size="large" style={{ marginRight: '12px' }}>Войти</Button>
                        </Link>
                        <Link to='/register' className='register-button'>
                            <Button type="default" size="large">Зарегистрироваться</Button>
                        </Link>

                </div>
            </div>
        </div>
    );
};

export default LandingPage;
