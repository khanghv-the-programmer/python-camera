import React from "react";
import "./css/login.css";
import Table from 'react-bootstrap/Table';
import Button from 'react-bootstrap/Button';
import Headers from './components/header';
import Footers from './components/footer';
import Createcameras from "./create_camera";
import Updatecameras from "./update_camera";
import { getEvent,getCamera ,postCreateCamera,getThumbnail,Deletecamera } from '../src/services/userservices';
import { useEffect, useState } from "react";
import { ToastContainer } from 'react-toastify';
// import Deletecameras from "./delete_camera";
import _, { truncate } from "lodash";
import 'react-toastify/dist/ReactToastify.css';
import { useNavigate } from "react-router-dom";
import { useLocation } from "react-router-dom";
import e from "cors";


export default function Listcamera() {
    const location = useLocation();
    const navigate = useNavigate();
    if(!location.state?.name ){
        navigate("/login")
    }
    const [images,setImages] = useState([])
    const [loading, setLoading] = useState(false);
    const [isShowModalAddNew, setIsShowModalAddNew] = useState(false);
    const [isShowModalEdit, setIsShowModalEdit] = useState(false);
    const [listcameras, setlistcameras] = useState([]);
    const [dataCameraEdit, setdataCameraEdit] = useState({});
    const [isShowModalDelete, setIsShowModalDelete] = useState(false);
    const [dataCameraDelete, setDataCameraDelete] = useState({});
    
    const handleClose = () => {
        setIsShowModalAddNew(false);
        setIsShowModalEdit(false);
        setIsShowModalDelete(false);
    }

    const handelEditCameraFromModal = (camera) => {
        //trỏ tới 2 địa chỉ khác nhau để nhận biết giá trị cũ thay đổi thành giá trị mới như thế nào
        let cloneListCamera = _.cloneDeep(listcameras);
        let index = listcameras.findIndex(item => item.id === camera.id);
        cloneListCamera[index].name_camera = camera.name_camera;
        setlistcameras(cloneListCamera);
    }
    const getCameras = async () => {
        setLoading(true)
        let res = await getCamera();
        console.log("res at getCameras",res);
        if (res) {
            setlistcameras(res.result.items);
            await getThumbnails()
        }
        console.log("finished")
        setLoading(false)
    }

    // for(let i = 0;i < listcameras.length;i++){
    //     console.log(listcameras[i].id)
    //     let obj = getThumbnails(listcameras[i].id)  
    //     listcameras[i].thumbnail = obj
    // }

   
      
    const getThumbnails = async () => {
        // let res = await getThumbnail(id);
        // console.log("res at getCameras",res);
        await Promise.all(listcameras.map(async(ele)=>{
            let res = await getThumbnail(ele.id)
            console.log('res in map',res)
            return ele.thumbnail = res
        }))
    }

    useEffect(() => {
        getCameras();
    }, [])

   

    const handleUpdateCamera = (camera) => {
        postCreateCamera()
        setlistcameras([camera, ...listcameras]);
    }

    const handleEditCamera = (camera) => {
        setdataCameraEdit(camera);
        setIsShowModalEdit(true);
    }
    const handleDeleteCamera = async(camera) => {
        await Deletecamera(camera)
    }
    const handelDeleteCameraFromModal = (camera) => {
        let cloneListCamera = _.cloneDeep(listcameras);
        cloneListCamera = cloneListCamera.filter(item => item.id !== camera.id)
        setlistcameras(cloneListCamera);
    }

    // const getEvents = async(id = 15,From = new Date("2024-01-29T00:13:00.767Z").toISOString(),To = new Date("2024-01-31T00:13:00.767Z").toISOString()) => {

    //     let res = await getEvent(id,From,To);
    //     console.log("events", res);
    //     setImages(res.listImages);
    // }
    // console.log("listcameras", listcameras)

    const handleView = (id) => {
        
        navigate("/viewEvent",{state:{id:id}})
    }
    console.log("listcameras", listcameras)
    return (
        <div>
            <div className="box">
                <Headers />
                {loading ? <p>LOADING...</p> : 
                <Table striped bordered hover>
                    <thead>
                        <tr>
                            <th>ID Camera</th>
                            <th>Name Camera</th>
                            <th>IP Camera</th>
                            <th>Port Camera</th>
                            <th>Username</th>
                            <th>Status</th>
                            <th></th>
                        </tr>
                    </thead>
                    <tbody>
                        {listcameras && listcameras.length > 0 && listcameras.map((item, index) => {
                            return (
                                <tr key={`user-${index}`}>
                                    <td className="col-2">{item.id}</td>
                                    <td>{item.name}</td>
                                    <td>{item.ip}</td>
                                    <td>{item.port}</td>
                                    <td>{item.username}</td>
                                    <td>{item.is_active?"ON":"OFF"}</td>
                                    <td className="col-3">
                                        <Button variant="success" onClick={e=>handleView(item.id)}>View</Button>{' '}
                                        {/* <Button variant="secondary"
                                            onClick={() => handleEditCamera(item)}
                                        >Edit camera</Button>{' '} */}
                                        {/* <Button variant="danger"
                                            onClick={() => handleDeleteCamera(item.id)}
                                        >Delete</Button>{' '} */}
                                    </td>
                                </tr>
                            )
                        })
                        }
                    </tbody>
                </Table>
                }
                <Button variant="primary" onClick={() => setIsShowModalAddNew(true)}>Create new camera</Button>

                <Createcameras show={isShowModalAddNew}
                    handleClose={handleClose}
                    handleUpdateCamera={handleUpdateCamera} />

                <Updatecameras
                    show={isShowModalEdit}
                    dataCameraEdit={dataCameraEdit}
                    handleClose={handleClose}
                    handelEditCameraFromModal={handelEditCameraFromModal} />
                {/* <Deletecameras
                    show={isShowModalDelete}
                    handleClose={handleClose}
                    dataCameraDelete={dataCameraDelete}
                    handelDeleteCameraFromModal={handelDeleteCameraFromModal}
                /> */}
                <div className="row">
                    <Footers />
                </div>
            </div>
            <ToastContainer
                position="top-right"
                autoClose={3000}
                hideProgressBar={false}
                newestOnTop={false}
                closeOnClick
                rtl={false}
                pauseOnFocusLoss
                draggable
                pauseOnHover
            />
        </div>

    )
};