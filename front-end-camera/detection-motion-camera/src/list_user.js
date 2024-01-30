import React from "react";
import "./css/login.css";
import Table from 'react-bootstrap/Table';
import Button from 'react-bootstrap/Button';
import Headers from './components/header';
import Footers from './components/footer';
import Createusers from "./create_user";
import { fetchAllusers,RegisApi } from "./services/userservices";
import { useEffect, useState } from "react";
import { ToastContainer } from 'react-toastify';
import Axios from 'axios';
import 'react-toastify/dist/ReactToastify.css';

export default function ListUser() {
    const [listusers, setlistusers] = useState([]);
    const [isShowModalAddNew, setIsShowModalAddNew] = useState(false);

    const handleClose = () => {
        setIsShowModalAddNew(false);
    }

    const getUsers = async () => {
        try {
            let res = await fetchAllusers();
            console.log("Fetched data:", res.result.items); // Log the fetched data
            if (res && res.result.items) {
                setlistusers(res.result.items);
            }
        } catch (error) {
            console.error("Error fetching users:", error);
        }
    }

    useEffect(() => {
        getUsers();
        
    }, [])

    const handleUpdateUser = async(full_name, userName, password) => {
       await RegisApi(full_name, userName, password)
        // setlistusers([user, ...listusers]);
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
                                    <td>{item.full_name}</td>
                                    <td>{item.username}</td>
                                    <td>{item.password}</td>
                                    <td>{item.isactive ? 'Active' : 'Inactive'}</td>
                                </tr>
                            )
                        })}
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