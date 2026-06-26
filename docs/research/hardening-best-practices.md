# Research: Security Hardening & Fail-Closed Patterns

This document consolidates research and best practices for the active hardening waves (Gateway and Enclave SDK).

## 1. Fail-Closed Admin & Gateway Patterns (CON-1279)

### Startup Secret Validation
- **Requirement:** Prevent application startup if sensitive secrets are in a "sentinel" or "default" state.
- **Pattern:**
  ```rust
  fn validate_secrets() -> Result<(), HardeningError> {
      let secret = env::var("ADMIN_API_KEY")?;
      if secret == "default_unsafe_value" || secret.len() < 32 {
          return Err(HardeningError::UnsafeSecret);
      }
      Ok(())
  }
  ```
- **Goal:** Deterministic rejection of unsafe configurations.

### Authenticated Route Enforcement
- **Requirement:** Consistent auth across all admin and governance routes.
- **Pattern:** Use a middleware that defaults to rejection. Any route not explicitly marked as "Public" must require a valid JWT or API key.
- **Degraded Mode:** If the auth provider is unreachable, the gateway must return `503 Service Unavailable` rather than allowing bypass.

## 2. Production-Boundary & Enclave Hardening (CON-1280)

### Driver Selection Logic
- **Requirement:** Prevent simulated drivers from reaching production builds.
- **Pattern:** Use Cargo features and compile-time checks.
  ```rust
  #[cfg(feature = "prod")]
  use enclave_driver::ProductionDriver;

  #[cfg(feature = "sim")]
  compile_error!("Simulation driver detected in production-flagged build!");
  ```

### Replay-Guard Fail-Closed (TEE)
- **Requirement:** Enclave must refuse operation if replay protection cannot be verified.
- **Mechanism:** Monotonic counters or persistent state root verification.
- **Fail-Closed logic:** If the monotonic counter read fails or returns a value lower than the last known state, the enclave must lock itself and refuse to sign further transactions.

### Attestation-Bypass Exclusion
- **Requirement:** Explicitly exclude debug paths that bypass remote attestation.
- **Action:** Remove any `debug_attestation` mocks from the production release branch.

---
*Status: Initial Research Complete (2026-06-26)*
