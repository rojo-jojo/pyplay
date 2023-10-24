import pydantic
import json
from typing import Optional, List

class Book(pydantic.BaseModel):
    title: str
    author: str
    publisher: str
    price: float
    isbn_10: Optional[str]
    isbn_13: Optional[str]
    subtitle: Optional[str]

def main() -> None:
    with open("jsons_pydantic/data.json") as file:
        data = json.load(file)
        books: List[Book] = [Book(**item) for item in data]
        print(books[0].title)

if __name__ == '__main__':
    main()
    print("No tests")