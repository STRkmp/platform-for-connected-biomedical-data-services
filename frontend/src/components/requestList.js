import React from 'react';
import './requestList.css'

const RequestList = ({ requests, handleDownloadResult }) => (
    <ul className="request-list">
        {requests.map(request => (
            <li className={`request-item ${getStatusColor(request.status)}`} key={request.id}>
                <h3>Номер запроса: {request.id}</h3>
                <p>Время запроса: {new Date(request.request_time).toLocaleString()}</p>
                <p>{request.description}</p>
                <p className="status">Статус: {getStatusText(request.status)}</p>
                {request.status === 'success' && (
                    <p className="download-link" onClick={() => handleDownloadResult(request.result_file)}>Скачать результат</p>
                )}
            </li>
        ))}
    </ul>
);

const getStatusText = (status) => {
    switch (status) {
        case 'success':
            return 'Успешно';
        case 'error':
            return 'Ошибка';
        case 'sent':
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
            return 'error';
        default:
            return '';
    }
};

export default RequestList;