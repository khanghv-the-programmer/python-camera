// import { Link } from 'react-router-dom';
import Headers from './components/header';
import Footers from './components/footer';
import "./css/home.css";
import React from 'react';

function App() {

  return (
    <div className="box">
      <Headers />
      <img className="img" alt="Bg" src={process.env.PUBLIC_URL + '/bg1_home.png'} />
      <div className="text-wrapper">CAMERA DETECT MOTION</div>
      <p className="your-life-your">
        Your Life - Your Moments <br />- Our Camera Magic -
      </p>
      <img className="bg-img" alt="Img" src={process.env.PUBLIC_URL + '/bg2_home.png'} />
      <Footers />
    </div>

  );
}

export default App;
