import asyncio
from typing import List, Dict

# DATABASE (IN-MEMORY)

books: List[Dict[str, object]] = [
    {"id": 1, "title": "Atomic Habits", "available": True},
    {"id": 2, "title": "Clean Code", "available": True},
    {"id": 3, "title": "Deep Work", "available": True}
]

# Lock to prevent race conditions
lock = asyncio.Lock()


# CORE FUNCTIONS

async def borrow_book(user_id: int, book_id: int) -> str:
    await asyncio.sleep(1)  # simulate delay

    async with lock:  # prevents two users modifying at same time
        for book in books:
            if book["id"] == book_id:
                if book["available"]:
                    book["available"] = False
                    return f"[SUCCESS] User {user_id} borrowed '{book['title']}'"
                else:
                    return f"[FAILED] User {user_id} tried to borrow '{book['title']}' (Already taken)"

        return f"[ERROR] Book {book_id} not found"


async def return_book(user_id: int, book_id: int) -> str:
    await asyncio.sleep(1)

    async with lock:
        for book in books:
            if book["id"] == book_id:
                book["available"] = True
                return f"[RETURNED] User {user_id} returned '{book['title']}'"

        return f"[ERROR] Book {book_id} not found"



# DISPLAY FUNCTION

def display_books() -> None:
    print("\n Current Library Status:")
    for book in books:
        status = "Available" if book["available"] else "Borrowed"
        print(f"Book ID {book['id']}: {book['title']} - {status}")
    print("-" * 40)



# SIMULATION

async def simulate_users() -> None:
    print(" Starting Library Simulation...\n")

    display_books()

    tasks = [
        borrow_book(1, 1),
        borrow_book(2, 1),  # conflict
        borrow_book(3, 2),
        return_book(1, 1),
        borrow_book(4, 1),  # after return
        borrow_book(5, 3)
    ]

    results = await asyncio.gather(*tasks)

    print("\n Operation Results:")
    for result in results:
        print(result)

    display_books()



# MAIN ENTRY POINT

if __name__ == "__main__":
    asyncio.run(simulate_users())