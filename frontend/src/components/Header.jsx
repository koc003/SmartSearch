import "../styles/Header.css";

function Header() {
    return (
        <header className="header">
            <h1 className="header-title">
                Ask Questions from PDFs
            </h1>

            <p className="header-subtitle">
                Upload PDFs and ask questions using
                <strong> Gemini 2.5 Flash</strong> +{" "}
                <strong>FAISS RAG</strong>
            </p>
        </header>
    );
}

export default Header;