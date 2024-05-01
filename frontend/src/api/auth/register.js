import axios from 'axios';

// const url = 'http://localhost:8000/register/';

// const register = (username, email, password) => {
//     return axios.post(url, {
//         username: username,
//         email: email,
//         password: password
//     });
// };
//
// import axios from "axios";

export const register = async (values) => {
    const config = {
        headers: {
            "Content-Type": "application/json",
        },
    };
    const body = JSON.stringify(values);

    try {
        // const res = await axios.post("/api/auth/register/", body, config);
        // const res = await axios.post("http://localhost:8000/health/register/", body, config);
        const res = await axios.post("http://127.0.0.1:8000/health/register/", body, config);
        return res.data;
    } catch (err) {
        throw err.response.data;
    }
};

