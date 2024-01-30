// import { Link } from 'react-router-dom';
import Headers from './components/header';
import Footers from './components/footer';
import "./css/home.css";
import React, { useEffect } from 'react';
import {useLocation} from 'react-router-dom';
import { useNavigate } from 'react-router-dom';
import {getCamera,getEvent} from './services/userservices';
import { useState } from 'react';

function ViewEvent() {
    // const [user, setUser] = useState(location.state?.name);
    const [loading, setLoading] = useState(false);
    const [images,setImages] = useState([])
    // const getCams = async() => {
    //     let res = await getCamera();
    //     console.log("cameras", res);
    //     setCamera(res.result.items);
    // }
    const getEvents = async(id = 15,From = new Date("2024-01-20T00:13:00.767Z").toISOString(),To = new Date("2024-01-31T00:13:00.767Z").toISOString()) => {
        setLoading(true)
        let res = await getEvent(id,From,To);
        console.log("events", res);
        setImages(res.listImages);
        setLoading(false)
    }
   
    
    const location = useLocation();
    const id = location.state?.id;
    useEffect(() => {
        
        getEvents(id)
    }, []);
    // const images = "data:image/png;base64, " + images[0]?.img;
  return (
    <div className="box">
      <Headers />
        {loading ? <div className="loader">LOADING</div>
        :
        <>
      
      <ul>

      {images.length>0?images.map((item, index) =>
        <li>{item.date}<br />
            <img src={'data:image/png;base64, '+item.img} width={'50%'} height={"auto"}/>
        </li>
        
      ):
      <li>There is no event</li>}    
      </ul>
        </>}
     
    </div>

  );
}

export default ViewEvent;
