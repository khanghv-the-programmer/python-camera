import React from "react";
import "./css/login.css";
import Table from 'react-bootstrap/Table';
import Button from 'react-bootstrap/Button';
import Headers from './components/header';
import Footers from './components/footer';
import Createusers from "./create_user";
import { fetchAllusers } from '../src/services/userservices';
import { useEffect, useState } from "react";
import { ToastContainer } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';

export default function ListUser() {
    const [listusers, setlistusers] = useState([]);
    const [isShowModalAddNew, setIsShowModalAddNew] = useState(false);

    const handleClose = () => {
        setIsShowModalAddNew(false);
    }
    const getUsers = async () => {
        let res = await fetchAllusers();
        console.log(res);
        if (res && res.data) {
            setlistusers(res.data);
        }
    }

    useEffect(() => {
        getUsers();
    }, [])

    const handleUpdateUser = (user) => {
        setlistusers([user, ...listusers]);
    }

    return (
        <div>
            <div className="box">
                <Headers />
                <Table striped bordered hover>
                    <thead>
                        <tr>
                            <th>ID</th>
                            <th>Full name</th>
                            <th>Username</th>
                            <th>Password</th>
                            <th>Status</th>

                        </tr>
                    </thead>
                    <tbody>
                        {listusers && listusers.length > 0 && listusers.map((item, index) => {
                            return (
                                <tr key={`user-${index}`}>
                                    <td className="col-2">{item.id}</td>
                                    <td>{item.fullname}</td>
                                    <td>{item.userName}</td>
                                    <td>{item.password}</td>
                                    <td>{item.isactive}</td>

                                </tr>
                            )
                        })
                        }
                    </tbody>
                </Table>
                <Button variant="primary" onClick={() => setIsShowModalAddNew(true)}>Create new user</Button>
                <Createusers show={isShowModalAddNew}
                    handleClose={handleClose}
                    handleUpdateUser={handleUpdateUser} />
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