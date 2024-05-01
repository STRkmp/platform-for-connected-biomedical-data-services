import { Avatar, Typography } from 'antd';
import { Row, Col } from 'antd';

const { Title, Text } = Typography;

const ProfilePage = () => {
    return (
        <div className='profile-page' style={{ display: 'flex', alignItems: 'center', flexDirection: 'column', padding: '24px' }}>
            <Row style={{width: '-webkit-fill-available'}} justify="start" align="middle" gutter={[16, 16]}>
                <Col flex={1} style={{ display: 'flex', alignItems: 'center' }}>
            <Avatar size={128} src="https://i.pravatar.cc/300" />
                </Col>
                <Col flex={4}>
            {/*<Title level={2} style={{ marginTop: '24px' }}>Имя пользователя</Title>*/}
                    <Typography.Title level={2} style={{ marginTop: '1rem', marginBottom: 0 }}>Имя пользователя</Typography.Title>

                    <Typography.Paragraph style={{ marginTop: 0 }}>example@example.com</Typography.Paragraph>
                    <Typography.Paragraph>Организация</Typography.Paragraph>
            {/*<Text strong style={{ marginTop: '8px' }}>Электронная почта:</Text>*/}
            {/*<Text>example@mail.com</Text>*/}
            {/*<Text strong style={{ marginTop: '8px' }}>Организация:</Text>*/}
            {/*<Text>Название организации</Text>*/}
                </Col>
            </Row>
        </div>
    );
};

export default ProfilePage;
