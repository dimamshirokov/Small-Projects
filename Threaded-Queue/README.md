<h1 align='center'> Threaded Queue </h1>

___

## 📰 Description

Flow pooling based on thread-safe queue.

### 👨🏻‍💻 What is done

Created a thread-safe queue storing functions intended for execution.
On the basis of this queue a thread pool is implemented.
This pool consists of a fixed number of worker threads equal to the number of hardware cores.
When a program has some work to do, it calls a function that places that work in the queue.
The worker thread takes the job from the queue, performs the task specified in it, and then checks if there are other jobs in the queue.

### ⌨️ Implemented classes

1. ThreadPool class is an implementation of a thread pool.

ThreadPool class fields:

- vector of threads that are initialized in the class constructor and destroyed in the destructor;
- thread-safe task queue for storing the work queue;
- other fields at the developer's discretion.

ThreadPool class methods:

- Work method - selects the next task from the queue and executes it. This method is passed to the thread constructor for execution;
- Submit method - places a task into the queue. The method can take either an object of the std::function template or an object of the package_task template as an argument;
- other methods are at the developer's discretion.

2. template class SafeQueue - implementation of a queue safe with respect to simultaneous access from several threads.
Fields of SafeQueue class:

- std::queue for storing tasks,
- std::mutex to implement locking,
- std::condtional_variables for notifications.

Methods of SafeQueue class:

- Push method - writes a new task to the beginning of the queue. It grabs a mutex, and when the operation is finished, the conditional variable is notified;
- Pop method - is pending until a notification to the conditional variable arrives. When the conditional variable is notified, the data is read from the queue.
- other methods are at the developer's discretion.

## 🚔 Run the program

In the folder /Small-Projects/Threaded-Queue/src, run the commands below.

```console
mkdir build
```
```console
cd build
```
```console
cmake ..
```
```console
make
```
```console
./threadedQueue
```

## 🥷🏻 Author

**Dima M. Shirokov**
- [GitHub](https://github.com/dimamshirokov)