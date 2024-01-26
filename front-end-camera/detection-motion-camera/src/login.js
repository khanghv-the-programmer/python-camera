import React from "react";
import "./css/login.css";
import Headers from './components/header';
import Footers from './components/footer';
export default function logins() {
    return (
        // <div className="box">

        //     <div className="overlap-2">
        //         <div className="text-wrapper-3">Hello, welcome back</div>
        //         <p className="p">Log in with your data that you entered during your registration </p>
        //         <div className="overlap-3">
        //             <p className="text-wrapper-5">Don't have an account ?</p><div className="text-wrapper-6">Sign up</div>
        //         </div>
        //         <div className="rectangle" /> <div className="rectangle-2" />
        //         <div className="text-wrapper-7">Username</div>
        //         <div className="text-wrapper-8">Password</div>
        //         <div className="text-wrapper-9">Forgot password</div>
        //         <div className="div-wrapper">
        //             <div className="text-wrapper-10">Sign in</div>
        //         </div>
        //         <div className="overlap-4">
        //             <div className="text-wrapper-11">Welcome To Our Website</div>
        //         </div>

        //     </div>
        // </div>
        <div className="box">
            <Headers />
            <img className="login-form-left" alt="Bg" src={process.env.PUBLIC_URL + '/bg_login1.png'} />
            <img className="login-form-right" alt="Bg" src={process.env.PUBLIC_URL + '/bg_login2.png'} />

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
                    <div className="col-12">
                        <span className="forgot-password">Forgot your password?</span>
                    </div>
                </div>
            </div>

            <Footers />
        </div>
    );
}