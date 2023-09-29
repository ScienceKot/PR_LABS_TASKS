### Task 4: Create HTTP web server.

For this laboratory task you will have to create a webserver that will will handle different routes and returns the page content.

If you choose to develop in Python you can modify the template provided by the Teacher. 

If you choose to develop the webserver in another programming language you will have to implement it from scratch, using the TCP protocol.

In class task:
* Create a webserver with 3 simple pages (like home, about us or contacts.) - 0.2 points.
* Create a template page for products that will incorporate products details. - 0.1 points.
* Create a product listing page. - 0.7 points.
* If a requested page doesn't exist return a 404 error code.

Also create a small TCP client that will connect to this webserver and will make TCP requests and print out the responses.

HINTS: For the products you can prepare a simple json file with the products fields like:
```json
[
  {
    "name" : "Fluent Python: Clear, Concise, and Effective Programming",
    "author" : "Luciano Ramalho",
    "price" : 39.95,
    "description" : "Don't waste time bending Python to fit patterns you've learned in other languages. Python's simplicity lets you become productive quickly, but often this means you aren't using everything the language has to offer. With the updated edition of this hands-on guide, you'll learn how to write effective, modern Python 3 code by leveraging its best ideas. "
  },
  {
    "name" : "Introducing Python: Modern Computing in Simple Packages",
    "author" : "Bill Lubanovic",
    "price" : 27.49,
    "description" : "Easy to understand and fun to read, this updated edition of Introducing Python is ideal for beginning programmers as well as those new to the language. Author Bill Lubanovic takes you from the basics to more involved and varied topics, mixing tutorials with cookbook-style code recipes to explain concepts in Python 3. End-of-chapter exercises help you practice what you’ve learned."
  }
]
```
Also, you can use regexes for parsing paths to extract the id of the product.

EXAMPLE: /product/1 will be returned the html tamplate filled with the information of the second dictionary.

### Homework

For the homework you will have to write a TCP parser of your own webserver.

The parser script should make requests to all pages on your webserver and:
* For simple page save the content of the page.
* From product pages product details should be placed in a dictionary like:
```json
{
    "name" : "Introducing Python: Modern Computing in Simple Packages",
    "author" : "Bill Lubanovic",
    "price" : 27.49,
    "description" : "Easy to understand and fun to read, this updated edition of Introducing Python is ideal for beginning programmers as well as those new to the language. Author Bill Lubanovic takes you from the basics to more involved and varied topics, mixing tutorials with cookbook-style code recipes to explain concepts in Python 3. End-of-chapter exercises help you practice what you’ve learned."
}
```
Finally routes to the product pages should be taken from the products listing page.