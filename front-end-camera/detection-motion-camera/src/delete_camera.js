import Button from 'react-bootstrap/Button';
import Modal from 'react-bootstrap/Modal';
import 'react-toastify/dist/ReactToastify.css';
// import { Deletecameras } from '../src/services/userservices';
import { toast } from 'react-toastify';

export default function Deletecamera(props) {
    const { show, handleClose, dataCameraDelete,handelDeleteCameraFromModal } = props;

   
    return (
        <div
            className="modal show"
            style={{ display: 'block', position: 'initial' }}
        >
            <Modal show={show} onHide={handleClose}>
                <Modal.Header closeButton>
                    <Modal.Title>Delete a camera</Modal.Title>
                </Modal.Header>
                <Modal.Body>
                    <div>
                        Do you want to delete this camera, user= {dataCameraDelete.user_name_camera} ?
                    </div>
                </Modal.Body>
                <Modal.Footer>
                    <Button variant="secondary" onClick={handleClose}>
                        Close
                    </Button>
                    <Button variant="primary">
                        Confirm
                    </Button>
                </Modal.Footer>
            </Modal>
        </div>
    );

}

