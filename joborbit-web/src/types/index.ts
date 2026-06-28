// Common TypeScript interfaces for JobOrbit
export interface UserProfile {
  id: string
  email: string
  displayName?: string
  createdAt: string
}

export interface JobApplication {
  id: string
  userId: string
  company: string
  position: string
  status: 'WISHLIST' | 'APPLIED' | 'INTERVIEWING' | 'OFFERED' | 'REJECTED'
  salary?: number
  location?: string
  url?: string
  appliedDate?: string
  notes?: string
}
