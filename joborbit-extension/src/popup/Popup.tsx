import React, { useState, useEffect } from 'react'

function Popup() {
  const [job, setJob] = useState<{ title?: string; url?: string } | null>(null)
  const [loading, setLoading] = useState(false)

  const handleCapture = async () => {
    setLoading(true)
    try {
      const [tab] = await chrome.tabs.query({ active: true, currentWindow: true })
      if (tab?.id) {
        chrome.tabs.sendMessage(tab.id, { action: 'SCRAPE_JOB' }, (response) => {
          if (response) {
            setJob(response)
          }
        })
      }
    } catch (error) {
      console.error('Error capturing job detail page:', error)
    } finally {
      setLoading(false)
    }
  }

  return (
    <div style={{ padding: '16px' }}>
      <h3 style={{ margin: '0 0 12px 0', color: '#6366f1' }}>JobOrbit Tracker</h3>
      <button 
        onClick={handleCapture}
        style={{
          width: '100%',
          padding: '8px 12px',
          backgroundColor: '#4f46e5',
          border: 'none',
          borderRadius: '4px',
          color: '#ffffff',
          fontWeight: 'bold',
          cursor: 'pointer'
        }}
      >
        {loading ? 'Analyzing...' : 'Clip Job Details'}
      </button>

      {job && (
        <div style={{ marginTop: '16px', background: '#1e293b', padding: '10px', borderRadius: '4px' }}>
          <p style={{ fontSize: '12px', margin: '4px 0' }}><strong>Title:</strong> {job.title || 'N/A'}</p>
          <p style={{ fontSize: '10px', margin: '4px 0', wordBreak: 'break-all' }}><strong>URL:</strong> {job.url}</p>
        </div>
      )}
    </div>
  )
}

export default Popup
