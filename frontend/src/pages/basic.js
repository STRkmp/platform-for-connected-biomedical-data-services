import { Layout, Button } from 'antd';
import '../App.css'
import withAuth from '../components/check_auth'
import {useNavigate} from 'react-router-dom';
import Cookies from 'js-cookie';
import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import {BugOutlined} from "@ant-design/icons";
import Sidebar from "../components/sidebar"
import './basic.css'
import axios from "axios";
import RequestForm from '../components/requestForm'; // Импорт компонента для отправки запросов
import RequestList from "../components/requestList";

const { Header, Content } = Layout;


const BasicPage = (props) => {
    const navigate = useNavigate();
    const [selectedItem, setSelectedItem] = useState(null);
    const [requests, setRequests] = useState([]);

    const handleLogout = () => {
        Cookies.remove('token');
            navigate('/start')
    };

    const handleMenuClick = async (item) => {
    try {
        setSelectedItem(item);
        console.log("Получаю список запросов:", selectedItem)
        const token = Cookies.get('token')
        const config = {
            headers: {
            Authorization: `Token ${token}`,
            'Service-id': item.key
        },
        };
        // Вызываем метод для получения списка запросов с использованием item.id
        const response = await axios.get(`http://localhost:8687/api/requests/`, config);
        setRequests(response.data);
        } catch (error) {
        console.error('Ошибка при получении списка запросов:', error);
    }
};
const handleDownloadResult = async (resultFile) => {
    try {
        const token = Cookies.get('token');
        const config = {
            headers: {
                Authorization: `Token ${token}`,
                'File-id': resultFile
            },
            responseType: 'blob', // Указываем тип ответа как blob (двоичный объект)
        };

        // Отправляем GET-запрос на сервер для скачивания файла
        const response = await axios.get(`http://localhost:8687/api/file/`, config);
        console.log(response)
        // Пытаемся получить имя файла из заголовка Content-Disposition
        const contentDispositionHeader = response.headers['content-disposition'];
        const fileNameRegex = /filename[^;=\n]*=((['"]).*?\2|[^;\n]*)/;
        const matches = fileNameRegex.exec(contentDispositionHeader);
        const fileName = matches && matches[1] ? matches[1].replace(/['"]/g, '') : 'file'; // Получаем имя файла

        // Создаем ссылку для скачивания файла
        const url = window.URL.createObjectURL(new Blob([response.data]));

        // Создаем ссылку для скачивания файла с указанием имени файла
        const link = document.createElement('a');
        link.href = url;
        link.setAttribute('download', fileName); // Устанавливаем имя файла
        document.body.appendChild(link);

        // Нажимаем на ссылку, чтобы начать скачивание файла
        link.click();

        // Очищаем ссылку после скачивания файла
        URL.revokeObjectURL(url);
    } catch (error) {
        console.error('Ошибка при скачивании файла:', error);
    }
};


    return (
        <>
            <Header className="header">
                <div className='logo'>
                    <Link to='/' className="profile-button" style={{color: 'white'}}>
                        <BugOutlined />
                    </Link>
                </div>

                <div className='controller'>
                    <Button type="primary" key='unlogin' onClick={handleLogout}>Выйти</Button>
                </div>

            </Header>
            <Layout className='main' style={{minHeight: '100%', minWidth: '30%'}}>
                <Sidebar handleMenuClick={handleMenuClick}/>

                <Layout>
                    {selectedItem && (
                        <>
                            <Layout.Content>
                                <RequestForm itemId={selectedItem} update={handleMenuClick}/>
                            </Layout.Content>
                            <Layout.Content>
                                <RequestList requests={requests} handleDownloadResult={handleDownloadResult} />
                            </Layout.Content>
                        </>
                    )}
                </Layout>
            </Layout>
        </>
    );
}

export default withAuth(BasicPage);
