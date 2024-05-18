import React, { useState } from 'react';
import { List, Card, Typography, Button, Modal, Input, message } from 'antd';
import axios from 'axios';
import Cookies from 'js-cookie';
import './requestList.css';

const { Text } = Typography;

const RequestList = ({ requests, handleDownloadResult }) => {
    const [isModalVisible, setIsModalVisible] = useState(false);
    const [comment, setComment] = useState('');
    const [currentRequestId, setCurrentRequestId] = useState(null);

    const showFeedbackModal = (requestId) => {
        setCurrentRequestId(requestId);
        setIsModalVisible(true);
    };

    const handleOk = async () => {
        try {
            const token = Cookies.get('token');
            const formData = new FormData();
            formData.append('comment', comment);

            const config = {
                headers: {
                    'Authorization': `Token ${token}`,
                    'Request-id': currentRequestId
                },
            };

            await axios.post('http://localhost:8687/api/feedback/', formData, config);
            message.success('Обратная связь успешно отправлена');
            setIsModalVisible(false);
            setComment('');
        } catch (error) {
            console.error('Ошибка при отправке обратной связи:', error);
            message.error('Ошибка при отправке обратной связи');
        }
    };

    const handleCancel = () => {
        setIsModalVisible(false);
        setComment('');
    };

    return (
        <>
            <List
                grid={{ gutter: 16, column: 1 }}
                dataSource={requests}
                renderItem={request => (
                    <List.Item>
                        <Card
                            title={`Номер запроса: ${request.id}`}
                            extra={<Text type={getStatusColor(request.status)}>{getStatusText(request.status)}</Text>}
                        >
                            <p><strong>Время запроса:</strong> {new Date(request.request_time).toLocaleString()}</p>
                            <p>{request.description}</p>
                            {request.status === 'success' && (
                                <>
                                    <Text className="download-link" onClick={() => handleDownloadResult(request.result_file)} style={{ color: '#1890ff', cursor: 'pointer' }}>Скачать результат</Text>
                                    <Button type="link" onClick={() => showFeedbackModal(request.id)}>Обратная связь</Button>
                                </>
                            )}
                        </Card>
                    </List.Item>
                )}
            />
            <Modal title="Обратная связь" visible={isModalVisible} onOk={handleOk} onCancel={handleCancel}>
                <Input.TextArea value={comment} onChange={(e) => setComment(e.target.value)} rows={4} placeholder="Введите ваш комментарий" />
            </Modal>
        </>
    );
};

const getStatusText = (status) => {
    switch (status) {
        case 'success':
            return 'Успешно';
        case 'error':
            return 'Ошибка';
        case 'created':
            return 'В очереди';
        default:
            return 'Неизвестный статус';
    }
};

const getStatusColor = (status) => {
    switch (status) {
        case 'success':
            return 'success';
        case 'error':
            return 'danger';
        case 'created':
            return 'warning';
        default:
            return 'default';
    }
};

export default RequestList;