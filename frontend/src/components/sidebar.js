import React, { useState, useEffect } from 'react';
import { Layout, Menu, Tooltip } from 'antd';
import { HeartOutlined, CloudOutlined } from '@ant-design/icons';
import axios from 'axios';
import Cookies from 'js-cookie';

const { Sider } = Layout;

const Sidebar = ({ handleMenuClick }) => {
    const [collapsed, setCollapsed] = useState(false);
    const [items, setItems] = useState([]);

    useEffect(() => {
        fetchData();
    }, []);

    const onCollapse = (collapsed) => {
        setCollapsed(collapsed);
    };

    const fetchData = async () => {
        try {
            const token = Cookies.get('token');
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

    const getMenuItemIcon = (name) => {
        switch (name) {
            case 'processing_model_sugar':
                return <HeartOutlined />;
            case 'processing_model1':
                return <CloudOutlined />;
            default:
                return null;
        }
    };

    return (
        <Sider collapsible collapsed={collapsed} onCollapse={onCollapse}>
            <div className="logo" />
            <Menu theme="dark" mode="inline" onSelect={handleMenuClick}>
                {items.map(item => (
                    <Menu.Item key={item.id} icon={getMenuItemIcon(item.name)}>
                        <Tooltip title={item.description} placement="right">
                            <span>{item.short_name}</span>
                        </Tooltip>
                    </Menu.Item>
                ))}
            </Menu>
        </Sider>
    );
};

export default Sidebar;