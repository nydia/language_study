-- 初始化数据
create database mengxiu_dashboard;
GRANT ALL ON mengxiu_dashboard.* TO 'test'@'%';
use mengxiu_dashboard;
drop table if exists tbl_machine_resources;
CREATE TABLE `tbl_machine_resources` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT 'id',
  `ip` varchar(64) DEFAULT '' COMMENT '机器IP',
  `cpu_total` float(10,2) DEFAULT '0.00' COMMENT 'CPU总数',
  `cpu_use` float(10,2) DEFAULT '0.00' COMMENT 'CPU已使用',
  `cpu_rate` float(10,2) DEFAULT '0.00' COMMENT 'CPU使用率',
  `mem_total` int(8) DEFAULT '0' COMMENT '总内存',
  `mem_use` int(8) DEFAULT '0' COMMENT '已用内存',
  `mem_free` int(8) DEFAULT '0' COMMENT '自由内存',
  `mem_available` int(8) DEFAULT '0' COMMENT '可用内存',
  `env` varchar(10) DEFAULT '' COMMENT 'dev-开发/sit-测试/uat-预生产/pit-生产',
  `status` char(1) DEFAULT '1' COMMENT '状态 1-启动/0-禁用',
  `careate_tm` varchar(20) DEFAULT '' COMMENT '创建时间 yyyy-MM-dd HH:MM:SS',
  `remark` varchar(256) DEFAULT '' COMMENT '备注',
  PRIMARY KEY (`id`)
);

