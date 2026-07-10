## Architectural Decisions & Testing Strategy

* *Note on Architecture:* In a mature production environment, testing a third-party financial API directly within an E2E UI pipeline is generally discouraged due to network flakiness, rate limiting, and execution speed. In production, the Binance API client would be thoroughly covered by unit and backend integration tests using mocked payloads, while the frontend would be tested using simulated server responses.

## Why This Hybrid Approach Was Chosen For This Portfolio

This framework intentionally implements a Hybrid E2E/Integration Testing strategy to demonstrate advanced automation engineering capabilities that standard tutorial projects omit:

* *Cross-System Data Pipeline Validation:* Instead of just verifying that UI elements exist, this test validates the integrity of the data passing between the frontend (React shopping cart) and the backend data wrapper (Binance API client).

* *Defensive Testing & Domain Knowledge:* The test verifies critical financial logic (ask_price > bid_price) to prove the application can gracefully handle corrupted or anomalous data from third-party feeds before passing it to the checkout calculations.

* *Targeted Gap Coverage:* While unit tests confirm that the math formulas work in isolation, this hybrid E2E test ensures that the real-world workflow—from adding an item to a dynamic React DOM to calculating a live crypto invoice total—functions seamlessly without synchronization or formatting breakdowns.