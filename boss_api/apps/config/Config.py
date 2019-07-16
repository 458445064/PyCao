
mysql_conf = {
    "vue": {
        "default": {
            "max_connections": 20,
            "wait_connection_timeout": 3,
            # "host": "mysql.zhugefang.com",
            # "user": "dm_rw",
            # "passwd": "CszwRk3breCsM5BCH0yDfHLorJM5QB5T",
            # "port": 9571,
            "host": "47.92.206.60",
            "user": "root",
            "port": 3306,
            "password": "123456",
            "charset": "utf8"
        },
        "slave_1": {
            "max_connections": 20,
            "wait_connection_timeout": 3,
            # "host": "mysql.zhugefang.com",
            # "user": "dm_rw",
            # "passwd": "CszwRk3breCsM5BCH0yDfHLorJM5QB5T",
            # "port": 9571,
            "host": "47.92.206.60",
            "user": "root",
            "port": 3306,
            "passwd": "123456",
            "charset": "utf8"
        }
    }
}

redis_conf = {
}

mongo_conf = {
}