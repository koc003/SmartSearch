import { useState } from "react";
import ReactMarkdown from "react-markdown";

import "../styles/AnswerCard.css";

function AnswerCard({ answer, showToast }) {

    const [copied, setCopied] = useState(false);

    const handleCopy = async () => {

        try {

            await navigator.clipboard.writeText(answer);

            setCopied(true);
            showToast("Answer copied!");

            setTimeout(() => {

                setCopied(false);

            }, 2000);

        } catch (error) {

            console.error("Copy failed", error);

        }

    };

    return (

        <div className="answer-card">

            <div className="answer-header">

                <h2>Answer</h2>

                <button
                    className="copy-btn"
                    onClick={handleCopy}
                >
                    {copied ? "Copied!" : "📋 Copy"}
                </button>

            </div>

            <div className="answer-content">

                <ReactMarkdown>

                    {answer}

                </ReactMarkdown>

            </div>

        </div>

    );

}

export default AnswerCard;