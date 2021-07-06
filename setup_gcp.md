## star mysql
```
docker run -p 3306:3306 --name some-mysql -e MYSQL_ROOT_PASSWORD=root -d mysql:5.7
```

## create database
docker exec -it some-mysql sh
mysql -u root -p
```
CREATE DATABASE twittor CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```