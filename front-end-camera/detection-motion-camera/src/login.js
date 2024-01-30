import React, { useState } from "react";
import "./css/login.css";
import { LoginApi } from "./services/userservices";
import Headers from './components/header';
import Footers from './components/footer';
import '@fortawesome/fontawesome-free/css/all.css';
import { toast } from "react-toastify";
import {useLocation} from 'react-router-dom';

import { useNavigate } from "react-router-dom";

export default function Logins() {
    const location = useLocation();
    const navigate = useNavigate();
    const [username, setUsername] = useState("");
    const [password, setPassword] = useState("");
    const [passwordVisible, setPasswordVisible] = useState(false);
    const [auth,setAuth] = useState(false);
    const [send,setSend] = useState(false);
    console.log(location.state?.message)
    const handleLogin = async (e) => {
        e.preventDefault();
        if (!username || !password) {
            toast.error("Username/password requiredee!");
            // console.log("Username/password requiredee!");
            return;
        }
        let res = await LoginApi(username);
        if (res && res.token) {
            localStorage.setItem("token", res.token)
        }
        console.log('res', res.result.items);
        if(res.result.items.length === 0){
           setSend(true)
            return;
        }
        else{
           setSend(true)
            setAuth(true)
        navigate("/listcameras", { state: { name: username } });
        console.log("check", res.result.items);
        }
       
    }

    return (
        <div className="box">
            <img className="login-form-left" alt="Bg" src={process.env.PUBLIC_URL + '/bg_login1.png'} />
            <img className="login-form-right" alt="Bg" src={process.env.PUBLIC_URL + '/bg_login2.png'} />
            <Headers />
            <div className="text-wrapper1">Motion Detector</div>
            <div className="login-container">
                <form>
                    <div className="login-content row">
                        <div className="col-12 text-center"> {location.state?.message ? `${location.state.message}`:'Hello, Welcome back'}
                        </div>
                        {!send && <p className="col-12 text-p" >Log in with your data that you entered during your registration </p>}
                        {send && !auth && <p className="col-12 text-p" >Username or password is incorrect </p>}
                        <div className="col-12 form-group login-input">
                            <label>Username</label>
                            <input type="text" className="form-control" placeholder="Enter your username" value={username} onChange={(e) =>{ console.log(e.target.value);setUsername(e.target.value)}} autoComplete="current-username"></input>
                        </div>
                        <div className="col-12 form-group login-input">
                            <label>Password</label>
                            <input
                                type={passwordVisible ? 'text' : 'password'}
                                className="form-control"
                                placeholder="Enter your password"
                                value={password}
                                onChange={(e) => setPassword(e.target.value)}
                                autoComplete="current-password"
                            />
                            <i
                                className={`fas ${passwordVisible ? 'fa-eye' : 'fa-eye-slash'}`}
                                onClick={() => setPasswordVisible(!passwordVisible)}
                            ></i>
                        </div>
                        <div className="col-12" >
                            <button className="btn-login"
                                onClick={e=>handleLogin(e)}>Login</button>
                        </div>
                    </div>
                </form>
            </div>
            <div className="row">
                <Footers />
            </div>
        </div>
    );
}