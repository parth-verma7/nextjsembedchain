import React, { useState } from 'react';
import { useRouter } from 'next/router';

export default function TextInput() {
    const [text, setText] = useState('');
    const [ans, setAns] = useState(''); // State to hold the 'ans'
    const router = useRouter();

    const handleSubmit = async (e) => {
        e.preventDefault();

        try {
            const response = await fetch('http://127.0.0.1:5000/process-text', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ text }),
            });

            if (response.ok) {
                const result = await response.json();
                setAns(result.ans); // Set the 'ans' in state
            } else {
                console.error('Text processing failed');
            }
        } catch (error) {
            console.error('Error:', error);
        }
    };

    return (
        <div>
            <h1 className='indexHeading'>Enter your query</h1>
            <form onSubmit={handleSubmit}>
                <label className='labelText'>
                    Implement the .add() functionality:
                    <br/>
                    <br/>
                    <textarea
                        className='textArea'
                        placeholder='Enter the query to extract from the link of .pdf or .txt uploaded'
                        value={text}
                        onChange={(e) => setText(e.target.value)}
                        required
                    />
                </label>
                <br/>
                <br/>
                <button type="submit" className='btn' >Submit</button>
                <h2>This backend has been built with Flask</h2>
            </form>
            
            {/* Display the 'ans' on the page */}
            {ans && (
                <div className='finalAnswer'>
                    <h2>Answer:</h2>
                    <h3>{ans}</h3>
                </div>
            )}
        </div>
    );
}
