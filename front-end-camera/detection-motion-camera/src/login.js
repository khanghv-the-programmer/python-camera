import React, { useState } from "react";
import "./css/login.css";
import { LoginApi } from "./services/userservices";
import Headers from './components/header';
import Footers from './components/footer';
import '@fortawesome/fontawesome-free/css/all.css';
import { toast } from "react-toastify";

export default function Logins() {
    const [username, setUsername] = useState("");
    const [password, setPassword] = useState("");
    const [passwordVisible, setPasswordVisible] = useState(false);

    const handleLogin = async () => {
        if (!username || !password) {
            toast.error("Username/password required!");
            return;
        }
        let res = await LoginApi(username, password);
        if (res && res.token) {
            localStorage.setItem("token", res.token)
        }
        console.log("check", res);
    }
    return (
        <div className="box">
            <img className="login-form-left" alt="Bg" src={process.env.PUBLIC_URL + '/bg_login1.png'} />
            <img className="login-form-right" alt="Bg" src={process.env.PUBLIC_URL + '/bg_login2.png'} />
            <Headers />
            <div className="text-wrapper1">Welcome To Our Website</div>
            <div className="login-container">
                <form>
                    <div className="login-content row">
                        <div className="col-12 text-center"> Hello, Welcome back
                        </div>
                        <p className="col-12 text-p" >Log in with your data that you entered during your registration </p>
                        <div className="col-12 form-group login-input">
                            <label>Username</label>
                            <input type="text" className="form-control" placeholder="Enter your username" value={username} onChange={(e) => setUsername(e.target.value)} autoComplete="current-username"></input>
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
                                onClick={() => handleLogin()}>Login</button>
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