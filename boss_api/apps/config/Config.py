mysql_conf = {
    "admin_vue": {
        "default": {
            "max_connections": 20,
            "wait_connection_timeout": 3,
            "host": "118.31.74.55",
            "user": "root",
            "port": 3300,
            "password": "admin",
            "charset": "utf8"
        },
        "slave_1": {
        }
    }
}

redis_conf = {
    "admin_vue": {
        "default": {
            "max_connections": 20,
            "wait_connection_timeout": 3,
            "host": "118.31.74.55",
            "user": "root",
            "port": 6370,
            "password": "admin",
            "charset": "utf8"
        },
        "slave_1": {
        }
    }

}

mongo_conf = {
    "admin_vue": {
        "default": {
            "max_connections": 20,
            "wait_connection_timeout": 3,
            "host": "118.31.74.55",
            "user": "root",
            "port": 6370,
            "password": "admin",
            "charset": "utf8"
        },
        "slave_1": {
        },
        "local": {
            "host": "127.0.0.1",
            "port": 27017
        }
    }
}
