// import { Link } from 'react-router-dom';
import Headers from './components/header';
import Footers from './components/footer';
import "./css/home.css";
import React, { useEffect } from 'react';
import {useLocation} from 'react-router-dom';
import { useNavigate } from 'react-router-dom';
import {getCamera,getEvent} from './services/userservices';
import { useState } from 'react';

function Welcome_user() {
    // const [user, setUser] = useState(location.state?.name);
    const [camera, setCamera] = useState([]);
    const [images,setImages] = useState([])
    const getCams = async() => {
        let res = await getCamera();
        console.log("cameras", res);
        setCamera(res.result.items);
    }

    const getEvents = async(id = 15,From = new Date("2024-01-29T00:13:00.767Z").toISOString(),To = new Date("2024-01-31T00:13:00.767Z").toISOString()) => {

        let res = await getEvent(id,From,To);
        console.log("events", res);
        setImages(res.listImages);
    }
    useEffect(() => {

        getCams();
        getEvents()
    }, []);

    const location = useLocation();
    // const images = "data:image/png;base64, " + images[0]?.img;
  return (
    <div className="box">
      <Headers />

      <p>WELCOME {location.state?.name}</p>
      <ul>
      {camera.map((item, index) => 
        <li>{item.id} - {item.ip} - {item.name} - {item.username}</li>
      )}
    
      </ul>
      <ul>
      {images.map((item, index) =>
        <li>{item.id} - {item.date}
            <img src={'data:image/png;base64, '+item.img} width={'20%'} height={"auto"}/>
        </li>
        
      )}    
      </ul>
      <Footers />
    </div>

  );
}

export default Welcome_user;
