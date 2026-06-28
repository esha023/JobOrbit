// Chrome extension background service worker
chrome.runtime.onInstalled.addListener(() => {
  console.log('JobOrbit Extension Installed successfully.')
})

// Listen for messages from content script or popup
chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {
  if (message.type === 'JOB_DETECTED') {
    console.log('Detected job post:', message.payload)
    // Perform async sync API calls or show badge notifications
    sendResponse({ status: 'queued' })
  }
  return true // keep channel open for async response
})
