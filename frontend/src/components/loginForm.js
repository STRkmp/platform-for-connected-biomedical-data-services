import React, { useState } from 'react';
import { Form, Input, Button, message } from 'antd';
import axios from 'axios';
import Cookies from 'js-cookie';
import { Link } from 'react-router-dom';
import './AuthForms.css'; // Импорт стилей

const LoginForm = () => {
    const [loading, setLoading] = useState(false);

    const onFinish = async (values) => {
        try {
            setLoading(true);
            const response = await axios.post('http://localhost:8687/api/login/', values);
            const { token } = response.data;
            Cookies.set('token', token);
            message.success('Авторизация успешна');
            // Перенаправляем пользователя на главную страницу после успешной аутентификации
            window.location.href = '/';
        } catch (error) {
            console.error('Ошибка при входе:', error);
            message.error('Ошибка при входе');
        } finally {
            setLoading(false);
        }
    };

    return (
        <div className="auth-container">
            <h1>Вход</h1>
            <Form
                name="login"
                initialValues={{ remember: true }}
                onFinish={onFinish}
                className="auth-form"
            >
                <Form.Item
                    name="username"
                    rules={[{ required: true, message: 'Введите имя пользователя' }]}
                >
                    <Input placeholder="Имя пользователя" />
                </Form.Item>

                <Form.Item
                    name="password"
                    rules={[{ required: true, message: 'Введите пароль' }]}
                >
                    <Input.Password placeholder="Пароль" />
                </Form.Item>

                <Form.Item>
                    <Button type="primary" htmlType="submit" loading={loading}>
                        Войти
                    </Button>
                    Или <Link to="/register">зарегистрируйтесь</Link>
                </Form.Item>
            </Form>
        </div>
    );
};

export default LoginForm;
