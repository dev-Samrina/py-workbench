# Py-Workbench 🛠️

A dedicated repository for modular Python applications, domain-level business logic, and algorithm design supporting my **Fullstack Django** development journey. 

This repository bridges pure Python fundamentals—such as state mutation, collections management, and functional validation—with real-world backend engineering patterns.

---

## 📌 Architectural Focus

Every script here isolates business logic outside of frameworks:
* **Pure Python Business Rules:** Decoupled algorithms that can be easily ported into Django model methods, service classes, or custom managers.
* **Data Flow & Collections:** Idiomatic use of dictionaries, lists, and loops reflecting how records and payloads are handled in backend workflows.
* **Clean Terminal Interfaces:** User-facing logic and state flow modeled cleanly via CLI before abstraction into web views and templates.

---

## 📂 Applications & Core Logic

### 1. Student Grade Calculator (`student_grade_calculator.py`)
* **Purpose:** Computes weighted percentages, validates score boundaries, and assigns standardized grade letters.
* **Backend Relevance:** Mirroring evaluation logic often found in educational web platforms, automated marking engines, or Django custom form validation.
* **Run:**
  ```bash
  python student_grade_calculator.py
  2. Shopping Cart Engine (shopping_cart.py)
Purpose: An interactive cart management session handling item selection, unit counts, dynamic subtotals, and final bill computation.

Backend Relevance: The foundational logic behind session-based e-commerce carts, checkout pipelines, and order computation in Django applications.

Run:

Bash
python shopping_cart.py
💻 Tech Stack
Language: Python 3.x

Ecosystem Target: Fullstack Django (Core Logic & OOP Foundations)

Dependencies: Python Standard Library

🚀 Setup & Execution
Clone the repository:

Bash
git clone [https://github.com/dev-samrina/py-workbench.git](https://github.com/dev-samrina/py-workbench.git)
Execute an application:

Bash
python shopping_cart.py
🗺️ Django Progression Roadmap
[ ] Refactor cart logic into an Object-Oriented paradigm (CartItem and Cart classes).

[ ] Port the shopping cart engine into a session-backed Django web application.

[ ] Implement database models using Django ORM (Product, Order, OrderItem).

[ ] Integrate SQLite/PostgreSQL for persistent cart transactions.

📝 License
Distributed under the MIT License.
