import axios from './customize-axios';

const fetchAllusers = () => {
    return axios.get("/api/users?page=1");
}

const postCreateCamera = (cameraName, userName, ip, port, status) => {
    return axios.post("/api/users", { cameraName, userName, ip, port, status })
}

const putUpdateCamera = (cameraName, userName, ip, port, status) => {
    return axios.put("/api/users", { cameraName, userName, ip, port, status })
}

const Deletecameras = (id) => {
    return axios.delete(`/api/users/${id}`);
}
export { fetchAllusers, postCreateCamera,putUpdateCamera, Deletecameras };