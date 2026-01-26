<!--
SYNC IMPACT REPORT
Version change: 0.0.0 -> 1.0.0
List of modified principles: Initial creation
Added sections: All
Removed sections: None
Templates requiring updates: None (Initial)
Follow-up TODOs: None
-->

# Project Constitution

**Project:** Todo Full-Stack Web Application (Spec-Driven, Hackathon Phase-2)
**Version:** 1.0.0
**Ratified:** 2026-01-20
**Last Amended:** 2026-01-20
**Status:** Active

## Preamble
This constitution defines the non-negotiable architectural, engineering, and operational principles for the Todo Full-Stack Web Application. It serves as the primary source of truth for decision-making and ensures alignment with the Spec-Driven Development (SDD) methodology.

## 1. Core Principles

### 1.1 Spec-Driven Development
**Rule:** No code shall be written without a preceding specification, plan, and task list.
**Rationale:** Ensures clarity, completeness, and alignment before implementation begin. The flow is strictly: Spec → Plan → Tasks → Implementation.

### 1.2 Backend-First Architecture
**Rule:** Backend logic and data correctness must be validated before UI integration.
**Rationale:** Prevents frontend-driven hacks and ensures the API is the source of truth. The frontend is merely a consumer of the API.

### 1.3 Security by Design
**Rule:** Security is foundational, not an afterthought. Strict user isolation and JWT-based authentication are mandatory.
**Rationale:** Protects user data and ensures compliance. Unauthorized access must be rejected at the API level regardless of UI state.

### 1.4 Deterministic, Reproducible Development
**Rule:** All development must be deterministic and reproducible using Claude Code.
**Rationale:** Reduces "it works on my machine" issues and ensures a clean, audit-friendly history of changes.

### 1.5 Clarity for Reviewers
**Rule:** All artifacts and code must be clear and accessible to hackathon reviewers and engineers.
**Rationale:** Facilitates evaluation and onboarding. Code and documentation should explain "why", not just "what".

### 1.6 Production-Aligned Engineering
**Rule:** Adopt standards suitable for production environments, even within the hackathon scope.
**Rationale:** Builds habits of quality and robustness. Includes proper error handling, logging, and environment configuration.

## 2. Standards

### 2.1 Technology Standards
- **Frontend:** Next.js 16+ (App Router)
- **Backend:** Python FastAPI
- **ORM:** SQLModel
- **Database:** Neon Serverless PostgreSQL
- **Authentication:** Better Auth (JWT-based)
- **API Style:** RESTful with proper HTTP status codes

### 2.2 Security Standards
- **JWT Requirement:** Mandatory for all protected endpoints.
- **Verification:** Performed within FastAPI middleware/dependencies.
- **Secrets:** Shared secret configured via `BETTER_AUTH_SECRET`.
- **Identity:** Authenticated user identity derived ONLY from JWT claims.
- **Authorization:** Task ownership enforced on EVERY operation (Create, Read, Update, Delete).
- **Access Control:** Unauthorized requests return 401 (Unauthenticated) or 403 (Unauthorized) consistently.

### 2.3 Data Standards
- **Persistence:** All user data must be persistently stored in Neon PostgreSQL.
- **Isolation:** Strict zero-leakage policy between users. Users can only access their own tasks.
- **Ownership:** Explicit foreign key relationships between Users and Tasks.
- **Schema:** All schema changes must be spec-approved and migration-managed.

### 2.4 Frontend Standards
- **Responsiveness:** UI must function on desktop and mobile viewports.
- **Auth Integration:** Routes gated by auth state; JWT automatically attached to API requests.
- **UX:** Clear error messages and loading states.
- **Validation:** Never bypass backend validation; frontend validation is for UX only.
- **Testing:** End-to-end integration must be validated.

### 2.5 Documentation Standards
- **Mandatory Order:**
  1. Spec-1: Backend Core & Data Layer
  2. Spec-2: Authentication & Security Integration
  3. Spec-3: Frontend Application & Full-Stack Integration
- **Traceability:** All features must trace back to a written spec.

## 3. Constraints & Success Criteria

### 3.1 Constraints
- Must implement all basic Todo features (CRUD).
- Multi-user support is mandatory.
- No advanced features beyond defined specs (scope discipline).
- Hackathon-ready delivery timeline.
- All architectural decisions reviewable via specs and plans.

### 3.2 Success Criteria
- Fully functional multi-user Todo web application.
- Backend, Auth, and Frontend integrated correctly.
- Strict data isolation (Users access ONLY their own tasks).
- All APIs protected and validated.
- Project passes hackathon evaluation for correctness, security, and clarity.

## 4. Governance

### 4.1 Amendment Process
Changes to this constitution require a formal Spec modification and approval via the `sp.constitution` workflow.
- **Major Version:** Fundamental principle changes.
- **Minor Version:** New standards or constraints.
- **Patch Version:** Clarifications and corrections.

### 4.2 Compliance
Every Pull Request and Feature Spec must strictly adhere to these principles. Deviations must be rejected or documented as approved exceptions in an ADR.
