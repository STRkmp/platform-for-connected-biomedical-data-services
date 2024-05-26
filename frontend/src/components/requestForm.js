import React, { useState } from 'react';
import { Form, Button, Upload, message, Input } from 'antd';
import { UploadOutlined } from '@ant-design/icons';
import axios from "axios";
import Cookies from "js-cookie";

const RequestForm = ({ itemId, update }) => {
    const [file, setFile] = useState(null);
    const [complaints, setComplaints] = useState('');

    const handleSubmit = async (values) => {
        try {
            console.log(values);
            const formData = new FormData();
            formData.append('file', values.file.file);
            formData.append('complaints', values.complaints); // Добавление жалоб в formData

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
            update(itemId); // Обновление данных после отправки запроса

            // Сброс файла
            setFile(null);
            setComplaints('')
        } catch (error) {
            console.error('Ошибка при отправке запроса:', error);
            message.error('Ошибка при отправке запроса');
        }
    };

    const beforeUpload = (file) => {
        setFile(file); // Сохранение файла перед загрузкой
        return false; // Отмена загрузки на сервер
    };

    return (
        <div>
            <h3>Создание запроса на распознавание</h3>
            <Form layout="vertical" onFinish={handleSubmit}>
                <Form.Item label="Файл" name="file" rules={[{ required: true, message: 'Загрузите файл' }]}>
                    <Upload beforeUpload={beforeUpload} maxCount={1} fileList={file ? [file] : []}>
                        <Button icon={<UploadOutlined />}>Выбрать файл</Button>
                    </Upload>
                </Form.Item>
                <Form.Item label="Жалобы" name="complaints">
                    <Input.TextArea value={complaints} onChange={(e) => setComplaints(e.target.value)} />
                </Form.Item>
                <Form.Item>
                    <Button type="primary" htmlType="submit">Отправить</Button>
                </Form.Item>
            </Form>
        </div>
    );
};

export default RequestForm;
