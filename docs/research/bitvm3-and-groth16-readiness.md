# Research: BitVM3 & Groth16 Production Readiness (2026-06-28)

## 1. BitVM3: Garbled Circuits & recursive proofs
BitVM3 is moving from research to pilot phase. It offers a ~3000x dispute cost reduction compared to BitVM2.

### Key Findings
- **BitHash**: Enables SNARK verification on Bitcoin script with minimal footprint.
- **Garbled Circuits**: Reduces on-chain fraud proofs to compact challenges (~200 bytes).
- **Adoption**: Teams like Citrea, Alpen, and Chainway are actively integrating BitVM3 concepts for recursive proof verification.

## 2. Groth16 on Bitcoin: Production Status
Previously considered experimental, Groth16 verification is now **production-ready** on Bitcoin Mainnet as demonstrated by Citrea's Clementine bridge.

### Status Update
- **Citrea Mainnet**: Launched Jan 2026.
- **Architecture**: RISC Zero zkVM (STARK) → Groth16 wrapper → BitVM2 on-chain verification.
- **Logic**: Groth16 provides the shortest proofs (~200-300 bytes), which is critical for Bitcoin's block space constraints.

## 3. Recommended Integration Path
1. **BitVM Adapter**: Update `verify_state_proof` to include Groth16 verifier logic.
2. **Recursive Aggregation**: Evaluate RISC Zero Bonsai for STARK-to-SNARK wrapping.
3. **Bridge Verification**: Use Citrea's Clementine as the reference for trust-minimized bridging.
