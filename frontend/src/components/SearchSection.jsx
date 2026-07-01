import { useState } from "react";
import { searchQuestion } from "../services/api";

import "../styles/SearchSection.css";
import LoadingSpinner from "./LoadingSpinner";

function SearchSection({ onSearchComplete }) {
    const [query, setQuery] = useState("");
    const [loading, setLoading] = useState(false);

    const handleSearch = async () => {
        if (!query.trim()) return;

        try {
            setLoading(true);

            const result = await searchQuestion(query);

            onSearchComplete(result);

        } catch (error) {
            console.error(error);
            alert("Search failed.");
        } finally {
            setLoading(false);
        }
    };

    const handleKeyDown = (event) => {

        if (event.key === "Enter" && !event.shiftKey) {

            event.preventDefault();

            handleSearch();

        }

    };

    return (
        <div className="search-card">

            <h2>Ask AI</h2>

            <div className="search-box">

                <textarea
                    className="search-input"
                    placeholder="Ask anything about the uploaded PDF..."
                    value={query}
                    onChange={(e) => setQuery(e.target.value)}
                    onKeyDown={handleKeyDown}
                    rows={5}
                    disabled={loading}
                />

                <button
                    className="search-btn"
                    onClick={handleSearch}
                    disabled={loading}
                >
                    {loading ? <LoadingSpinner /> : "🔍"}
                </button>

            </div>

        </div>
    );
}

export default SearchSection;