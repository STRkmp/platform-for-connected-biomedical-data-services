import React, { useState, useEffect } from 'react';
import { Layout, Menu } from 'antd';
import { UserOutlined, VideoCameraOutlined, UploadOutlined } from '@ant-design/icons';
import axios from 'axios';
import Cookies from "js-cookie";

const { Sider } = Layout;

const Sidebar = ({ handleMenuClick }) => {
    const [collapsed, setCollapsed] = useState(true);
    const [items, setItems] = useState([]);

    useEffect(() => {
        fetchData();
    }, []);

    const onCollapse = (collapsed) => {
        setCollapsed(collapsed);
    };

    const fetchData = async () => {
        try {
            const token = Cookies.get('token')
            const config = {
                headers: {
                Authorization: `Token ${token}`,
            },
            };
            const response = await axios.get('http://localhost:8687/api/processing_services/', config);
            setItems(response.data);
            console.log(response.data)
        } catch (error) {
            console.error('Ошибка при получении данных:', error);
        }
    };

    return (
        <Sider>
            <div className="logo" />
            <Menu theme="dark" mode="inline" onSelect={handleMenuClick}>
                {items.map(item => (
                    <Menu.Item key={item.id} >{item.name}</Menu.Item>
                ))}
            </Menu>
        </Sider>
    );
};

export default Sidebar;