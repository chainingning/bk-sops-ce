# -*- coding: utf-8 -*-
"""
Tencent is pleased to support the open source community by making 蓝鲸智云PaaS平台社区版 (BlueKing PaaS Community
Edition) available.
Copyright (C) 2017-2019 THL A29 Limited, a Tencent company. All rights reserved.
Licensed under the MIT License (the "License"); you may not use this file except in compliance with the License.
You may obtain a copy of the License at
http://opensource.org/licenses/MIT
Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on
an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the
specific language governing permissions and limitations under the License.
"""

from config import RUN_VER

if RUN_VER == 'open':
    from blueapps.patch.settings_open_saas import *  # noqa
else:
    from blueapps.patch.settings_paas_services import *  # noqa

# 本地开发环境Å
RUN_MODE = 'DEVELOP'
BK_CC_HOST = 'http://192.168.10.200:8083'

# APP本地静态资源目录
STATIC_URL = '/static/'

# APP静态资源目录url
# REMOTE_STATIC_URL = '%sremote/' % STATIC_URL

# Celery 消息队列设置 RabbitMQ
BROKER_URL = 'amqp://admin:admin@192.168.10.222:15672//'
# Celery 消息队列设置 Redis
#BROKER_URL = 'redis://127.0.0.1:6379/0'

DEBUG = False

# 本地开发数据库设置
# USE FOLLOWING SQL TO CREATE THE DATABASE NAMED APP_CODE
# SQL: CREATE DATABASE `bk_sops` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'bk_sops',
        'USER': 'root',
        'PASSWORD': '123456',
        'HOST': '192.168.10.222',
        'PORT': '3306',
        'OPTIONS': {
            "init_command": "SET sql_mode='STRICT_TRANS_TABLES'",
            },
        'TEST': {
            'NAME': 'bk_sops',
            'CHARSET': 'utf8',
            'COLLATION': 'utf8_general_ci',
        }
    },
}
REDIS = {
    'host': 'localhost',
    'port': 6379,
}
LOG_PERSISTENT_DAYS = 1

# CELERY_ALWAYS_EAGER = True
# TEST_RUNNER = 'djcelery.contrib.test_runner.' \
#               'CeleryTestSuiteRunnerStoringResult'

# 多人开发时，无法共享的本地配置可以放到新建的 local_settings.py 文件中
# 并且把 local_settings.py 加入版本管理忽略文件中
try:
    from local_settings import *  # noqa
except ImportError:
    pass
