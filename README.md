# AirBnB_clone
### Expected web static for the final product:

<p align="center">
  <img src="https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/268/8-index.png">
</p>

### Web Stack for building the product:

<p align="center">
  <img src="https://i.imgur.com/lgZnZrz.png">
</p>

### Schemas:

<p align="center">
  <img src="https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/289/AirBnb_DB_diagramm.jpg">
</p>

---
## Part 1: 0x00. AirBnB clone - The console

![](./0x00-images/img_1.png)

Part 1 of AirBnB Clone project @Holberton: The goal of this project is to deploy a server with a simple copy of the AirBnB web app to demonstrate technical grasp (dare we say mastery?) of both front & backend development.

The overall Project scope is:

- Build a command line interpreter to manipulate data without a visual interface.
- A front-end (user interface) and a back-end for the web app: static and dynamic
- Data storage via a database or a file storage
- An API that bridges the front-end and the data (retrieve, create, delete, update)

### Objectives For The BaseModel Class: A Class that defines all common attributes/methods for other classes:

#### Public instance attributes:

- **id:** string - assign with an uuid when an instance is created

- **created_at:** The current datetime when an instance is created

- **updated_at:** The current datetime when an instance is created, updated every time you change your object

- **__str__:** should print: [<class name>] (<self.id>) <self.__dict__>

#### Public instance methods:
- save(self): updates the public instance with the current datetime
- to_dict(self): returns a dictionary containing all keys/values of __dict__ of the instance. This method will be the first piece of the serialization/deserialization process to JSON format.

### Objectives For The Command Line Interpreter:
- Create a new object (ex: a new User or a new Place)
- Retrieve an object from a file, a database etc…
- Do operations on objects (count, compute stats, etc…)
- Update attributes of an object
- Destroy an object

### Operating In Interactive Mode:
```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb)
(hbnb)
(hbnb) quit
$
```

### Operating In Non-Interactive Mode:
```
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
```
**Example Usage:**
```
newMod = BaseModel()
       - creates an instance of a method

print(NewMod.id)
	- prints the UUID
	   b6a6e15c-c67d-4312-9a75-9d084935e5

print(NewMod.created_at)
         - prints the time when the instance was created (ISO format)
	   '2017-09-28T21:03:54.052298'

print(NewMod.updated_at)
	- prints the most recent time that file was updated (ISO format)
       	  '2017-09-28T21:03:54.052302'
```
