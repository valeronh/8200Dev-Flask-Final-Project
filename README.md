# Course Attendance Application # 

**Description:**
#### Webex class attendance calculative application ####
- Raw csv files according to classes attendance are downloaded from a remote Amazon server.
- The data is processed by attendance algorithm written by Yona Bloy - https://github.com/natibloy/bynet.
- The processed data is stored in Mysql database.
- The data is presented in a web server over port 5000 using Flask Framework.
- The application is dockerized and the image uploaded to Docker-hub: https://hub.docker.com/r/valeron12345/flask_app.
- Docker-Compose runs the application and mysql server in 2 network sharing containers.

**Requirements:**
- Docker
- Docker-Compose

**Installation:**
- Clone the repository: `git clone https://github.com/valeronh/flaskexample.git`
- Create `.env` file in your local repository that will contain:
  
    | Variable: | Explanation: |
    | :-------: | :----------: |
    | MYSQL_HOST | Choose MYSQL HOST name |
    | MYSQL_USER | Choose MYSQL USER name |
    | MYSQL_PASSWORD | Choose MYSQL PASSWORD |
    | MYSQL_DATABASE | Choose MYSQL DATABASE name |
    | CLOUD_HOSTNAME | Write remote machine IP |
    | CLOUD_USERNAME | Write remote macchine USERNAME |
    | CLOUD_PASSWORD | Write remote machine PASSWORD |
    | CLOUD_PATH | Write the path to files directory on the remote machine |
  
- Table creation commad(The table is created automatically):
    - `CREATE TABLE IF NOT EXISTS owner(id INT NOT NULL AUTO_INCREMENT, name VARCHAR(30), average VARCHAR(20), PRIMARY KEY(id))`

**Run The Application:**
- `docker-compose up -d`
- Open your web browser and type: `YOUR IP:5000`
