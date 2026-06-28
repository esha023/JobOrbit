import { BrowserRouter as Router, Routes, Route } from 'react-router-dom'
import { QueryClient, QueryClientProvider } from '@tanstack/react-query'

const queryClient = new QueryClient({
  defaultOptions: {
    queries: {
      refetchOnWindowFocus: false,
      retry: 1,
    },
  },
})

function App() {
  return (
    <QueryClientProvider client={queryClient}>
      <Router>
        <Routes>
          <Route 
            path="/" 
            element={
              <div className="flex flex-col items-center justify-center min-h-screen p-4 text-center">
                <header className="max-w-2xl glassmorphism-card rounded-2xl p-8 border border-slate-800">
                  <h1 className="text-4xl md:text-5xl font-extrabold tracking-tight bg-clip-text text-transparent bg-gradient-to-r from-accent-indigo via-accent-purple to-accent-blue mb-4">
                    JobOrbit
                  </h1>
                  <p className="text-lg text-slate-350 mb-6">
                    AI-powered Career Management Platform. Track job applications, schedule interviews, track recruiter emails, parse resumes, and generate cover letters.
                  </p>
                  <div className="text-sm text-slate-500">
                    Application scaffold initialized successfully.
                  </div>
                </header>
              </div>
            } 
          />
        </Routes>
      </Router>
    </QueryClientProvider>
  )
}

export default App
