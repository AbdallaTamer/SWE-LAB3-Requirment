### 2. Postman Collection: (https://www.postman.com/science-candidate-57891817/workspace/a-tamer/request/38975911-024baf03-53b1-4cee-b691-ae4bde746e08?action=share&creator=38975911&ctx=documentation)


#### **Test Cases for Postman Collection**:

**1. Test Case: GET `/books` (Valid Token)**  
- **Method**: `GET`
- **URL**: `http://127.0.0.1:5000/books`
- **Headers**:  
  `Authorization: Bearer secret-token`
- **Expected Response**: 
  - Status code: `200 OK`
  - Body: List of books in JSON format

---

**2. Test Case: GET `/books` (Invalid Token)**  
- **Method**: `GET`
- **URL**: `http://127.0.0.1:5000/books`
- **Headers**:  
  `Authorization: Bearer wrong-token`
- **Expected Response**: 
  - Status code: `401 Unauthorized`
  - Body: `{"message": "Invalid token!"}`

---

**3. Test Case: POST `/books` (Valid Input and Token)**  
- **Method**: `POST`
- **URL**: `http://127.0.0.1:5000/books`
- **Headers**:  
  - `Authorization: Bearer secret-token`
  - `Content-Type: application/json`
- **Body**:  
  ```json
  {
      "title": "New Book",
      "author": "New Author",
      "genre": "Science Fiction",
      "published_year": 2024
  }
  ```
- **Expected Response**: 
  - Status code: `201 Created`
  - Body: The newly created book in JSON format

---

**4. Test Case: POST `/books` (Invalid Input, Missing Title)**  
- **Method**: `POST`
- **URL**: `http://127.0.0.1:5000/books`
- **Headers**:  
  - `Authorization: Bearer secret-token`
  - `Content-Type: application/json`
- **Body**:  
  ```json
  {
      "author": "New Author",
      "genre": "Science Fiction",
      "published_year": 2024
  }
  ```
- **Expected Response**: 
  - Status code: `400 Bad Request`
  - Body: `{"error": "Title and author are required!"}`

---

**5. Test Case: PUT `/books/1` (Update Book, Valid Token)**  
- **Method**: `PUT`
- **URL**: `http://127.0.0.1:5000/books/1`
- **Headers**:  
  - `Authorization: Bearer secret-token`
  - `Content-Type: application/json`
- **Body**:  
  ```json
  {
      "title": "Updated Book Title",
      "author": "Updated Author"
  }
  ```
- **Expected Response**: 
  - Status code: `200 OK`
  - Body: The updated book in JSON format

---

**6. Test Case: DELETE `/books/2` (Delete Book, Valid Token)**  
- **Method**: `DELETE`
- **URL**: `http://127.0.0.1:5000/books/2`
- **Headers**:  
  `Authorization: Bearer secret-token`
- **Expected Response**: 
  - Status code: `200 OK`
  - Body: `{"message": "Book deleted!"}`

---

**7. Test Case: DELETE `/books/999` (Invalid ID, Book Not Found)**  
- **Method**: `DELETE`
- **URL**: `http://127.0.0.1:5000/books/999`
- **Headers**:  
  `Authorization: Bearer secret-token`
- **Expected Response**: 
  - Status code: `404 Not Found`
  - Body: `{"error": "Book not found!"}`
 

### 3. Swagger Documentation:


#### Swagger YAML File:
```yaml
openapi: 3.0.0
info:
  title: Book Collection API
  description: A simple API to manage a book collection.
  version: 1.0.0
servers:
  - url: http://127.0.0.1:5000

paths:
  /books:
    get:
      summary: Get all books
      responses:
        '200':
          description: A list of books
          content:
            application/json:
              schema:
                type: array
                items:
                  $ref: '#/components/schemas/Book'
        '401':
          description: Unauthorized
    post:
      summary: Add a new book
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/BookInput'
      responses:
        '201':
          description: Book created
        '400':
          description: Bad request
        '401':
          description: Unauthorized

  /books/{book_id}:
    put:
      summary: Update a book
      parameters:
        - name: book_id
          in: path
          required: true
          schema:
            type: integer
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/BookInput'
      responses:
        '200':
          description: Book updated
        '404':
          description: Book not found
        '401':
          description: Unauthorized

    delete:
      summary: Delete a book
      parameters:
        - name: book_id
          in: path
          required: true
          schema:
            type: integer
      responses:
        '200':
          description: Book deleted
        '404':
          description: Book not found
        '401':
          description: Unauthorized

components:
  schemas:
    Book:
      type: object
      properties:
        id:
          type: integer
        title:
          type: string
        author:
          type: string
        genre:
          type: string
        published_year:
          type: integer
    BookInput:
      type: object
      properties:
        title:
          type: string
        author:
          type: string
        genre:
          type: string
        published_year:
          type: integer
```

