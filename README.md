# Library Management System (Asynchronous Python)

## Overview

This project is a terminal-based Library Management System implemented in Python. It demonstrates the use of asynchronous programming to handle multiple users borrowing and returning books concurrently. The system focuses on simplicity while showcasing core programming concepts such as async, await, and type annotations.

## Features

Concurrent book borrowing and returning
Simulation of multiple users interacting simultaneously
Prevention of race conditions using asyncio.Lock
Clear and structured terminal output

### Technologies

- Python 3
- asyncio
- typing module
- How to Run
- Ensure Python 3 is installed
- Navigate to the project folder

### Run:

python main.py
Key Concepts
Asynchronous Programming: Enables non-blocking execution using async and await
Concurrency Control: Ensures safe data access using asyncio.Lock
Type Annotations: Improves readability and code reliability
Output

## The program displays:

- Initial library status
- Results of concurrent operations
- Final updated library state
- Limitations
- Uses in-memory data (no persistence)
- No user interface
- Conclusion

This project demonstrates efficient handling of concurrent operations using Python’s asynchronous features, while maintaining simplicity and clarity in design.
