import logging
from .models import Machine
from .db_connection import DbConnection
from utils.log_utils import LogUtils

"""
Linux服务器信息本地数据库存储
"""
class MachineDb:
    conn = object()
    def __init__(self) -> None:
        pass

    def get_machine_list(self):
        _resource_list = []
        _conn = object()
        try:
            _conn = DbConnection().get_connection()
            # 创建一个 Cursor 对象
            with _conn.cursor() as cursor:
                _sql = "select * from tbl_machine_resources where status = '1' order by id asc "
                cursor.execute(_sql)
                _data = cursor.fetchall() # 通过fetchall方法获得数据

                for row in _data:
                    machine = Machine(row['id'],row['ip'],row['cpu_total'],row['cpu_use'],row['cpu_rate'],row['mem_total'],row['mem_use'],row['mem_free'],row['mem_available'],row['env'],row['status'],row['remark'])
                    _resource_list.append(machine)
                #print(_resource_list)
        except:
            LogUtils().info("Error: unable to fetch data")
        finally:
            # 关闭数据库连接
            _conn.close()

        # 处理返回的结果的内存的单位
        #return _resource_list
        return self.handle_machine_list(_resource_list)

    def get_machine_info(self,machine_id):
        LogUtils().info(">>>>>>获取信息开始")
        _machine_info = object()
        try:
            _conn = DbConnection().get_connection()
            # 创建一个 Cursor 对象
            with _conn.cursor() as cursor:
                _sql = "select * from tbl_machine_resources where status = '1' and id = %s order by id asc "
                cursor.execute(_sql, (machine_id))
                row  = cursor.fetchone()

                if row:
                    _machine_info = Machine(row['id'],row['ip'],row['cpu_total'],row['cpu_use'],row['cpu_rate'],row['mem_total'],row['mem_use'],row['mem_free'],row['mem_available'],row['env'],row['status'],row['remark'])
                else:
                    print("No more rows in the result set.")
        except Exception as e:
            LogUtils().info("从DB获取机器的信息错误，错误原因：{}", e) 
        finally:
            # 关闭数据库连接
            _conn.close()
        return  _machine_info
    def update_machine_info(self,machine_info): # 更新机器信息
        LogUtils().info(">>>>>>更新机器信息开始")
        _update_result = 0
        try:
            _conn = DbConnection().get_connection()
             # 创建游标对象
            cursor = _conn.cursor()

            _sql = "update tbl_machine_resources set cpu_total=%s,cpu_use=%s,cpu_rate=%s,mem_total=%s,mem_use=%s,mem_free=%s,mem_available=%s where id = %s "
            cpu_total = machine_info.cpu_total if machine_info.cpu_total is not None else 0
            cpu_use = machine_info.cpu_use if machine_info.cpu_use is not None else 0
            cpu_rate = machine_info.cpu_rate if machine_info.cpu_rate is not None else 0
            mem_total = machine_info.mem_total if machine_info.mem_total is not None else 0
            mem_use = machine_info.mem_use if machine_info.mem_use is not None else 0
            mem_free = machine_info.mem_free if machine_info.mem_free is not None else 0
            mem_available = machine_info.mem_available if machine_info.mem_available is not None else 0
            id = machine_info.id

            # 执行更新操作
            _update_result = cursor.execute(_sql, (cpu_total, cpu_use, cpu_rate, mem_total, mem_use, mem_free, mem_available, id))
            # 提交事务
            _conn.commit()

            #print("更新数据库的结果>>>>>>:", _update_result)
            #print("Machine information updated successfully.")

        except Exception as e:
            LogUtils().info("更新数据库的机器的信息错误，错误原因：{}", e) 
        finally:
            # 关闭数据库连接
            _conn.close()   
        return _update_result
    def handle_machine_list(self, machine_list): # 转换内存的单位 kb -> mb
        if machine_list is None:
            return machine_list
        _machine_list = []
        for re in machine_list:
            re.mem_total = round(re.mem_total/1024, 2) if re.mem_total is not None else 0
            re.mem_use = round(re.mem_use/1024, 2) if re.mem_use is not None else 0
            re.mem_free = round(re.mem_free/1024, 2) if re.mem_free is not None else 0
            re.mem_available = round(re.mem_available/1024, 2) if re.mem_available is not None else 0

            _machine_list.append(re)
        return _machine_list

