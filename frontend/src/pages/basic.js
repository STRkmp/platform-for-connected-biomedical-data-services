import { Layout, Button } from 'antd';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import '../App.css';
import withAuth from '../components/check_auth'
import {useNavigate} from 'react-router-dom';
import Cookies from 'js-cookie';

import { Link } from 'react-router-dom';
import Sidebar from '../components/sidebar'
import {UserOutlined, BugOutlined} from "@ant-design/icons";

import './basic.css'
import LandingPage from "./start";


// import {FontAwesomeIcon} from "@fortawesome/react-fontawesome";


const { Header, Content } = Layout;

const BasicPage = (props) => {
    const navigate = useNavigate();
    const handleLogout = () => {
        // if (localStorage.getItem('token')){
        Cookies.remove('token');

        //     localStorage.removeItem('token');
            navigate('/start')
        // }

    };

    return (
        <>
            {/*{Cookies.get('token')} ?*/}
            <Header className="header">
                <div className='logo'>
                    <Link to='/' className="profile-button" style={{color: 'white'}}>
                        <BugOutlined />
                    </Link>
                </div>

                <div className='controller'>
                    <Link to='/profile' className="profile-button" style={{color: 'white'}}>
                        <UserOutlined />
                    </Link>
                    {/*<Link to='/'>*/}
                    <Button type="primary" key='login' onClick={handleLogout}>Выйти</Button>
                    {/*</Link>*/}
                </div>

            </Header>
            <Layout className='main'>
                <Sidebar />

                <Layout style={{ padding: '0 24px 24px' }}>
                    <Content
                        className="site-layout-background"
                        style={{
                            padding: 24,
                            margin: 0,
                            minHeight: 280,
                        }}
                    >
                        <div className="upload-container">
                            {/*{<DicomViewer file='C:\Users\stepa\Downloads\2_skull_ct\DICOM\l0' />}*/}
                            {props.component}
                        </div>
                    </Content>
                </Layout>
            </Layout>
            {/*{navigate('/start')}*/}
        </>
    );
}

export default withAuth(BasicPage);
