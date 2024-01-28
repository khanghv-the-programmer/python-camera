import React from "react";
import "./css/login.css";
import Headers from './components/header';
import Footers from './components/footer';

export default function logins() {
    return (
        <div className="box">

            <img className="login-form-left" alt="Bg" src={process.env.PUBLIC_URL + '/bg_login1.png'} />
            <img className="login-form-right" alt="Bg" src={process.env.PUBLIC_URL + '/bg_login2.png'} />
            <Headers />
            <div className="text-wrapper1">Welcome To Our Website</div>
            <div className="login-container">

                <div className="login-content row">
                    <div className="col-12 text-center"> Hello, Welcome back
                    </div>
                    <p className="col-12 text-p" >Log in with your data that you entered during your registration </p>
                    <div className="col-12 form-group login-input">
                        <label>Username</label>
                        <input type="text" className="form-control" placeholder="Enter your username"></input>
                    </div>
                    <div className="col-12 form-group login-input">
                        <label>Password</label>
                        <input type="password" className="form-control" placeholder="Enter your password"></input>

                    </div>
                    <div className="col-12" >
                        <button className="btn-login">Login</button>
                    </div>
                </div>
            </div>
            <div className="row">
                <Footers />
            </div>
        </div>
    );
}