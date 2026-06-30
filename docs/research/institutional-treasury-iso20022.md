# Research: ISO 20022 Institutional Treasury Support

## Status: Transition from pacs.008 to camt.053/054
While we have support for `pacs.008` (Credit Transfer), institutional treasury requires statement and notification support.

### Key Message Types
- **camt.053**: Bank-to-Customer Statement (End-of-Day). The ISO replacement for MT940.
- **camt.054**: Bank-to-Customer Debit/Credit Notification. The ISO replacement for MT942.
- **camt.052**: Intraday Report (Lower priority).

### Market Context (2026)
- **SWIFT Migration**: Completed Nov 2025. Legacy MT messages are now rejected for cross-border payments.
- **BRICS Impact**: CIPS and SPFS are using ISO 20022 with specific extensions that require normalization.

### Implementation Gap
Current `normalize_brics_ingress()` needs to distinguish between mBridge and CIPS-specific extensions to prevent parsing errors on high-value settlements.
