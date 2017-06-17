# fillet
Bishop's ROS Workspace

## Osiris Package
### Ganesh
Python script that harvests information by invoking rosbag upon a "recordbegin" from the /control topic.

TODO: Convert to service

### Reaper
Service that kills and lets roslaunch ressurect /socket_node upon a "unityshutdown" on the input.
Returns 1 if successful 0 if not.
