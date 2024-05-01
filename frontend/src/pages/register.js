import { Form, Input, Button } from 'antd';
import React, { useState } from "react";

import { useNavigate } from 'react-router-dom';
import { register } from '../api/auth/register';


import './registration.css'
const layout = {
    wrapperCol: { span: 16 },

};

const RegistrationPage = () => {
    const navigate = useNavigate();
    const [form] = Form.useForm();
    const [loading, setLoading] = useState(false);


    const onFinish = async (values) => {
        setLoading(true)

        register(values)
            .then((data) => {
                // Обработка успешного ответа
                setLoading(false)
                navigate('/');
            })
            .catch((error) => {
                // Обработка ошибки
                console.error(error);
                this.setState({ error: 'Registration failed. Please try again.' });
            });

    };

    const onFinishFailed = (errorInfo) => {
        console.log('Failed:', errorInfo);
    };

    return (
        <div className='registration-page'>
            <Form
                {...layout}
                form={form}
                name="register"
                initialValues={{ remember: true }}
                onFinish={onFinish}
                onFinishFailed={onFinishFailed}
                style={{ display: 'flex', flexDirection: 'column', width: '100%' }}
            >
                <Form.Item
                    label="Username"
                    name="username"
                    rules={[{ required: true, message: 'Please input your username!' }]}
                    style={{ marginBottom: '12px', width: '50%' }}
                >
                    <Input />
                </Form.Item>

                <Form.Item
                    name="email"
                    label="E-mail"
                    rules={[
                        {
                            type: 'email',
                            message: 'The input is not valid E-mail!',
                        },
                        {
                            required: true,
                            message: 'Please input your E-mail!',
                        },
                    ]}
                >
                    <Input />
                </Form.Item>

                <Form.Item
                    label="Пароль"
                    name="password"
                    hasFeedback
                    rules={[{ required: true, message: 'Please input your password!' }]}
                    style={{ marginBottom: '12px', width: '50%'}}
                >
                    <Input.Password />
                </Form.Item>

                <Form.Item
                    name="confirm"
                    label="Confirm Password"
                    dependencies={['password']}
                    hasFeedback
                    rules={[
                        {
                            required: true,
                            message: 'Please confirm your password!',
                        },
                        ({ getFieldValue }) => ({
                            validator(_, value) {
                                if (!value || getFieldValue('password') === value) {
                                    return Promise.resolve();
                                }

                                return Promise.reject(
                                    new Error('The two passwords that you entered do not match!')
                                );
                            },
                        }),
                    ]}
                >
                    <Input.Password />
                </Form.Item>

                <Form.Item wrapperCol={{ span: 16 }} style={{width: '50%'}}>
                    <Button type="primary" htmlType="submit" loading={loading}>
                        Submit
                    </Button>
                </Form.Item>
            </Form>
        </div>
    );
};

export default RegistrationPage;
