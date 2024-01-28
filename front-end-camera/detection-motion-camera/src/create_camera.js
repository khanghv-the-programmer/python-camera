
import Button from 'react-bootstrap/Button';
import Modal from 'react-bootstrap/Modal';
import React, { useState, useEffect } from 'react';
import { postCreateCamera } from './services/userservices';
import { toast } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';

export default function Createcameras(props) {
    const { show, handleClose, handleUpdateCamera } = props;
    const [cameraName, setCameraName] = useState('');
    const [userName, setUserName] = useState('');
    const [ip, setIp] = useState('');
    const [port, setPort] = useState('');
    const [status, setStatus] = useState('');

    const handleSaveCamera = async () => {
        let res = await postCreateCamera(cameraName, ip, userName, ip, port, status);

        // Check if res.id is undefined or null, then set it to 1
        if (!res.id) {
            res.id = 1;
        }
        // Reset fields and perform other actions
        if (res && res.id) {
            handleClose();
            setCameraName('');
            setUserName('');
            setIp('');
            setPort('');
            setStatus('');
            toast.success("Create a camera succeed!");

            // Test API Update
            handleUpdateCamera({
                name_camera: cameraName,
                user_name_camera: userName,
                id: res.id,
                ip_camera: ip,
                port_camera: port,
                status_camera: status
            });
        } else {
            // Error
            toast.error("Cannot create a camera!");
        }
        console.log(res);
    };
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
    useEffect(() => {
        setUserName(props.userName);
    }, [props.userName]);
    
    return (
        <div
            className="modal show"
            style={{ display: 'block', position: 'initial' }}
        >
            <Modal show={show} onHide={handleClose}>
                <Modal.Header closeButton>
                    <Modal.Title>Add New Camera</Modal.Title>
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
                    <Button variant="primary" onClick={() => handleSaveCamera()}>
                        Add New
                    </Button>
                </Modal.Footer>
            </Modal>
        </div>
    );

}
