# Task 2: Serialization.

Hi everyone welcome to the second laboratory task the PR laboratory work. The topic of this laboratory work is Serialization.

## Task description.

In the player.py file you have defined a class - Player. You have to create a players factory class that will be able to convert different serializable formats into player class and backwards.

In the [factory.py](https://github.com/ScienceKot/PR_LABS_TASKS/edit/main/LAB2/factory.py) you have a class defined with 6 empty methods which are:

```python
class PlayerFactory:
    def to_json(self, players):
        '''
            This function should transform a list of Player objects into a list with dictionaries.
        '''
        pass

    def from_json(self, list_of_dict):
        '''
            This function should transform a list of dictionaries into a list with Player objects.
        '''
        pass

    def from_xml(self, xml_string):
        '''
            This function should transform a XML string into a list with Player objects.
        '''
        pass

    def to_xml(self, list_of_players):
        '''
            This function should transform a list with Player objects into a XML string.
        '''
        pass

    def from_protobuf(self, binary):
        '''
            This function should transform a binary protobuf string into a list with Player objects.
        '''
        pass

    def to_protobuf(self, list_of_players):
        '''
            This function should transform a list with Player objects intoa binary protobuf string.
        '''
        pass
```

For the laboratory work, you must implement the first 4 methods (to_json, from_json, to_xml, from_xml).

You also have two files:
* players.json
* players.xml

Use them to test your factory.

After implementing all methods use the [tests.py](https://github.com/ScienceKot/PR_LABS_TASKS/edit/main/LAB2/tests.py) file to test your implementation. After all tests are passed please present the work to me.

To run the tests just run the following command:
``python tests.py``

## Homework.

For the homework you will have to implement two methods (from_protobuf and to_protobuf). 
To test your new functions use the homework_test_py file.

HINT: https://www.freecodecamp.org/news/googles-protocol-buffers-in-python/
HINT: You will be punished for using ChatGPT.
