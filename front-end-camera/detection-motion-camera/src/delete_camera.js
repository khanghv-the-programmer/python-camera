import Button from 'react-bootstrap/Button';
import Modal from 'react-bootstrap/Modal';
import 'react-toastify/dist/ReactToastify.css';
import { Deletecameras } from '../src/services/userservices'
import { toast } from 'react-toastify';

export default function Deletecamera(props) {
    const { show, handleClose, dataCameraDelete,handelDeleteCameraFromModal } = props;

    const ConfirmDelete = async () => {
        let res = await Deletecameras(dataCameraDelete.id)
        //Vì status trả về kiểu string nên dấu + sẽ có tác dụng convert về int
        if (res && +res.statusCode === 204) {
            toast.success("Delete camera succeed!");
            handleClose();
            handelDeleteCameraFromModal(dataCameraDelete);
        }
        else {
            toast.error("Incomplete delete camera")
        }
    }
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
                    <Button variant="primary" onClick={() => ConfirmDelete()}>
                        Confirm
                    </Button>
                </Modal.Footer>
            </Modal>
        </div>
    );

}

