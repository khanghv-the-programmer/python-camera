
import Button from 'react-bootstrap/Button';
import Modal from 'react-bootstrap/Modal';
import React, { useState, useEffect } from 'react';
import { postCreateUser } from './services/userservices';
import { toast } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';

export default function Createusers(props) {
    const { show, handleClose, handleUpdateUser } = props;
    const [fullname, setFullname] = useState('');
    const [userName, setUserName] = useState('');
    const [password, setPassword] = useState('');
    const [isactive, setisactive] = useState('');

    const handleSaveUser = async () => {
        let res = await postCreateUser(fullname, password, userName, isactive);

        // Check if res.id is undefined or null, then set it to 1
        if (!res.id) {
            res.id = 1;
        }
        // Reset fields and perform other actions
        if (res && res.id) {
            handleClose();
            setFullname('');
            setUserName('');
            setPassword('');
            setisactive('');
            toast.success("Create a user succeed!");

            // Test API Update
            handleUpdateUser({
                full_name: fullname,
                user_name: userName,
                id: res.id,
                user_password: password,
                status_user: isactive
            });
        } else {
            // Error
            toast.error("Cannot create a user!");
        }
        console.log(res);
    };
    const handleSubmit = (e) => {
        e.preventDefault();

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
                    <Modal.Title>Add New User</Modal.Title>
                </Modal.Header>
                <Modal.Body>
                    <form onSubmit={handleSubmit}>
                        <div className="mb-3">
                            <label htmlFor="exampleInputEmail1" className="form-label">Name of user</label>
                            <input type="text" className="form-control" id="exampleInputEmail1" value={fullname} onChange={(e) => setFullname(e.target.value)} />
                        </div>
                        <div className="mb-3">
                            <label htmlFor="exampleInputIP" className="form-label">Username</label>
                            <input type="text" className="form-control" id="exampleInputIP" value={userName} onChange={(e) => setUserName(e.target.value)} />
                        </div>
                        <div className="mb-3">
                            <label htmlFor="exampleInputPort" className="form-label">Password</label>
                            <input type="password" className="form-control" id="exampleInputPort" value={password} onChange={(e) => setPassword(e.target.value)} />
                        </div>
                        <div className="mb-3">
                            <label htmlFor="exampleInputUsername" className="form-label">Active</label>
                            <input type="text" className="form-control" id="exampleInputUsername" value={isactive} onChange={(e) => setisactive(e.target.value)} />
                        </div>
                    </form>
                </Modal.Body>
                <Modal.Footer>
                    <Button variant="secondary" onClick={handleClose}>
                        Close
                    </Button>
                    <Button variant="primary" onClick={() => handleSaveUser()}>
                        Add New
                    </Button>
                </Modal.Footer>
            </Modal>
        </div>
    );

}
