# CSI3105 Software Testing Assignment

## Overview
This repository contains the testing implementation for a Python-based Event Booking System. The system supports scheduling meetings, booking vacation dates, and checking availability for rooms and personnel.

The purpose of this project is to apply software testing techniques to evaluate the correctness, reliability, and robustness of the system using automated testing.

---

## Testing Approach

The project uses two main testing strategies:

### Black-Box Testing (Person A)
- Equivalence Partitioning (EP)
- Boundary Value Analysis (BVA)
- Weak-robust test case design
- Focus on input validation and known defects

### Structural Testing (Person B)
- Control Flow Graphs (CFG)
- Branch coverage testing
- Focus on internal program logic

---

## Project Structure


CSI3105-Testing-Assignment/
│
├── src/ # System source code
├── tests/ # pytest test files
│ ├── test_blackbox_ep.py
│ ├── test_blackbox_bva.py
│ ├── test_faults.py
│ ├── test_structural_meeting.py
│ ├── test_structural_calendar.py
│ ├── test_structural_room.py
│ └── test_structural_person.py
│
├── docs/ # Report and documents
├── test_outputs/ # Screenshots of pytest results
├── requirements.txt
└── README.md


---

## Responsibilities

### Person A (Wilson)
- Design Equivalence Partitioning (EP) test cases
- Design Boundary Value Analysis (BVA) test cases
- Implement pytest tests for input validation
- Test known faults:
  - Feb 29 (leap year issue)
  - 30 November issue
  - 11:00–11:59 PM time issue
  - Invalid dates (e.g. day 32)
  - Case sensitivity issues
- Produce defect report

### Person B (Chilufya)
- Create Control Flow Graphs (CFG)
- Design branch coverage test cases
- Implement structural pytest tests
- Document test plan and execution

---

## Setup Instructions

### 1. Clone the Repository


git clone https://github.com/wilsonmugwe/CSI3105-Testing-Assignment.git
cd CSI3105-Testing-Assignment


---

### 2. Install Dependencies


python -m pip install pytest


---

### 3. Run Test Cases


python -m pytest


All test files are located in the `tests/` directory.

---

## Test Results

- Test results will appear in the terminal after running pytest
- Screenshots of test execution should be saved in:


test_outputs/


---

## Known Issues Tested

The following known defects are tested in this project:

- Leap year issue (Feb 29 not handled correctly)
- Invalid dates accepted (e.g. day 32)
- 30 November booking issue
- 11 PM booking time issue
- Case sensitivity issues for room and person names
- Ambiguous error messages

---

## Notes

- Some tests may fail intentionally to demonstrate existing defects
- Failed tests are valid if they highlight real system issues
- All identified defects are documented in the report

---

## Submission Contents

The final submission includes:

- Testing report (in docs/)
- Complete project folder (this repository)
- pytest test files
- Screenshots of test execution
- Meeting minutes
- Peer review form

---

## Tools Used

- Python 3
- pytest
- Visual Studio Code / PyCharm
- GitHub