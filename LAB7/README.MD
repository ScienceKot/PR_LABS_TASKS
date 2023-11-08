# Task 2: RabbitMQ.

Hi everyone in this laboratory work you have one of the following options to impliment the task:
1. Add RabbitMQ to the 999 parser.
2. Add RabbitMQ to the chatbot application.
## 999 Parser.

For this task you must do the following tasks:
1. Implement the url link extractor as a produce. It should after extracting the products url from the listing page push them to RabbitMQ Queue. (0.5 points)
2. Implement the product details parser functionality as a consumer. It should extract a url from the RabbitMQ queue parse the product details and write this data in a location of persistence. Then take another url from queue and so on. (0.5 points)
3. You should be able to run multiple consumers concurrently. The number of running threats should be settable. (0.5 points)
4. Implement a way of persistence. Either a data base or fiel (I recoment TinyDB). (0.5 points)

## Chatbot.

For this task you must do the following tasks:
1. When the users send's a message it pushes a message to RabbitMQ. (1 point)
2. Server should be able to extract these messages from RabitMQ and send them to the room it is addresses to. (1 point)

