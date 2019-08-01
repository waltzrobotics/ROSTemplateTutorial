# Service Example




```
roscore
```

```
rosrun cpp_service_example cpp_service_server_example
```

```
rosrun cpp_service_example add_two_ints_client 1 3
```

Results:

```
rosrun cpp_service_example cpp_service_client_example 1 3


[ INFO] [1563382684.295545818]: Sum: 4
```

From Server:

```
[ INFO] [1563382655.032078547]: Ready to add two ints.
[ INFO] [1563382684.295308270]: request: x=1, y=3
[ INFO] [1563382684.295360299]: sending back response: [4]
```