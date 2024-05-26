import React, { useState } from 'react';
import { List, Card, Typography, Button, Modal, Input, message, Space } from 'antd';
import axios from 'axios';
import Cookies from 'js-cookie';
import './requestList.css';

const { Text } = Typography;

const RequestList = ({ requests, handleDownloadResult }) => {
    const [isModalVisible, setIsModalVisible] = useState(false);
    const [comment, setComment] = useState('');
    const [currentRequestId, setCurrentRequestId] = useState(null);
    const [filter, setFilter] = useState(null);

    const handleFilter = (status) => {
        setFilter(status);
    };

    const filteredRequests = filter ? requests.filter(request => request.status === filter) : requests;


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
            <Space>
                <Button onClick={() => handleFilter('success')}>Успешные</Button>
                <Button onClick={() => handleFilter('created')}>В очереди</Button>
                <Button onClick={() => handleFilter('error')}>Ошибки</Button>
                <Button onClick={() => setFilter(null)}>Сбросить фильтр</Button>
            </Space>
            <List
                className="request-list-container"
                grid={{ gutter: 16, column: 1 }}
                dataSource={filteredRequests.sort((a, b) => b.id - a.id)} // Сортировка по убыванию номеров запросов
                renderItem={request => (
                    <List.Item>
                        <Card
                            title={`Номер запроса: ${request.id}`}
                            extra={<Text type={getStatusColor(request.status)}>{getStatusText(request.status)}</Text>}
                        >
                            {request.complaints && (
                                <p><strong>Жалобы:</strong>{request.complaints}</p>
                            )}
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