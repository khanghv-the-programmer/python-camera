import Container from 'react-bootstrap/Container';
import Nav from 'react-bootstrap/Nav';
import Navbar from 'react-bootstrap/Navbar';
import NavDropdown from 'react-bootstrap/NavDropdown';
import { NavLink } from 'react-router-dom';
export default function Headers() {


    return (
        <Navbar expand="lg" className="bg-body-tertiary" bg="dark" data-bs-theme="dark" >
            <Container>
                <Navbar.Brand>
                    <NavLink to="/" className="nav-link">SafetyGuardCamera</NavLink>
                </Navbar.Brand>
                <Navbar.Toggle aria-controls="basic-navbar-nav" />
                <Navbar.Collapse id="basic-navbar-nav">
                    <Nav className="me-auto" >
                        <Nav>
                            <NavLink to="/" className="nav-link">Home</NavLink>
                            <NavLink to="/camera" className="nav-link">Live Camera</NavLink>
                        </Nav>
                    </Nav>
                    <Nav>
                        <NavDropdown title="Setting" id="basic-nav-dropdown">
                            <NavDropdown.Item >
                                <NavLink to="/login" style={{ color: 'white' }} className="text-decoration-none">
                                    Login
                                </NavLink>
                            </NavDropdown.Item>
                            <NavDropdown.Item>
                                 <NavLink to="/sigin" style={{ color: 'white' }} className="text-decoration-none">Sign in</NavLink>
                            </NavDropdown.Item>
                            <NavDropdown.Item to="#action/3.2">
                                View
                            </NavDropdown.Item>
                            <NavDropdown.Item to="#action/3.3">Create</NavDropdown.Item>
                            <NavDropdown.Divider />
                            <NavDropdown.Item to="#action/3.4">
                                Logout
                            </NavDropdown.Item>
                        </NavDropdown>
                    </Nav>
                </Navbar.Collapse>
            </Container>
        </Navbar>
    );
}

