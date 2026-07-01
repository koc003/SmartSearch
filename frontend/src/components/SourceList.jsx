import { useState } from "react";

import "../styles/SourceList.css";

function SourceList({ sources }) {

    const [expandedIndex, setExpandedIndex] = useState(null);

    const toggleSource = (index) => {

        if (expandedIndex === index) {
            setExpandedIndex(null);
        } else {
            setExpandedIndex(index);
        }

    };

    return (

        <div className="source-card">

            <h2>
                Retrieved Sources ({sources.length})
            </h2>

            {sources.map((source, index) => {

                const expanded = expandedIndex === index;

                return (

                    <div
                        key={source.index}
                        className="source-item"
                        onClick={() => toggleSource(index)}
                    >

                        <div className="source-header">

                            <div>

                                <strong>
                                    📄 Source {index + 1}
                                </strong>

                            </div>

                            <div>

                                {expanded ? "▲" : "▼"}

                            </div>

                        </div>

                        <p className="source-preview">

                            {expanded
                                ? source.chunk
                                : `${source.chunk.slice(0, 90)}...`
                            }

                        </p>

                    </div>

                );

            })}

        </div>

    );

}

export default SourceList;