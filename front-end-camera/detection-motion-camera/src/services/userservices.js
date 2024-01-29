import axios from './customize-axios';

const fetchAllusers = () => {
    return axios.get("/api/users");
}
//User

const postCreateUser = (fullname, userName, password, isactive) => {
    return axios.post("/api/users/GetUser", { fullname, userName, password, isactive })
}


//Camera
const postCreateCamera = (cameraName, userName, ip, port, status) => {
    return axios.post("/api/users/GetUser", { cameraName, userName, ip, port, status })
}

const putUpdateCamera = (cameraName, userName, ip, port, status) => {
    return axios.put("/api/users", { cameraName, userName, ip, port, status })
}

const Deletecameras = (id) => {
    return axios.delete(`/api/users/${id}`);
}

const LoginApi = (username, password) => {
    return axios.post("/api/login", { username, password });
}

const RegisApi = (full_name, userName, password) => {
    return axios.post("api/register", { full_name, userName, password })
}

export { fetchAllusers, postCreateCamera, putUpdateCamera, Deletecameras, LoginApi, RegisApi, postCreateUser };