# JobOrbit Shared Module (`joborbit-shared`)

This repository folder holds configuration properties, lifecycle enums, API JSON schemas, and validators used across the client frontend, backend REST API, and browser extension.

## Directory Structure

```
joborbit-shared/
├── contracts/       # API request/response JSON schemas and contracts
├── constants/       # Global constants, paths, and config bounds
├── enums/           # State and lifecycle enums (ApplicationStatus, InterviewType, etc.)
├── validators/      # Reusable validation schemas and boundary rules
└── README.md        # This integration overview
```

## Integration Strategy

Because this workspace uses heterogeneous runtimes (**TypeScript** on the frontend & browser extension, **Python** on the backend), this package does not store runtime-specific code directly. Instead:

### 1. Enums & Constants
Enums and constants are declared as raw JSON or simple dictionary schemas where applicable, or generated as companion source targets in TypeScript (`.ts`) and Python (`.py`) during compilation/build stages.

*   **Enums Defined**:
    *   `ApplicationStatus`: `WISHLIST`, `APPLIED`, `INTERVIEWING`, `OFFERED`, `REJECTED`
    *   `InterviewType`: `SCREENING`, `TECHNICAL`, `BEHAVIORAL`, `SYSTEM_DESIGN`, `FIT`
    *   `NotificationType`: `DEADLINE_REMINDER`, `INTERVIEW_ALERT`, `SYSTEM_UPDATE`
    *   `TaskPriority`: `LOW`, `MEDIUM`, `HIGH`, `CRITICAL`
    *   `EmailCategory`: `RECRUITER_CONTACT`, `AUTO_REPLY`, `INTERVIEW_REQUEST`, `REJECTION`, `OFFER`

### 2. API Contracts & JSON Schemas
Request/response models are described in **JSON Schema** format under the `contracts/` directory. 
*   **Backend Integration**: FastAPI reads JSON schemas directly or compiles Pydantic classes dynamically matching these fields.
*   **Frontend & Extension Integration**: Frontend packages compile static schemas into TypeScript typings using mapping libraries (e.g., `json-schema-to-typescript`).
