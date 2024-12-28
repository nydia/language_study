#! /bin/sh
#接收外部参数
harbor_username=admin
harbor_passwd=Harbor12345
harbor_url=172.30.41.248
image_name=mengxiu-dashboard
env=dev
network_port=8088
container_port=8088
project_name=mengxiu-dashboard

# 发布
deploy() {
  imageName=$harbor_url/mengxiu/$env/$image_name:1.0.0

  echo "$imageName"

  #查询容器是否存在，存在则删除
  containerId=`sudo docker ps -a | grep -w ${image_name}  | awk '{print $1}'`
  if [ "$containerId" !=  "" ] ; then
    #停掉容器
    sudo docker stop $containerId

    #删除容器
    sudo docker rm $containerId

    echo "成功删除容器"
  fi

  #查询镜像是否存在，存在则删除
  imageId=`sudo docker images | grep -w $image_name  | awk '{print $3}'`

  if [ "$imageId" !=  "" ] ; then

    #删除镜像
    sudo docker rmi -f $imageId

    echo "成功删除镜像"
  fi

  # 登录Harbor
  sudo docker login -u $harbor_username -p $harbor_passwd $harbor_url

  # 下载镜像
  sudo docker pull $imageName

  # 启动容器
  sudo docker run -it -P -d -p $network_port:$container_port -v /opt/appl/spring-cloud/logs/$project_name:/opt/appl/spring-cloud/logs/$project_name -v /etc/ansible/hosts:/etc/ansible/hosts -v /etc/ansible/ansible.cfg:/etc/ansible/ansible.cfg --dns 8.8.8.8 --dns 8.8.4.4 --name $project_name $imageName

  echo "容器启动成功"

}

#发布容器
deploy