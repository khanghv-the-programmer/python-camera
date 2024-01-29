import "./css/register.css";
import Headers from './components/header';
import Footers from './components/footer';

export default function Register() {
    return (
        <div className="box">
            <img className="login-form-left" alt="Bg" src={process.env.PUBLIC_URL + '/bg_regis1.png'} />
            <img className="login-form-right" alt="Bg" src={process.env.PUBLIC_URL + '/bg_regis2.png'} />
            <Headers />
            <div className="text-wrapper1">Hello, friend</div>
            <div className="text-wrapper2">Fill up personal information and start journey with us</div>
            <div className="register-container">
                <div className="register-content row">
                    <div className="col-12 text-regis"> Create an account
                    </div>
                    <p className="col-12 text-p" >Safeguarding Security Through Visual Surveillance </p>
                    <div className="col-12 col-md-6 form-group register-input">
                        <label>First Name</label>
                        <input type="text" className="form-control" placeholder="Enter your first name" />
                    </div>
                    <div className="col-12 col-md-6 form-group register-input">
                        <label>Last Name</label>
                        <input type="text" className="form-control" placeholder="Enter your last name" />
                    </div>
                    <div className="col-12 form-group register-input">
                        <label>Username</label>
                        <input type="text" className="form-control" placeholder="Enter your username"></input>
                    </div>
                    <div className="col-12 form-group register-input">
                        <label>Password</label>
                        <input type="password" className="form-control" placeholder="Enter your password"></input>
                    </div>
                    <div className="col-12 form-group register-input">
                        <label>Confirm Password</label>
                        <input type="password" className="form-control" placeholder="Enter your re-password"></input>
                    </div>
                    <div className="col-12" >
                        <button className="btn-signup">Sign up</button>
                    </div>
                </div>
            </div>
            <div className="row">
                <Footers />
            </div>
        </div>
    );
}