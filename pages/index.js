import React, { useState } from 'react';
import { useRouter } from 'next/router';

export default function URLInput() {
  const [url, setUrl] = useState('');
  const router = useRouter();

  const handleSubmit = (e) => {
    e.preventDefault();
    // Save the URL in session storage for the next page
    sessionStorage.setItem('submittedUrl', url);
    // Redirect to the next page
    router.push('/text-input');
  };

  return (
    <div>
      <h1 className='indexHeading'>Enter the URL of .pdf or .txt file</h1>
      <form onSubmit={handleSubmit}>
        <label>
          URL :  
          <input
          className='textArea'
            type="url"
            placeholder='Enter the URL for .query functionality'
            value={url}
            onChange={(e) => setUrl(e.target.value)}
            required
          />
        </label>
        <br/>
        <button type="submit" className='btn'>Next</button>
      </form>
      <h2>This site has been built with Next.js</h2>
    </div>
  );
}
