import axios from './customize-axios';

//User
const fetchAllusers = () => {
    return axios.get("/api/users/GetUser");
}

const postCreateUser = (full_name, user_name, password, isactive) => {
    return axios.post("/api/users/EditUser", { full_name, user_name, password, isactive })
}
//Camera
const postCreateCamera = (name, username, password, ip, port) => {
    return axios.post("/api/cameras/EditCameras", { "name":name, "username":username, "password":password, "ip":ip, "port":port})
}

const putUpdateCamera = (cameraName, userName, ip, port, status) => {
    return axios.put("/api/users", { cameraName, userName, ip, port, status })
}

const Deletecamera = (camera) => {
    console.log("camera",camera);
    return axios.delete(`/api/cameras/EditCameras`,{"id":camera});
}

const LoginApi = (username) => {
    return axios.post("/api/users/GetUser", { "user_name":username });
}

const RegisApi = (full_name, userName, password) => {
    return axios.post("api/users/EditUser", { "user_name":userName, "password":password,"full_name":full_name })
}

const getCamera = () => {
    return axios.get("/api/cameras/GetCamera");
}

const getThumbnail = (id) => {
    return axios.post("/api/cameras/GetLastestCapture",{"id":id});
}

const getEvent = (id,From,To) => {
    return axios.post("/api/cameras/GetCapture",{id,From,To});
}


export { fetchAllusers, postCreateCamera, putUpdateCamera, Deletecamera, LoginApi, RegisApi, postCreateUser,getCamera,getEvent, getThumbnail };