

```shell script
docker run -it --rm -v /media/wwaltz/ISA-Work/_external_only/personal/repositories/ROSTemplateTutorial:/home/wwaltz/work --net=host --name waltz1 waltz:base
docker run -it --rm -v /home/wwaltz/hdd/projects/ros_development/ROSTemplateTutorial_copied:/home/wwaltz/work --net=host --name waltz1 waltz:base

docker run -it --rm -v /home/wwaltz/hdd/projects/ros_development/ROSTemplateTutorial:/home/wwaltz/work --net=host --name waltz1 waltz:base
docker run -it --rm -v /home/wwaltz/hdd/projects/ROSTemplateTutorial:/home/wwaltz/work --net=host --name waltz1 waltz:base
```