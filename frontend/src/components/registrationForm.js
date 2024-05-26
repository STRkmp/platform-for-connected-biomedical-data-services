import React, { useState } from 'react';
import { Form, Input, Button, message } from 'antd';
import axios from 'axios';
import { Link } from 'react-router-dom'; // Импорт useHistory
import './AuthForms.css'; // Импорт стилей

const RegisterForm = () => {
    const [loading, setLoading] = useState(false);

    const onFinish = async (values) => {
        try {
            setLoading(true);
            // Проверяем совпадение паролей
            if (values.password !== values.repeatPassword) {
                message.error('Пароли не совпадают');
                setLoading(false);
                return;
            }
            // Удаляем поле repeatPassword из данных перед отправкой на сервер
            const { repeatPassword, ...requestData } = values;
            // Отправить данные на сервер для регистрации

            console.log(requestData)
            const response = await axios.post('http://localhost:8687/api/register/', requestData);
            console.log('Успешная регистрация:', response.data);
            message.success('Регистрация успешна');
            // Перенаправляем пользователя на страницу входа после успешной регистрации
            window.location.href = '/';
        } catch (error) {
            console.error('Ошибка при регистрации:', error);
            message.error('Ошибка при регистрации', error);
        } finally {
            setLoading(false);
        }
    };

    return (
        <div className="auth-container">

            <Form
                name="register"
                initialValues={{remember: true}}
                onFinish={onFinish}
                className="auth-form"
            >
                <h1>Регистрация</h1>
                <Form.Item
                    name="username"
                    rules={[{required: true, message: 'Введите имя пользователя'}]}
                >
                    <Input placeholder="Имя пользователя"/>
                </Form.Item>

                <Form.Item
                    name="password"
                    rules={[{required: true, message: 'Введите пароль'}]}
                >
                    <Input.Password placeholder="Пароль"/>
                </Form.Item>

                <Form.Item
                    name="repeatPassword"
                    dependencies={['password']}
                    hasFeedback
                    rules={[
                        {required: true, message: 'Повторите пароль'},
                        ({getFieldValue}) => ({
                            validator(_, value) {
                                if (!value || getFieldValue('password') === value) {
                                    return Promise.resolve();
                                }
                                return Promise.reject('Пароли не совпадают');
                            },
                        }),
                    ]}
                >
                    <Input.Password placeholder="Повторите пароль"/>
                </Form.Item>

                <Form.Item
                    name="email"
                    rules={[{required: true, message: 'Введите email'}]}
                >
                    <Input type="email" placeholder="Email"/>
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
