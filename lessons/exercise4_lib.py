# 1. Function with default parameter
def register_member(name, membership="Regular"):
    print(f"Member {name} registered with {membership} membership.")


# 2. Function with *args
def add_books(*books):
    count = 0
    for book in books:
        print(f"Book added: {book}")
        count += 1
    return count


# 3. Function with **kwargs
def borrow_book(member, **details):
    title = details.get("title", "Unknown Book")
    days = de
