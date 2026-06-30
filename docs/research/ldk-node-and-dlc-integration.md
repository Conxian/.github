# Research: LDK Node Production & DLC Integration (2026-06-28)

## 1. Lightning: LDK Node v0.4+
The current simulated Lightning backend is a bottleneck. LDK Node is the recommended production path.

### Key Features
- **Production Daemon**: LDK Server GA since Bitcoin 2026.
- **API Simplification**: Wraps full LDK complexity into ~30 API calls.
- **Compatibility**: BOLT12 and LSP support built-in.

## 2. DLC: rust-dlc & Adaptor Signatures
Discrete Log Contracts (DLCs) are required for trust-minimized financial products (bonds, derivatives).

### Technical Requirements
- **Crates**: `dlc-manager`, `dlc-messages`, `dlc-trie`.
- **Adaptor Signatures**: Schnorr (BIP-340) for Discreet Log Contracts on Taproot.
- **Transport**: NIP-88 (Nostr-based DLC messaging) for oracle announcements and CET negotiation.

## 3. Recommended Actions
1. **Adapter Switch**: Replace `SimulatedLightningBackend` with `LdkNodeBackend`.
2. **DLC CET Construction**: Implement real Contract Execution Transaction (CET) logic using `rust-dlc`.
