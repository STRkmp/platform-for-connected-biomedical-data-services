import React from 'react';
import axios from 'axios';
import { Form, Button, Upload, message, Typography } from 'antd';
import { UploadOutlined } from '@ant-design/icons';
import Cookies from "js-cookie";

const { Title } = Typography;

const RequestForm = ({ itemId, update }) => {

    const handleSubmit = async (values) => {
        try {
            console.log(itemId)
            console.log(values);
            const formData = new FormData();
            formData.append('file', values.file.file); // Добавляем файл в FormData
            console.log(formData);
            const token = Cookies.get('token');
            const config = {
                headers: {
                    'Authorization': `Token ${token}`,
                    'Content-Type': 'multipart/form-data',
                    'Service-id': itemId.key
                },
            };

            const response = await axios.post('http://localhost:8687/api/request/', formData, config);
            console.log('Успешный ответ:', response.data);
            message.success('Запрос успешно отправлен');
            update(itemId);
        } catch (error) {
            console.error('Ошибка при отправке запроса:', error);
            message.error('Ошибка при отправке запроса');
        }
    };

    // Функция перед отправкой файла, чтобы предотвратить фактическую загрузку на сервер
    const beforeUpload = (file) => {
        return false; // Отменяем загрузку
    };

    return (
        <div style={styles.container}>
            <Title level={3} style={styles.title}>Создание запроса на распознавание</Title>
            <Form layout="vertical" onFinish={handleSubmit}>
                <Form.Item label="Файл" name="file" rules={[{ required: true, message: 'Загрузите файл' }]}>
                    <Upload beforeUpload={beforeUpload} maxCount={1}>
                        <Button icon={<UploadOutlined />}>Выбрать файл</Button>
                    </Upload>
                </Form.Item>
                <Form.Item>
                    <Button type="primary" htmlType="submit">Отправить</Button>
                </Form.Item>
            </Form>
        </div>
    );
};

const styles = {
    container: {
        border: '1px solid #d9d9d9',
        borderRadius: '8px',
        padding: '16px',
        boxShadow: '0 2px 8px rgba(0, 0, 0, 0.1)',
        backgroundColor: '#fff',
        marginBottom: '16px'
    },
    title: {
        marginBottom: '24px',
        textAlign: 'center'
    }
};

export default RequestForm;