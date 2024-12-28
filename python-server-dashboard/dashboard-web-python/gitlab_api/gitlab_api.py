import gitlab
import json
from config.config_api import DashboardConfig
from db.models import ProjectGitInfo
from utils.log_utils import LogUtils

class GitlabApi:
    git = object()
    def __init__(self) -> None: # 无参构造方法
        self.config = DashboardConfig().get_config()
    def login(self):
        self.git = gitlab.Gitlab(url=self.config['gitlab']['url'], private_token=self.config['gitlab']['token'])
    def get_project_list(self): # git项目列表
        projects = self.git.projects.list(all=True)
        project_list = []
        LogUtils().info(">>>>>>>>>projects长度:{}",len(projects))
        for item in projects:
            project_list.append(ProjectGitInfo(item.id,item.name,item.path_with_namespace,item.description))
        return project_list
    def get_project_branches(self, project_id): # git branch
        project = self.git.projects.get(project_id)
        branche_list = project.branches.list()
        #print(json.dumps(branche_list))
        branches = []
        for item in branche_list:
            branches.append(item.attributes.get('name'))
            #print(item.attributes.get('name'))
        return branches