
import Button from 'react-bootstrap/Button';
import Modal from 'react-bootstrap/Modal';
import React, { useState } from 'react';
import { postCreateUser } from './services/userservices';
import { toast } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';

export default function Createusers(props) {
    const { show, handleClose, handleUpdateUser } = props;
    const [fullname, setFullname] = useState('');
    const [username, setUserName] = useState('');
    const [password, setPassword] = useState('');
    const [isactive, setisactive] = useState(false);

    const handleSaveUser = async () => {
        try {
            let res = await postCreateUser(fullname, username, password, isactive);
            console.log("check log", res);

            if (res ) {
                handleClose();
                toast.success("Create a user succeed!");
                // Test API Update
                // handleUpdateUser({
                //     id: res.id,
                //     full_name: fullname,
                //     user_name: username,
                //     user_password: password,
                //     status_user: isactive
                // });
            } else {
                // Error
                toast.error("Cannot create a user!");
            }
        } catch (error) {
            toast.success("Create a user succeed!");
            // Handle error as needed
            toast.error("Error creating user!");
        }
    };
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
                    <form>
                        <div className="mb-3">
                            <label htmlFor="exampleInputEmail1" className="form-label">Name of user</label>
                            <input type="text" className="form-control" id="exampleInputEmail1" value={fullname} onChange={(e) => setFullname(e.target.value)} />
                        </div>
                        <div className="mb-3">
                            <label htmlFor="exampleInputUsername" className="form-label">Username</label>
                            <input type="text" className="form-control" id="exampleInputUsername" value={username} onChange={(e) => setUserName(e.target.value)} />
                        </div>
                        <div className="mb-3">
                            <label htmlFor="exampleInputPort" className="form-label">Password</label>
                            <input type="password" className="form-control" id="exampleInputPort" value={password} onChange={(e) => setPassword(e.target.value)} />
                        </div>
                        <div className="mb-3">
                            <label htmlFor="exampleInputActive" className="form-label">Active</label>
                            <br></br>
                            <input
                                type="checkbox"
                                className="form-check-input"
                                id="exampleInputActive"
                                checked={isactive}
                                onChange={() => setisactive(!isactive)}
                            />
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
