import { useState } from "react";
import UploadSection from "./components/UploadSection";
import SearchSection from "./components/SearchSection";
import AnswerCard from "./components/AnswerCard";
import SourceList from "./components/SourceList";
import Header from "./components/Header";
import "./styles/App.css";
import Toast from "./components/Toast";
import Navbar from "./components/Navbar";

function App() {
  const [isUploaded, setIsUploaded] = useState(false);
  const [searchResult, setSearchResult] = useState(null);
  const [toast, setToast] = useState({
    visible: false,
    message: "",
    type: "success",
  });

  const handleUploadSuccess = () => {
    setIsUploaded(true);

    // Clear previous search results when a new PDF is uploaded
    setSearchResult(null);
  };

  const handleSearchComplete = (result) => {
    setSearchResult(result);
  };
  const showToast = (message, type = "success") => {

    setToast({
        visible: true,
        message,
        type,
    });

    setTimeout(() => {

        setToast((prev) => ({
            ...prev,
            visible: false,
        }));

    }, 2500);

  };
  return (
    <div className="app">
      <Toast
        message={toast.message}
        type={toast.type}
        visible={toast.visible}
      />
      <div className="container">
        <Navbar />
        <Header />

        <UploadSection
          onUploadSuccess={handleUploadSuccess}
          showToast={showToast}
        />

        {isUploaded && (
          <>
            <p className="upload-success">
              PDF uploaded successfully. You can now ask questions.
            </p>

            <SearchSection
              onSearchComplete={handleSearchComplete}
            />
          </>
        )}

        {searchResult && (
          <>
            <AnswerCard
              answer={searchResult.answer}
            />

            <SourceList
              sources={searchResult.sources}
            />
          </>
        )}

      </div>
    </div>
  );
}

export default App;