# beta_基于机器学习的电影评论情感分析与研究系统

### 配置信息

  database: vm432_bf0a45f882b27e8f

  default port:9100

### 部署启动步骤

1. 激活python环境
2. 项目根目录下执行:
   3. 建库,建表,初始化administrator管理员密码,默认123456
   4. 启动项目,可用 123456 123456登入系统

# code

    check.bat
    init_project.bat
    start_project.bat

### 代码结构

 a_simulink_unit/generate_detect.py # 这个是算法处理部分

 appcenter/admin.py # 后台管理

 appcenter/models.py # 数据库表和字段定义

 config_busi/views.py # 前端增删改查

 config_visual/views.py # 大屏 你这个没有。

 sys_user/views.py  # 这里是登陆注册的

 templates/config_busi/auto_detect.html # 这个是图像合成的界面

 templates/login.html # 前端登录

 templates/register.html# 前端注册

 templates/index_v1.html # 前端 主页

# Spark

spark:3.0.2

python==3.8.18
pip==23.3.1
py4j==0.10.9
pyspark==3.0.2
setuptools==68.0.0
wheel==0.41.2




### 默认数据集在a_simulink_unit\data文件夹.

算法类的数据集同上,需要上传视频和图片的同上
