# BLOG
A really simple blogging app in <b>Django</b> just for learning
# BUILDING AND LAUNCHING THE APPLICATION
You only need <b>Docker</b> to build this application
- Build a Docker image: <br>
`docker build -t UNIQUE_NAME .`
- Run the app: <br>
`docker run -p 8000:8000 UNIQUE_NAME`
# CLOSING
To stop the application, type: <br>
`docker stop <container ID>` <br>
The <b>Container ID</b> can be found with: <br>
`docker container ls`