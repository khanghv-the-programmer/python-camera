import React from 'react';
import ReactDOM from 'react-dom/client';
import 'bootstrap/dist/css/bootstrap.min.css';
import './index.css';
import { BrowserRouter, Routes, Route } from "react-router-dom";
import reportWebVitals from './reportWebVitals';
import App from './home';
import Logins from './login'
import Notfound from "./components/notfound";
import Registers from './register';
import Listcameras from './list_camera';
import Createcameras from './create_camera';
import Updatecameras from './update_camera';
import 'react-toastify/dist/ReactToastify.css';

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <BrowserRouter>
      <Routes>
        <Route path='/' element={<App />}> </Route>
        <Route path="login" element={<Logins />}></Route>
        <Route path="register" element={<Registers />}></Route>
        <Route path="listcameras" element={<Listcameras />}></Route>
        <Route path="listcameras/createcameras" element={<Createcameras />}></Route>
        <Route path="listcameras/updatecameras" element={<Updatecameras />}></Route>
        <Route path="*" element={<Notfound />} />
      </Routes>
    </BrowserRouter>
  </React.StrictMode>
);
reportWebVitals();
