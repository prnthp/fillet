# fillet
Bishop's ROS Workspace

## Osiris Package
### Ganesh
Service that harvests information by invoking rosbag upon a "recordbegin" command, takes arguments: command filename [topics]. Giving command "recordend" kills all rosbag nodes.

### Reaper
Service that kills and lets roslaunch ressurect /socket_node upon a "unityshutdown" on the input.
Returns 1 if successful 0 if not.
