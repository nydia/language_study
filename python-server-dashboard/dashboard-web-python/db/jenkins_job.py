import logging
from .models import JenkinsJob
from .db_connection import DbConnection
from datetime import datetime
from utils.log_utils import LogUtils

class JenkinsJobDb:
    def __init__(self) -> None:
        pass
    def get_job_list(self): # 获取任务列表
        _resource_list = []
        _conn = object()
        try:
            _conn = DbConnection().get_connection()
            # 创建一个 Cursor 对象
            with _conn.cursor() as cursor:
                _sql = "select * from tbl_jenkins_job where status = '1' order by id asc "
                cursor.execute(_sql)
                _data = cursor.fetchall() # 通过fetchall方法获得数据
                for row in _data:
                    _resource_list.append(self.job_row_handle(row))

            return _resource_list       
        except Exception as e:
            print("Error: unable to fetch data:",e)
        finally:
            # 关闭数据库连接
            _conn.close()

    def get_job_info_by_name(self,job_name): # 根据job_name获取任务信息
        _conn = object()
        try:
            _conn = DbConnection().get_connection()
            # 创建一个 Cursor 对象
            with _conn.cursor() as cursor:
                _sql = "select * from tbl_jenkins_job where job_name = %s "
                cursor.execute(_sql, (job_name))
                row  = cursor.fetchone()
                if row:
                    return self.job_row_handle(row)

        except Exception as e:
            print("Error: unable to fetch data, ", e)
        finally:
            # 关闭数据库连接
            _conn.close()

    def get_job_info_by_id(self,id): # 根据id获取任务信息
        _conn = object()
        try:
            _conn = DbConnection().get_connection()
            # 创建一个 Cursor 对象
            with _conn.cursor() as cursor:
                _sql = "select * from tbl_jenkins_job where id = %s "
                cursor.execute(_sql, (id))
                row  = cursor.fetchone()
                if row:
                    return self.job_row_handle(row)

        except Exception as e:
            print("Error: unable to fetch data, ", e)
        finally:
            # 关闭数据库连接
            _conn.close()
            
    def job_row_handle(self,row): # 处理数据库行，返回job 信息
        # JenkinsJob(row['id'],row['job_name'],row['deploy_host'],row['deploy_tm'],row['deploy_option'],row['branch'],row['env'],row['pit_auto_apply'],row['create_tm'],row['status'])
        _job = JenkinsJob()
        _job.id = row['id']
        _job.job_name = row['job_name']
        _job.deploy_host_sit = row['deploy_host_sit']
        _job.deploy_host_dev = row['deploy_host_dev']
        _job.deploy_tm = row['deploy_tm']
        _job.deploy_option = row['deploy_option']
        _job.branch = row['branch']
        _job.env = row['env']
        _job.pit_auto_apply = row['pit_auto_apply']
        _job.project_id = row['project_id']
        _job.create_tm = row['create_tm']
        _job.status = row['status']
        _job.type = row['type']
        _job.image_name = row['image_name']
        _job.env_dev_status = row['env_dev_status']
        _job.env_sit_status = row['env_sit_status']
        _job.env_pit_status = row['env_pit_status']
        _job.update_tm = row['update_tm']
        return _job

    def update_job_by_jobname(self,job): # 更新任务信息 以 job_name 为条件
        print(">>>>>>更新任务信息开始")
        _update_result = 0
        try:
            _conn = DbConnection().get_connection()
             # 创建游标对象
            with _conn.cursor() as cursor:

                update_fields = self.build_update_field(job)

                # 构建更新 SQL 语句
                table = 'tbl_jenkins_job'
                set_clause = ', '.join([f"{field} = %s" for field in update_fields.keys()])
                update_query = f"UPDATE {table} SET {set_clause} WHERE job_name = %s"

                # 将字段值添加到参数中
                update_values = list(update_fields.values())
                update_values.append(job.job_name)

                _update_result = cursor.execute(update_query, tuple(update_values))
                _conn.commit()

                #print("更新数据库的结果>>>>>>:", _update_result)
                #print("Machine information updated successfully.")

        except Exception as e:
            print(">>>>>byName更新数据库失败：", e)
            logging.info("获取机器的数据库信息错误，错误原因：{}".format(e)) 
        finally:
            # 关闭数据库连接
            _conn.close()   
        return _update_result

    def update_job_by_id(self,job): # 更新任务信息 以 id 为条件
        print(">>>>>>更新任务信息开始")
        _update_result = 0
        try:
            _conn = DbConnection().get_connection()
             # 创建游标对象
            with _conn.cursor() as cursor:

                update_fields = self.build_update_field(job)

                # 构建更新 SQL 语句
                table = 'tbl_jenkins_job'
                set_clause = ', '.join([f"{field} = %s" for field in update_fields.keys()])
                update_query = f"UPDATE {table} SET {set_clause} WHERE id = %s"

                # 将字段值添加到参数中
                update_values = list(update_fields.values())
                update_values.append(job.id)
                
                _update_result = cursor.execute(update_query, tuple(update_values))
                _conn.commit()

                #print("更新数据库的结果>>>>>>:", _update_result)
                #print("Machine information updated successfully.")

        except Exception as e:
            print(">>>>>byId更新数据库失败：", e)
            logging.info("获取机器的数据库信息错误，错误原因：{}".format(e)) 
        finally:
            # 关闭数据库连接
            _conn.close()   
        return _update_result

    def build_update_field(self,job): # 构建更新字段
        update_fields = {}
        if hasattr(job,"deploy_option") and job.deploy_option is not None:
            update_fields['deploy_option'] = job.deploy_option
        if hasattr(job,"branch") and job.branch is not None:
            update_fields['branch'] = job.branch
        if hasattr(job,"env") and job.env is not None:
            update_fields['env'] = job.env
        if hasattr(job,"pit_auto_apply") and job.pit_auto_apply is not None:
            update_fields['pit_auto_apply'] = job.pit_auto_apply
        if hasattr(job,"status") and job.status is not None:
            update_fields['status'] = job.status
        if hasattr(job,"deploy_tm") and job.deploy_tm is not None:
            update_fields['deploy_tm'] = job.deploy_tm
        if hasattr(job,"project_id") and job.project_id is not None:
            update_fields['project_id'] = job.project_id
        if hasattr(job,"image_name") and job.image_name is not None:
            update_fields['image_name'] = job.image_name
        if hasattr(job,"env_dev_status") and job.env_dev_status is not None:
            update_fields['env_dev_status'] = job.env_dev_status
        if hasattr(job,"env_sit_status") and job.env_sit_status is not None:
            update_fields['env_sit_status'] = job.env_sit_status
        if hasattr(job,"env_pit_status") and job.env_pit_status is not None:
            update_fields['env_pit_status'] = job.env_pit_status

        # 获取当前时间
        current_time = datetime.now()
        update_tm = current_time.strftime("%Y-%m-%d %H:%M:%S")
        update_fields['update_tm'] = update_tm

        return update_fields        

    def insert_job(self,job): # 插入任务信息
        print("插入任务信息开始>>>>>>")
        _insert_result = 0
        try:
            _conn = DbConnection().get_connection()
             # 创建游标对象
            with _conn.cursor() as cursor:

                _sql = " insert into tbl_jenkins_job(job_name,create_tm) values(%s,%s) "

                # 获取当前时间
                current_time = datetime.now()
                create_tm = current_time.strftime("%Y-%m-%d %H:%M:%S")

                # 执行更新操作
                _insert_result = cursor.execute(_sql, (job.job_name, create_tm))
                # 提交事务
                _conn.commit()

                print("插入数据库的结果>>>>>>:", _insert_result)
                print("JenkinsJob information updated successfully.")

        except Exception as e:
            print(">>>>>更新数据库失败：", e)
            logging.info("获取机器的数据库信息错误，错误原因：{}".format(e)) 
        finally:
            # 关闭数据库连接
            _conn.close()
        return _insert_result

    def update_job_deploy_info(self,job): # 更新任务信息发布任务信息
        LogUtils().info("发布任务更新信息>>>>>>")
        # 获取当前时间
        current_time = datetime.now()
        job.deploy_tm = current_time.strftime("%Y-%m-%d %H:%M:%S")
        _result = self.update_job_by_id(job)
        LogUtils().info(">>>>>>更新项目git仓库信息结果: {}", _result)
        return _result

    def update_job_git_info(self,job): # 更新项目的git信息
        LogUtils().info(">>>>>>更新项目git仓库信息")
        _result = self.update_job_by_id(job)
        LogUtils().info(">>>>>>更新项目git仓库信息结果: {}", _result)
        return _result

    def update_job_server_state(self,job): # 更新应用状态结果
        LogUtils().info(">>>>>>更新应用状态")
        _result = self.update_job_by_id(job)
        LogUtils().info(">>>>>>更新应用状态结果: {}", _result)
        return _result