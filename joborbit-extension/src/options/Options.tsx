import React, { useState, useEffect } from 'react'

function Options() {
  const [apiUrl, setApiUrl] = useState('http://localhost:8000')

  useEffect(() => {
    chrome.storage.sync.get(['apiBaseUrl'], (result) => {
      if (result.apiBaseUrl) {
        setApiUrl(result.apiBaseUrl)
      }
    })
  }, [])

  const handleSave = () => {
    chrome.storage.sync.set({ apiBaseUrl: apiUrl }, () => {
      alert('Settings saved successfully.')
    })
  }

  return (
    <div style={{ maxWidth: '400px', margin: '0 auto', background: '#0f172a', padding: '24px', borderRadius: '8px', border: '1px solid #334155' }}>
      <h2 style={{ color: '#818cf8', marginTop: 0 }}>Extension Settings</h2>
      <div style={{ marginBottom: '16px' }}>
        <label style={{ display: 'block', marginBottom: '8px', fontSize: '14px' }}>JobOrbit Backend API URL</label>
        <input 
          type="text" 
          value={apiUrl} 
          onChange={(e) => setApiUrl(e.target.value)}
          style={{
            width: '100%',
            padding: '8px',
            borderRadius: '4px',
            border: '1px solid #475569',
            backgroundColor: '#1e293b',
            color: '#f8fafc',
            boxSizing: 'border-box'
          }}
        />
      </div>
      <button 
        onClick={handleSave}
        style={{
          padding: '8px 16px',
          backgroundColor: '#4f46e5',
          border: 'none',
          borderRadius: '4px',
          color: '#ffffff',
          fontWeight: 'bold',
          cursor: 'pointer'
        }}
      >
        Save Settings
      </button>
    </div>
  )
}

export default Options
