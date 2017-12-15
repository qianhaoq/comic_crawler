#!/bin/sh
# for((i=1;i<803;i++))
# set -x
for i in `seq -f "%03g" 802`
do
    cd images/${i}
    # echo ${i}
    n=`ls -l | wc -l`
    # echo $n
    if [ $n -lt 10 ]:
    then echo "${i} 图片不足"
    fi
    cd ../../
done
