import axios from 'axios';

export const login = async (values) => {

    try {
        const config = {
            headers: {
                'Content-Type': 'application/json',
                },
            };

        const body = JSON.stringify(values)
        const res = await axios.post("http://localhost:8687/api/login/", body, config);
        return res.data;
    } catch (err) {
        throw err.response.data;
    }
};

