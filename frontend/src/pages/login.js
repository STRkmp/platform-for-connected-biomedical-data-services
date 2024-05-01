import { Form, Input, Button } from 'antd';
import { useNavigate } from 'react-router-dom';
import { message } from 'antd';
import Cookies from 'js-cookie';

import './login.css'
import {login} from "../api/auth/login";
const layout = {
    wrapperCol: { span: 16 },

};

const LoginPage = () => {
    const navigate = useNavigate();
    const onFinish = (values) => {
        login(values)
            .then((data) => {
                if (data.status === 'success') {
                    Cookies.set('token', data.refresh, { expires: 7 }); // expires: 7 - куки будут жить 7 дней
                    // localStorage.setItem('token', data.refresh);
                    navigate('/');
                } else
                    message.error('Пользователь не найден в базе')


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
        <div className='login-page'>
            <Form
                {...layout}
                name="login-form"
                initialValues={{ remember: true }}
                onFinish={onFinish}
                onFinishFailed={onFinishFailed}
                style={{ display: 'flex', flexDirection: 'column', width: '100%' }}
            >
                <Form.Item
                    label="Ты кто?"
                    name="username"
                    rules={[{ required: true, message: 'Please input your username!' }]}
                    style={{ marginBottom: '12px', width: '50%' }}
                >
                    <Input />
                </Form.Item>

                <Form.Item
                    label="Пароль"
                    name="password"
                    rules={[{ required: true, message: 'Please input your password!' }]}
                    style={{ marginBottom: '12px', width: '50%'}}
                >
                    <Input.Password />
                </Form.Item>

                <Form.Item wrapperCol={{ span: 16 }} style={{width: '50%'}}>
                    <Button type="primary" htmlType="submit">
                        Submit
                    </Button>
                </Form.Item>
            </Form>
        </div>
    );
};

export default LoginPage;
