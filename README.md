# Pro Email Generator Toolkit

This tool moves beyond simple concatenation. It models real-world email systems using an Strategy Design Pattern implemented across email_strategies.py. Instead of one method, we now employ multiple specialized generators (e.g., professional corporate naming, initial/last patterns, random identifiers). The generator_core orchestrator randomly selects between these strategies to maximize the diversity and perceived validity of the final output pool.

---

# Core Components Explained

- email_strategies.py **(The Strategies)**: Contains discrete, specialized logic units for generating specific types of email addresses based on best practices found in corporate IT departments. This modularity allows you to easily plug in new naming conventions without touching the core running mechanism.
- generator_core.py **(The Context/Orchestrator)**: Manages which strategies are active and executes them cyclically, ensuring that the final batch is drawn from the union of all available pattern spaces. It handles the primary logic loop to maximize unique yields (set usage).
- main.py **(The View/Controller)**: Handles the presentation layer. It uses colorama for enhanced visual feedback crucial for a "high-level" feel, ensuring the output is engaging whether running in Termux or CMD Prompt.

---

# Installation & Usage Guide

### Prerequisites:

- Python 3.8+
- The necessary external library: `colorama`

### Installation Command:

1 | Clone this repository:
```bash
git clone https://github.com/r3xden/Email-Generator
```

2 | CD into repository:
```bash
cd Email-Generator
```

3 | Install requirements:
```bash
pip install -r requirements.txt
```

4 | Run the tool:
```bash
python main.py
```

---

# Notice

The structure automatically detects if you are in a Termux/Android environment vs. native PC shell and adjusts its welcome message.

### Educational Value & Credits

This implementation is designed for advanced educational purposes in software architecture, demonstrating:

- **Design Patterns**: Implementation of the Strategy Pattern.
- **Modularity**: Clear separation of concerns between logic, state, and presentation.
- **Robustness**: Multi-layer generation approach to mitigate pattern bias.

---

# Credits

Created by: Rexden [For Education purpose].

### LICENSE

Under MIT.

### Summary Table for Quick Reference

| Component | Role Key | Functionality | Complexity Level |
|-----------|----------|---------------|------------------|
| main.py | Runner/UI	| System detection, Output styling (Colorama)	| Medium |
| generator_core.py | Orchestrator | Manages and calls strategies; Collision control | High |
| email_strategies.py | Engine | Stores name pools & implements diverse generation formulas	| Very High |
