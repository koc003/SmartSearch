import "../styles/Navbar.css";

function Navbar() {

    return (

        <nav className="navbar">

            <div className="navbar-logo">

                🔍 SmartSearch

            </div>

            <div className="navbar-links">

                <a
                    href="https://github.com/koc003/SmartSearch"
                    target="_blank"
                    rel="noreferrer"
                >
                    GitHub
                </a>

            </div>

        </nav>

    );

}

export default Navbar;