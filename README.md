# Python Flask RESTful Server with Gunicorn 示例

Python version 3.8.7

## 本地部署

```
# 安装 pyenv
export v=3.8.7; wget https://npm.taobao.org/mirrors/python/$v/Python-$v.tar.xz -P ~/.pyenv/cache/; pyenv install $v

# 进入项目目录配置虚拟环境
cd python-flask-demo
pip install virtualenv
virtualenv -p ~/.pyenv/versions/3.8.7/bin/python venv

# 安装依赖包
source venv/bin/activate
pip install -r requirements.txt -i https://pypi.doubanio.com/simple/

# 本地调试运行
export FLASK_APP=main.py
flask run

# 或者本地 Gunicorn 运行
gunicorn -c gunicorn.conf main:app
```

## Docker 部署

```
# 进入项目目录构建项目镜像
cd python-flask-demo
docker build -t flask-demo .

# 启动已经构建的 Docker 镜像
docker run -e TZ="Asia/Shanghai" -d -p 80:80 --name my-flask-server flask-demo
```

## API 接口测试

查询全部 Authors

```
curl --location --request GET 'http://{{host}}/api/v1/authors'
```

创建 Author

```
curl --location --request POST 'http://{{host}}/api/v1/authors' \
--header 'Content-Type: application/json' \
--data-raw '{
    "name": "user1",
    "specialisation": "specialisation1"
}'
```

查询指定 ID 为 1 的 Author

```
curl --location --request GET 'http://127.0.0.1/api/v1/authors/1'
```


更新指定 ID 为 1 的 Author

```
curl --location --request PUT 'http://127.0.0.1:5000/api/v1/authors/1' \
--header 'Content-Type: application/json' \
--data-raw '{
    "name": "new name",
    "specialisation": "new specialisation"
}'
```

删除 ID 为 1 的 Author

```
curl --location --request DELETE 'http://127.0.0.1:5000/api/v1/authors/1'
```