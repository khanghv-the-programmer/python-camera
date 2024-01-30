
import Button from 'react-bootstrap/Button';
import Modal from 'react-bootstrap/Modal';
import React, { useEffect, useState } from 'react';
import { putUpdateCamera } from '../src/services/userservices';
import { toast } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';

export default function Updatecameras(props) {
    const { show, handleClose, dataCameraEdit, handelEditCameraFromModal } = props;
    const [cameraName, setCameraName] = useState('');
    const [ip, setIp] = useState('');
    const [userName, setUserName] = useState('');
    const [port, setPort] = useState('');
    const [status, setStatus] = useState('');

    // const handleEditCamera = async () => {
    //     try {
    //         let res = await putUpdateCamera(cameraName, ip, userName, port, status);
    //         if (res && res.updatedAt) {
    //             handelEditCameraFromModal({
    //                 id: dataCameraEdit.id,
    //                 name_camera: cameraName,
    //                 ip_camera: ip,
    //                 user_name_camera: userName,
    //                 port_camera: port,
    //                 status_camera: status
    //             });
    //             handleClose();
    //             toast.success("Update camera succeed!");
    //         }

    //     } catch (error) {
    //         console.error('Error updating camera:', error);
    //         toast.error('Error updating camera. Please try again.'); // Use toast to display an error message
    //     }
    // };
    console.log("check", dataCameraEdit);
    
    useEffect(() => {
        if (show) {
            setCameraName(dataCameraEdit.cameraName);
            setUserName(dataCameraEdit.userName);
            setIp(dataCameraEdit.ip);
            setPort(dataCameraEdit.port);
            setStatus(dataCameraEdit.status);
        }
    }, [show, dataCameraEdit]);

    const handleSubmit = (e) => {
        e.preventDefault();

        // Kiểm tra rỗng và định dạng IP và Port
        if (!cameraName || !ip || !port) {
            alert('Please fill in all required fields (Name, IP, Port).');
            return;
        }

        // Kiểm tra định dạng IP
        const ipRegex = /^(\d{1,3}\.){3}\d{1,3}$/;
        if (!ipRegex.test(ip)) {
            alert('Please enter a valid IP address.');
            return;
        }

        // Kiểm tra định dạng Port
        const portRegex = /^\d+$/;
        if (!portRegex.test(port)) {
            alert('Please enter a valid port number.');
            return;
        }


    };
    return (
        <div
            className="modal show"
            style={{ display: 'block', position: 'initial' }}
        >
            <Modal show={show} onHide={handleClose}>
                <Modal.Header closeButton>
                    <Modal.Title>Edit Camera</Modal.Title>
                </Modal.Header>
                <Modal.Body>
                    <form onSubmit={handleSubmit}>
                        <div className="mb-3">
                            <label htmlFor="exampleInputEmail1" className="form-label">Name of camera</label>
                            <input type="text" className="form-control" id="exampleInputEmail1" value={cameraName} onChange={(e) => setCameraName(e.target.value)} />
                        </div>
                        <div className="mb-3">
                            <label htmlFor="exampleInputIP" className="form-label">IP</label>
                            <input type="text" className="form-control" id="exampleInputIP" value={ip} onChange={(e) => setIp(e.target.value)} />
                        </div>
                        <div className="mb-3">
                            <label htmlFor="exampleInputPort" className="form-label">Port</label>
                            <input type="text" className="form-control" id="exampleInputPort" value={port} onChange={(e) => setPort(e.target.value)} />
                        </div>
                        <div className="mb-3">
                            <label htmlFor="exampleInputUsername" className="form-label">Username</label>
                            <input type="text" className="form-control" id="exampleInputUsername" value={userName} onChange={(e) => setUserName(e.target.value)} />
                        </div>
                        <div className="mb-3">
                            <label htmlFor="exampleInputStatus" className="form-label">Status</label>
                            <input type="text" className="form-control" id="exampleInputStatus" value={status} onChange={(e) => setStatus(e.target.value)} />
                        </div>
                    </form>
                </Modal.Body>
                <Modal.Footer>
                    <Button variant="secondary" onClick={handleClose}>
                        Close
                    </Button>
                    {/* <Button variant="primary" onClick={() => handleEditCamera()}>
                        Confirm
                    </Button> */}
                </Modal.Footer>
            </Modal>
        </div>
    );

}
