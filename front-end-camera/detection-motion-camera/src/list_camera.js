import React from "react";
import "./css/login.css";
import Table from 'react-bootstrap/Table';
import Button from 'react-bootstrap/Button';
import Headers from './components/header';
import Footers from './components/footer';
import Createcameras from "./create_camera";
import Updatecameras from "./update_camera";
import { fetchAllusers } from '../src/services/userservices';
import { useEffect, useState } from "react";
import { ToastContainer } from 'react-toastify';
import Deletecameras from "./delete_camera";
import _ from "lodash";
import 'react-toastify/dist/ReactToastify.css';


export default function Listcamera() {
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

    useEffect(() => {
        getCameras();
    }, [])

    const getCameras = async () => {
        let res = await fetchAllusers();
        console.log(res);
        if (res && res.data) {
            setlistcameras(res.data);
        }
    }

    const handleUpdateCamera = (camera) => {
        setlistcameras([camera, ...listcameras]);
    }

    const handleEditCamera = (camera) => {
        setdataCameraEdit(camera);
        setIsShowModalEdit(true);
    }
    const handleDeleteCamera = (camera) => {
        setIsShowModalDelete(true)
        setDataCameraDelete(camera);
    }
    const handelDeleteCameraFromModal = (camera) => {
        let cloneListCamera = _.cloneDeep(listcameras);
        cloneListCamera = cloneListCamera.filter(item => item.id !== camera.id)
        setlistcameras(cloneListCamera);
    }
    return (
        <div>
            <div className="box">
                <Headers />
                <Table striped bordered hover>
                    <thead>
                        <tr>
                            <th>ID Camera</th>
                            <th>Name Camera</th>
                            <th>IP Camera</th>
                            <th>Port Camera</th>
                            <th>Username</th>
                            <th>Status</th>
                            <th>Setting</th>
                        </tr>
                    </thead>
                    <tbody>
                        {listcameras && listcameras.length > 0 && listcameras.map((item, index) => {
                            return (
                                <tr key={`user-${index}`}>
                                    <td className="col-2">{item.id}</td>
                                    <td>{item.name_camera}</td>
                                    <td>{item.ip_camera}</td>
                                    <td>{item.port_camera}</td>
                                    <td>{item.user_name_camera}</td>
                                    <td>{item.status_camera}</td>
                                    <td className="col-3">
                                        <Button variant="success">View</Button>{' '}
                                        <Button variant="secondary"
                                            onClick={() => handleEditCamera(item)}
                                        >Edit camera</Button>{' '}
                                        <Button variant="danger"
                                            onClick={() => handleDeleteCamera(item)}
                                        >Delete</Button>{' '}
                                    </td>
                                </tr>
                            )
                        })
                        }
                    </tbody>
                </Table>
                <Button variant="primary" onClick={() => setIsShowModalAddNew(true)}>Create new camera</Button>

                <Createcameras show={isShowModalAddNew}
                    handleClose={handleClose}
                    handleUpdateCamera={handleUpdateCamera} />

                <Updatecameras
                    show={isShowModalEdit}
                    dataCameraEdit={dataCameraEdit}
                    handleClose={handleClose}
                    handelEditCameraFromModal={handelEditCameraFromModal} />
                <Deletecameras
                    show={isShowModalDelete}
                    handleClose={handleClose}
                    dataCameraDelete={dataCameraDelete}
                    handelDeleteCameraFromModal={handelDeleteCameraFromModal}
                />
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