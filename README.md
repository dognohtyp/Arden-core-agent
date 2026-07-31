# Aeden: Local Autonomous Agent Core

An enterprise-ready, air-gapped Autonomous AI Agent infrastructure designed to execute localized LLM orchestration entirely decoupled from third-party cloud APIs.

## Key Architecture Milestones

*   **Context Window Engine:** Engineered a custom sliding-window buffer management layer to mathematically truncate incoming memory states, safely staying beneath hard model token constraints.
*   **Hardware Execution Layer:** Configured low-level CUDA GPU runtime acceleration drivers to maximize execution speed on local consumer hardware.
*   **High-Frequency Automation:** Developed multi-threaded data pipelines utilizing WebSocket protocol overrides and browser automation hooks to bypass enterprise security tokens in real time.

## System Topology

*   `autonomous_core.py` — Main context-bounded inference loop engine.
*   `Seeds/` — Base initialization state layer configurations.
*   `Memory/` — Sliding-window persistent state log directory.

## License

This architecture is distributed completely open-source under the official **MIT License**.
