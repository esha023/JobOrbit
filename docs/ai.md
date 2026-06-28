# JobOrbit AI Module Documentation

This document describes the structure of the artificial intelligence package (`joborbit-api/src/app/ai/`), explaining the design principles of prompts, parsing utilities, agents, and multi-step pipeline workflows.

## 1. Design Guidelines (AI-First Architecture)
JobOrbit isolates AI elements to prevent business models from leaking into integration-specific services. This approach makes it easy to substitute models (e.g. swap Gemini with OpenAI or local LLMs) or test prompting chains independently.

---

## 2. Directory Layout & Components

### 1. `agents/`
Defines agent scripts that perform distinct tasks using prompt templates, parser adapters, and model APIs.
*   **Resume Analyzer**: Validates resume structure and extracts skills/experience levels.
*   **Resume Matcher**: Compares a user's resume against job descriptions, calculating suitability scores.
*   **Interview Coach**: Generates interview questions based on job postings.
*   **Email Classifier**: Catches incoming emails and labels recruiters, schedule requests, or rejection alerts.
*   **Cover Letter Generator**: Drafts cover letters matching job specs.
*   **Career Advisor**: Recommends action logs based on application status.

### 2. `prompts/`
Stores template strings for LLMs. Isolating prompt configurations from python scripts keeps formatting clean and readable.

### 3. `parsers/`
Extracts structured JSON data from messy, unstructured text. Converts raw inputs like HTML job boards, PDFs, or email strings into validated schemas.

### 4. `responses/`
Holds Pydantic validation structures for structured LLM outputs, ensuring the API returns valid data.

### 5. `integrations/`
Contains third-party client wrappers. It acts as the driver layer (e.g., [gemini.py](file:///C:/Users/Esha%20Chavan/.gemini/antigravity/scratch/joborbit/joborbit-api/src/app/ai/integrations/gemini.py)) mapping raw SDK calls.

### 6. `workflows/`
Executes multi-agent orchestrators. Pipelines process inputs across multiple agents sequentially (e.g. parse resume text -> extract skills -> match job descriptions -> output recommendations).

### 7. `utils/`
Shared helper tools (e.g., token estimators, content parsers, request retry mechanisms).
