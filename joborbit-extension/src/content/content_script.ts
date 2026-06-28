// Content script running on LinkedIn/Indeed job details pages
console.log('JobOrbit Content Script active.')

function parseJobDetails() {
  // Logic to extract job title, company, description, and link will go here
  const title = document.querySelector('h1')?.textContent?.trim() || ''
  return {
    title,
    url: window.location.href,
    scrapedAt: new Date().toISOString()
  }
}

// Listen for scraping requests from popup
chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
  if (request.action === 'SCRAPE_JOB') {
    const jobData = parseJobDetails()
    sendResponse(jobData)
  }
  return true
})
