import React, { useState } from 'react';
import { Layout, Menu, Button } from 'antd';
import { UploadOutlined, UserOutlined, VideoCameraOutlined, SettingOutlined } from '@ant-design/icons';

const { Sider } = Layout;

// после регистрации есть вкладка добавить
const Sidebar = () => {
    const [collapsed, setCollapsed] = useState(false);

    const onCollapse = (collapsed) => {
        setCollapsed(collapsed);
    };

    return (
        <Sider collapsible collapsed={collapsed} onCollapse={onCollapse}>
            <div className="logo" />
            <Menu theme="dark" defaultSelectedKeys={['1']} mode="inline">

                <Menu.ItemGroup title="Легкие">
                    <Menu.Item icon={<UserOutlined />} key="unhomogen">Негомогенность</Menu.Item>
                    <Menu.Item icon={<VideoCameraOutlined />} key="mass">Узлы</Menu.Item>
                    <Menu.Item icon={<UploadOutlined />} key="pneumonia">Пневмония</Menu.Item>
                </Menu.ItemGroup>

            </Menu>
        </Sider>
    );
};


export default Sidebar;
