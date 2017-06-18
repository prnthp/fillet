# fillet
Bishop's ROS Workspace

## Osiris Package
### Ganesh
Service that harvests information by invoking rosbag upon a *recordbegin* command.

Takes arguments: *command* filename [topics].

Valid commands: *recordbegin*, *recordend*

Filename: Any string - will be appended to front of rosbag filename. Directory is ~/Record/.

Topics: Given as array of strings

### Reaper
Service that kills and lets roslaunch resurrect /socket_node upon a "unityshutdown" on the input.

### Comms Test
Service that returns hex md5 digest of given string. Used to test communications with Unity before initiating experiments.
