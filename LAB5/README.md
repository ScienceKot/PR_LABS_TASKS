## Task 5: Create Basic Chat.

### In class task.

Plase find the task [here](https://apanin.atlassian.net/wiki/spaces/~5570586a87144029464756beeaa7dd41789a42/pages/2621441/Lecture+5+Create+basic+chat)

### Homwork.

Add to the existing chat the possibility to send .txt files and images.

For sending a image implement the following functionality add the handling of the following commands:
* ``upload: <path to file>`` - this command should check if the file exists at the provided path it exists it should be uploaded to server.
    * If the file exists then it is send to the server using the TCP connection. Then the server will respond ``User X uploaded the name_of_file.txt file``. Finally all files should be save in a Media server accessible only for server, for example ``SERVER_MEDIA``
    * If the file doesn't exist the user should recieve a message - ``File <name of file> doesn't exist``. (This message should be recieved only by the user that tried to send a file).
* ``download: <name of file.extension>`` - this command should check if the file exists in the ``SERVER_MEDIA`` folder, and if it exists the server should send it to the client.
    * If the file exists then it is send to the client requesting it and then saved by the client in a specific media folder.
    * If the file doesn't exist then the server should return the following message ``The <file.extention> doesn't exist``

This task is formed from 2 subtasks.
* Sending a .txt file - you should be able to send a txt file. For this task you can send the file content in json or in a binary format, You are free to choose - (0.4 points).
* Sending a image (.png or .jpg or .jpeg) - you should be able to send a image. For this task you will have to send the image as a binary format. (0.6 points)

In rest the communication should remain in the json format.

TIPS: When creatting a client you create a media folder for it with a unique name (you can user uuid for it) and also for the every room. You can delete it when the client are stopped.