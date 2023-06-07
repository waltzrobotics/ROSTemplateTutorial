# repo_docker.sh
# last updated: 20210326 wjw
#
# description
#
# Notes:
#   - script functional with basic parameter update
#
# Revision:
#   1.0 Initial Version (20210324)
#   1.1 Established basic working version, master maintained in ROSDocker repository (20210326)
#   1.2  ()
#
# TODO:
#   - [ ] improve input parameters
#   - [ ] work on customizing general use build command using strings to simplify docker run commands
#
# Example usage:
#    - shell_script -param1
# 

# plan for input arguments: 
#   --update => update 
#   ability to specify type of docker image

while [ -n "$1" ]; do                                       # while loop starts
 
    case "$1" in
    
    -u) 
        param="$2"                                          # get positional value associated to paremeter flag
        #echo "-u (update) option passed with param=$param" # DEBUG ECHO
        update=1
        shift;;                                             # Remove parameter from input list
    -param2)
        param="$2"
        #echo "-param2 option passed with param=$param" 
        shift;;
    --)                                                     # handle -- parameter(s)
        shift # The double dash which separates options from parameters
 
        break
        ;;                                                  # exit the loop using break command
 
    *) echo "Option $1 not recognized" ;;                   # handle unknown cases
    esac                                                    # end case statement
    shift
done

cur_dir=$(pwd)
cur_dir="$(dirname "$cur_dir")"                             # get parent directory to scripts directory (repository root)
echo $cur_dir

if [ "$update" == 1 ]; then
    # update
    docker run -it --rm -v $cur_dir:/home/wwaltz/work --net=host --name waltz1 waltzbase:20.04
    #echo "running docker update command"
else
    echo "not update -- need to set standard docker run"
fi


# OLD DOCKER RUN COMMANDS

#docker run -it --rm -v /media/wwaltz/ISA-Work/_external_only/personal/repositories/ROSTemplateTutorial:/home/wwaltz/work --net=host --name waltz1 waltz:base
#docker run -it --rm -v /home/wwaltz/hdd/projects/ros_development/ROSTemplateTutorial_copied:/home/wwaltz/work --net=host --name waltz1 waltz:base
#docker run -it --rm -v /home/wwaltz/hdd/projects/ros_development/ROSTemplateTutorial:/home/wwaltz/work --net=host --name waltz1 waltz:base
#docker run -it --rm -v /home/wwaltz/hdd/projects/ROSTemplateTutorial:/home/wwaltz/work --net=host --name waltz1 waltz:base
