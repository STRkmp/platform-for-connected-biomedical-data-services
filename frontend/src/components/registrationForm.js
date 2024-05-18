import React, { useState } from 'react';
import { Form, Input, Button, message } from 'antd';
import axios from 'axios';
import { Link } from 'react-router-dom';
import './AuthForms.css'; // Импорт стилей

const RegisterForm = () => {
    const [loading, setLoading] = useState(false);

    const onFinish = async (values) => {
        try {
            setLoading(true);
            // Отправить данные на сервер для регистрации
            message.success('Регистрация успешна');
            // Перенаправляем пользователя на страницу входа после успешной регистрации
            window.location.href = '/login';
        } catch (error) {
            console.error('Ошибка при регистрации:', error);
            message.error('Ошибка при регистрации');
        } finally {
            setLoading(false);
        }
    };

    return (
        <div className="auth-container">
            <h1>Регистрация</h1>
            <Form
                name="register"
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
                        Зарегистрироваться
                    </Button>
                    Уже есть аккаунт? <Link to="/login">Войдите</Link>
                </Form.Item>
            </Form>
        </div>
    );
};

export default RegisterForm;
