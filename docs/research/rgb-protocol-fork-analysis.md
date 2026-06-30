# Critical Research: RGB Protocol Fork Evaluation (2026-06-28)

## ⚠️ Critical Finding: v0.12 Incompatibility & Production Readiness
Recent research into the RGB ecosystem reveals a significant divergence between two primary forks. Our current implementation target (v0.12) is identified as **not production-ready** for our requirements.

### Fork Comparison

| Feature | RGB v0.11.1 (Target ✅) | RGB v0.12 (Current ❌) |
| :--- | :--- | :--- |
| **Org/Owner** | [rgb-protocol](https://github.com/rgb-protocol) | RGB-WG (Maxim Orlovsky) |
| **Status** | Production Mainnet (July 2025) | Research/Core Only |
| **Major Backing** | Tether USD₮ (70B+), Bitfinex | Individual/Experimental |
| **Wallets** | Iris, BitMask, Tribe, BiHelix | None |
| **Lightning** | Native (RGB Lightning Node) | Tests Disabled |
| **Stack** | Complete (lib + cmd + sandbox) | Core Only (incomplete) |

### Impact on Conxian
Our existing `rgb_adapter.rs` references the v0.12 ecosystem. Continuing on this path risks:
1. **Zero Wallet Compatibility**: No existing production wallets support v0.12.
2. **No Stablecoin Support**: Tether is launching on the v0.11.1 fork.
3. **Broken Lightning Path**: The LN integration in v0.12 is currently non-functional.

### Recommendation
**Immediate pivot to RGB v0.11.1 (rgb-lib).**
We must switch the `rgb-core` dependency to `rgb-lib` to align with the production ecosystem used by Tether and major wallet providers.

### Sources
- [RGB Protocol Association Official Docs](https://docs.rgb.info)
- [Why v0.11.1? (Official Statement)](https://github.com/rgb-protocol/.github/blob/master/WHY_v0.11.1.md)
