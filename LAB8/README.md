# Task 8: RAFT Algorithm Implimentation using UDP.

Hi everyone, welcome to the 8th laboratory on Network Programming. In this Laboratory you are going to implement the RAFT algorithm for Leader Election.

## Task description.

For this task you have to take the laboratory where you implemented a CRUD Service and add two more copies of this service as separated services.

From this services one will be the Leader and the other ones will be the followers.

The difference in these two types of services is the following:
* Leaders can do writes (CREATE, UPDATE, DELETES) and reads (READ).
* The followers can accept only reads.
* When a Leader accepts write request it should forward this request to all followers.
* The followers should accept writes only from the leader.

For this laboratory you will have to impliment the RAFT algorithm for the Leader Election. The RAFT algorithm has the following steps:
1. All services try to connect using the UDP connection and try bind to the connection.
2. Only one will succeed in this, and this service will become the Leader.
3. The rest of services will become Followers.
4. After becoming a Follower the services should send to the leader a Accept message informing they accept him being a leader.
5. The Leader should response back with it's HTTP credentials (ip, port, token for writes) to inform the followers about it's location.
6. After getting the Leader's information the Followers should send back their HTTP credentials.
7. The Leader should save for later use the followers credentials.
8. THe HTTP server starts up.

After electing the Leader service, the followers should accept only read requests from outer world, however the Leader can accept all types of request, and should forward the requests to the Followers.

Here are some additional sorces:
1. https://hackernoon.com/distributed-data-store-and-transaction-sagas
2. https://hackernoon.com/understanding-partitioned-services-in-distributed-systems (not very usefull for this lab - you must implement only the Replication)
3. https://loud-orange-6fb.notion.site/Partition-Leader-Elections-and-re-elections-c0e9100c729b4fe4829c6025d4aae155?pvs=4 (my implementation of RAFT)
