# Dynamic Reconfigure

Notes:

- naming convensions seem to matter
    - camel case
- project naming schemes to be consistent


## Process

- add project dependency on dynamic reconfigure
- configuration file (that makes use of ros msg)
- set up server and callback functions (in node)
- cmake file dependency, target config file, add dependency to configuration


## References

- http://wiki.ros.org/dynamic_reconfigure/Tutorials/SettingUpDynamicReconfigureForANode%28cpp%29
- https://github.com/UCSD-E4E/stingray-auv
- 