drop table if exists tbl_jenkins_job;
CREATE TABLE `tbl_jenkins_job` (
  `id` int(8) NOT NULL AUTO_INCREMENT COMMENT '唯一性ID',
  `job_name` varchar(64) DEFAULT '' COMMENT 'job名称',
  `deploy_host_sit` varchar(255) DEFAULT '' COMMENT '发布job的机器IP(SIT)',
  `deploy_host_dev` varchar(255) DEFAULT '' COMMENT '发布job的机器IP(DEV)',
  `deploy_tm` varchar(20) DEFAULT '' COMMENT '发布时间',
  `deploy_option` varchar(10) DEFAULT '' COMMENT '发布选项 deploy/rollback/restart',
  `branch` varchar(64) DEFAULT '' COMMENT '分支',
  `env` varchar(20) DEFAULT '' COMMENT '环境 dev/sit/uat/pit',
  `pit_auto_apply` varchar(1) DEFAULT '' COMMENT '是否发布阿里云 1-是/0-否',
  `project_id` varchar(10) DEFAULT '' COMMENT 'git项目ID',
  `create_tm` varchar(20) DEFAULT '' COMMENT '创建时间',
  `status` varchar(1) DEFAULT '0' COMMENT '应用状态 1-是/0-否',
  `type` varchar(20) DEFAULT '' COMMENT '前端/后端',
  `image_name` varchar(64) DEFAULT '' COMMENT '应用镜像名称',
  `env_dev_status` varchar(10) DEFAULT '' COMMENT '应用服务状态:RUNNING-正常/ERROR-错误',
  `env_sit_status` varchar(10) DEFAULT '' COMMENT '应用服务状态:RUNNING-正常/ERROR-错误',
  `env_pit_status` varchar(10) DEFAULT '' COMMENT '应用服务状态:RUNNING-正常/ERROR-错误',
  `update_tm` varchar(20) COLLATE utf8mb4_bin DEFAULT '' COMMENT '更新时间',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=15;

drop table if exists tbl_admin_user;
CREATE TABLE `tbl_admin_user` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `username` VARCHAR(64) DEFAULT NULL,
  `password` VARCHAR(64) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=INNODB AUTO_INCREMENT=1;;

delete from tbl_machine_resources;
insert into `tbl_machine_resources` (`id`, `ip`, `cpu_total`, `cpu_use`, `cpu_rate`, `mem_total`, `mem_use`, `mem_free`, `mem_available`, `env`, `status`, `careate_tm`, `remark`) values('1','10.200.200.145','0.00','0.00',NULL,'0','0','0','0','dev-sh','1','2023-08-21 14:00:00','');
insert into `tbl_machine_resources` (`id`, `ip`, `cpu_total`, `cpu_use`, `cpu_rate`, `mem_total`, `mem_use`, `mem_free`, `mem_available`, `env`, `status`, `careate_tm`, `remark`) values('2','172.30.42.10','0.00','0.00',NULL,'0','0','0','0','sit','1','2023-08-21 14:00:00','');
insert into `tbl_machine_resources` (`id`, `ip`, `cpu_total`, `cpu_use`, `cpu_rate`, `mem_total`, `mem_use`, `mem_free`, `mem_available`, `env`, `status`, `careate_tm`, `remark`) values('3','172.30.42.11','0.00','0.00',NULL,'0','0','0','0','sit','1','2023-08-21 14:00:00','');
insert into `tbl_machine_resources` (`id`, `ip`, `cpu_total`, `cpu_use`, `cpu_rate`, `mem_total`, `mem_use`, `mem_free`, `mem_available`, `env`, `status`, `careate_tm`, `remark`) values('4','172.30.42.12','0.00','0.00',NULL,'0','0','0','0','sit','1','2023-08-21 14:00:00','');
insert into `tbl_machine_resources` (`id`, `ip`, `cpu_total`, `cpu_use`, `cpu_rate`, `mem_total`, `mem_use`, `mem_free`, `mem_available`, `env`, `status`, `careate_tm`, `remark`) values('5','172.30.42.13','0.00','0.00',NULL,'0','0','0','0','sit','1','2023-08-21 14:00:00','');
insert into `tbl_machine_resources` (`id`, `ip`, `cpu_total`, `cpu_use`, `cpu_rate`, `mem_total`, `mem_use`, `mem_free`, `mem_available`, `env`, `status`, `careate_tm`, `remark`) values('6','172.30.42.14','0.00','0.00',NULL,'0','0','0','0','sit','1','2023-08-21 14:00:00','');
insert into `tbl_machine_resources` (`id`, `ip`, `cpu_total`, `cpu_use`, `cpu_rate`, `mem_total`, `mem_use`, `mem_free`, `mem_available`, `env`, `status`, `careate_tm`, `remark`) values('7','172.30.42.15','0.00','0.00',NULL,'0','0','0','0','sit','1','2023-08-21 14:00:00','');
insert into `tbl_machine_resources` (`id`, `ip`, `cpu_total`, `cpu_use`, `cpu_rate`, `mem_total`, `mem_use`, `mem_free`, `mem_available`, `env`, `status`, `careate_tm`, `remark`) values('8','172.30.42.16','0.00','0.00',NULL,'0','0','0','0','sit','1','2023-08-21 14:00:00','');
insert into `tbl_machine_resources` (`id`, `ip`, `cpu_total`, `cpu_use`, `cpu_rate`, `mem_total`, `mem_use`, `mem_free`, `mem_available`, `env`, `status`, `careate_tm`, `remark`) values('9','172.30.41.236','0.00','0.00',NULL,'0','0','0','0','dev','1','2023-08-21 14:00:00','');
insert into `tbl_machine_resources` (`id`, `ip`, `cpu_total`, `cpu_use`, `cpu_rate`, `mem_total`, `mem_use`, `mem_free`, `mem_available`, `env`, `status`, `careate_tm`, `remark`) values('10','172.30.41.10','0.00','0.00',NULL,'0','0','0','0','dev','1','2023-08-21 14:00:00','');
insert into `tbl_machine_resources` (`id`, `ip`, `cpu_total`, `cpu_use`, `cpu_rate`, `mem_total`, `mem_use`, `mem_free`, `mem_available`, `env`, `status`, `careate_tm`, `remark`) values('11','172.30.41.11','0.00','0.00',NULL,'0','0','0','0','dev','1','2023-08-21 14:00:00','');
insert into `tbl_machine_resources` (`id`, `ip`, `cpu_total`, `cpu_use`, `cpu_rate`, `mem_total`, `mem_use`, `mem_free`, `mem_available`, `env`, `status`, `careate_tm`, `remark`) values('12','172.30.41.12','0.00','0.00',NULL,'0','0','0','0','dev','1','2023-08-21 14:00:00','');
insert into `tbl_machine_resources` (`id`, `ip`, `cpu_total`, `cpu_use`, `cpu_rate`, `mem_total`, `mem_use`, `mem_free`, `mem_available`, `env`, `status`, `careate_tm`, `remark`) values('13','172.30.41.13','0.00','0.00',NULL,'0','0','0','0','dev','1','2023-08-21 14:00:00','');
insert into `tbl_machine_resources` (`id`, `ip`, `cpu_total`, `cpu_use`, `cpu_rate`, `mem_total`, `mem_use`, `mem_free`, `mem_available`, `env`, `status`, `careate_tm`, `remark`) values('14','172.30.41.14','0.00','0.00',NULL,'0','0','0','0','dev','1','2023-08-21 14:00:00','');
insert into `tbl_machine_resources` (`id`, `ip`, `cpu_total`, `cpu_use`, `cpu_rate`, `mem_total`, `mem_use`, `mem_free`, `mem_available`, `env`, `status`, `careate_tm`, `remark`) values('15','172.30.41.15','0.00','0.00',NULL,'0','0','0','0','dev','1','2023-08-21 14:00:00','');
insert into `tbl_machine_resources` (`id`, `ip`, `cpu_total`, `cpu_use`, `cpu_rate`, `mem_total`, `mem_use`, `mem_free`, `mem_available`, `env`, `status`, `careate_tm`, `remark`) values('16','172.30.41.16','0.00','0.00',NULL,'0','0','0','0','dev','1','2023-08-21 14:00:00','');


delete from tbl_jenkins_job;
insert into `tbl_jenkins_job` (`id`, `job_name`, `deploy_host_sit`, `deploy_host_dev`, `deploy_tm`, `deploy_option`, `branch`, `env`, `pit_auto_apply`, `project_id`, `create_tm`, `status`, `type`, `image_name`, `env_dev_status`, `env_sit_status`, `env_pit_status`, `update_tm`) values('1','channel-docker(暂不用)','','','','','','','','394','2023-08-24 13:51:48','0','后端','','','','','');
insert into `tbl_jenkins_job` (`id`, `job_name`, `deploy_host_sit`, `deploy_host_dev`, `deploy_tm`, `deploy_option`, `branch`, `env`, `pit_auto_apply`, `project_id`, `create_tm`, `status`, `type`, `image_name`, `env_dev_status`, `env_sit_status`, `env_pit_status`, `update_tm`) values('2','gold-h5-pipeline(用户)','172.30.42.63','10.200.200.145','','','','','','386','2023-08-24 13:51:48','1','前端','','','','','');
insert into `tbl_jenkins_job` (`id`, `job_name`, `deploy_host_sit`, `deploy_host_dev`, `deploy_tm`, `deploy_option`, `branch`, `env`, `pit_auto_apply`, `project_id`, `create_tm`, `status`, `type`, `image_name`, `env_dev_status`, `env_sit_status`, `env_pit_status`, `update_tm`) values('3','gold-user-pipeline(用户)','172.30.42.12','10.200.200.145','','','','','','385','2023-08-24 13:51:48','1','后端','gold-user','','','','');
insert into `tbl_jenkins_job` (`id`, `job_name`, `deploy_host_sit`, `deploy_host_dev`, `deploy_tm`, `deploy_option`, `branch`, `env`, `pit_auto_apply`, `project_id`, `create_tm`, `status`, `type`, `image_name`, `env_dev_status`, `env_sit_status`, `env_pit_status`, `update_tm`) values('4','ips-sms-pit(暂不用)','','','','','','','','','2023-08-24 13:51:48','0','后端','','','','','');
insert into `tbl_jenkins_job` (`id`, `job_name`, `deploy_host_sit`, `deploy_host_dev`, `deploy_tm`, `deploy_option`, `branch`, `env`, `pit_auto_apply`, `project_id`, `create_tm`, `status`, `type`, `image_name`, `env_dev_status`, `env_sit_status`, `env_pit_status`, `update_tm`) values('5','meng-pay-gateway-pipeline(支付网关)','172.30.42.15','10.200.200.145','','','','','','387','2023-08-24 13:51:48','1','后端','pay-gateway','','','','');
insert into `tbl_jenkins_job` (`id`, `job_name`, `deploy_host_sit`, `deploy_host_dev`, `deploy_tm`, `deploy_option`, `branch`, `env`, `pit_auto_apply`, `project_id`, `create_tm`, `status`, `type`, `image_name`, `env_dev_status`, `env_sit_status`, `env_pit_status`, `update_tm`) values('6','mengxiu-channel-pipeline(渠道)','172.30.42.14','10.200.200.145','','','','','','388','2023-08-24 13:51:48','1','后端','mengxiu-channel','','','','');
insert into `tbl_jenkins_job` (`id`, `job_name`, `deploy_host_sit`, `deploy_host_dev`, `deploy_tm`, `deploy_option`, `branch`, `env`, `pit_auto_apply`, `project_id`, `create_tm`, `status`, `type`, `image_name`, `env_dev_status`, `env_sit_status`, `env_pit_status`, `update_tm`) values('7','mengxiu-channel-多环境(仅做参考)','','','','','','','','388','2023-08-24 13:51:48','0','后端','','','','','');
insert into `tbl_jenkins_job` (`id`, `job_name`, `deploy_host_sit`, `deploy_host_dev`, `deploy_tm`, `deploy_option`, `branch`, `env`, `pit_auto_apply`, `project_id`, `create_tm`, `status`, `type`, `image_name`, `env_dev_status`, `env_sit_status`, `env_pit_status`, `update_tm`) values('8','mengxiu-demo-pipeline','172.30.42.16','10.200.200.145','','','','','','393','2023-08-24 13:51:48','1','后端','mengxiu-demo','','','','');
insert into `tbl_jenkins_job` (`id`, `job_name`, `deploy_host_sit`, `deploy_host_dev`, `deploy_tm`, `deploy_option`, `branch`, `env`, `pit_auto_apply`, `project_id`, `create_tm`, `status`, `type`, `image_name`, `env_dev_status`, `env_sit_status`, `env_pit_status`, `update_tm`) values('9','mengxiu-h5-demo-pipeline','172.30.42.63','10.200.200.145','','','','','','','2023-08-24 13:51:48','1','前端','','','','','');
insert into `tbl_jenkins_job` (`id`, `job_name`, `deploy_host_sit`, `deploy_host_dev`, `deploy_tm`, `deploy_option`, `branch`, `env`, `pit_auto_apply`, `project_id`, `create_tm`, `status`, `type`, `image_name`, `env_dev_status`, `env_sit_status`, `env_pit_status`, `update_tm`) values('10','mengxiu-h5-freestyle(暂不用)','','','','','','','','','2023-08-24 13:51:48','0','前端','','','','','');
insert into `tbl_jenkins_job` (`id`, `job_name`, `deploy_host_sit`, `deploy_host_dev`, `deploy_tm`, `deploy_option`, `branch`, `env`, `pit_auto_apply`, `project_id`, `create_tm`, `status`, `type`, `image_name`, `env_dev_status`, `env_sit_status`, `env_pit_status`, `update_tm`) values('11','mengxiu-paddle(挡版)','172.30.42.14','10.200.200.145','','','','','','392','2023-08-24 13:51:48','1','后端','mengxiu-paddle','','','','');
insert into `tbl_jenkins_job` (`id`, `job_name`, `deploy_host_sit`, `deploy_host_dev`, `deploy_tm`, `deploy_option`, `branch`, `env`, `pit_auto_apply`, `project_id`, `create_tm`, `status`, `type`, `image_name`, `env_dev_status`, `env_sit_status`, `env_pit_status`, `update_tm`) values('12','mengxiu-risk-pipeline(风控)','172.30.42.11','10.200.200.145','','','','','','389','2023-08-24 13:51:48','1','后端','mengxiu-risk','','','','');
insert into `tbl_jenkins_job` (`id`, `job_name`, `deploy_host_sit`, `deploy_host_dev`, `deploy_tm`, `deploy_option`, `branch`, `env`, `pit_auto_apply`, `project_id`, `create_tm`, `status`, `type`, `image_name`, `env_dev_status`, `env_sit_status`, `env_pit_status`, `update_tm`) values('13','mengxiu-task-pipeline(任务)','172.30.42.15','10.200.200.145','','','','','','390','2023-08-24 13:51:48','1','后端','mengxiu-task','','','','');
insert into `tbl_jenkins_job` (`id`, `job_name`, `deploy_host_sit`, `deploy_host_dev`, `deploy_tm`, `deploy_option`, `branch`, `env`, `pit_auto_apply`, `project_id`, `create_tm`, `status`, `type`, `image_name`, `env_dev_status`, `env_sit_status`, `env_pit_status`, `update_tm`) values('14','pipeline_demo1(暂不用)','','','','','','','','','2023-08-24 13:51:48','0','后端','','','','','');
