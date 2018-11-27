import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 将app添加到python扫描的路径中
sys.path.insert(0, os.path.join(BASE_DIR, 'apps'))

SECRET_KEY = 'or+v)%cqs*9nxb*%74g1e39g@tu8cfth80()txzg@hhyv+9mm9'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'apps.account',
    'apps.home',
    'apps.sort_movies',
    'captcha',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'taopiaopiao.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'taopiaopiao.wsgi.application'

'''
sql_mode有三种选项
ANSI 宽松模式 对插入的数据进行校验的时候，如果发现数据的长度或者类型不匹配，django会对数据类型进行调整，长度将会截取，开发里边慎用
TRADITIONAL 严格模式 能保证数据的准确性
STRICT_TRINS_TABLES 更严格模式

'''
# MYSQL_OPTIONS={
#     'sql_mode':'TRADITIONAL',
#     'charset':'utf8',
#     'init_command':'SET default_storage_engine=INNODB'
# }
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'tpp',
        'USER': 'root',
        'PASSWORD': 'root',
        'PORT': 3306,
        'HOST': '127.0.0.1'
    }
}

# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# 修改语言
LANGUAGE_CODE = 'zh-hans'
# 时区
TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True
# 是否使用django的时区
USE_TZ = False

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

#当使用继承的方式重写auth模块用户表的时候，需要指定一下
AUTH_USER_MODEL='account.User'

# ===============发送邮箱配置==========
# 发送邮件的服务器地址
EMAIL_HOST = 'smtp.163.com'
# 发送邮件端口
EMAIL_PORT = 25
# 发送邮件默认的名称
EMAIL_HOST_USER = 'm17538238049@163.com'
# 授权码
EMAIL_HOST_PASSWORD = 'python1805'
# 是否启用tls安全协议
EMAIL_USE_TLS = True

# 是否启用SSL安全协议
# EMAIL_USE_SSL = True
# 发送超时时间
# EMAIL_TIMEOUT =

# ===============发送邮箱配置 end ==========

###################redis缓存######################
# 缓存配置
CACHES = {
    "default": {
        # 使用redis做缓存
        'BACKEND': 'django_redis.cache.RedisCache',
        # 将缓存的数据保存在该目录下
        # 缓存的地址
        'LOCATION': 'redis://127.0.0.1:6379/1',
        # rediss: //[:password]@localhost:6379 / 0
        'TIMEOUT': 300,
        'OPTIONS': {
            # "PASSWORD": ""
            # 是否压缩缓存数据
            # "COMPRESSOR": "django_redis.compressors.zlib.ZlibCompressor",
            # 配置连接池
            "CONNECTION_POOL_KWARGS": {"max_connections": 100, "retry_on_timeout": True}
        }
    },
    'session': {
        # 指定缓存的类型是文件缓存
        'BACKEND': 'django_redis.cache.RedisCache',
        # 将缓存的数据保存在该目录下
        'LOCATION': 'redis://127.0.0.1:6379/15',
        'TIMEOUT': 300,
        'OPTIONS': {
            # "PASSWORD": ""
            # 是否压缩缓存数据(非必要)
            "COMPRESSOR": "django_redis.compressors.lzma.LzmaCompressor",
            # 配置连接池
            "CONNECTION_POOL_KWARGS": {"max_connections": 100, "retry_on_timeout": True}
        }
    },
}

# session使用redis座位缓存
SESSION_ENGINE = "django.contrib.sessions.backends.cache"
SESSION_CACHE_ALIAS = "session"

#配置验证码相关数据
CAPTCHA_CHALLENGE_FUNCT = 'captcha.helpers.math_challenge'



