import axios from './customize-axios';

//User
const fetchAllusers = () => {
    return axios.get("/api/users/GetUser");
}

const postCreateUser = (full_name, user_name, password, isactive) => {
    return axios.post("/api/users/EditUser", { full_name, user_name, password, isactive })
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