import axios from 'axios';

export const login = async (values) => {

    try {
        const res = await axios.post("http://localhost:8687/api/login/", values);
        return res.data;
    } catch (err) {
        throw err.response.data;
    }
};

