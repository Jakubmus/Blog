# BLOG
A really simple blogging app in <b>Django</b>just for learning
# BUILDING AND LAUNCHING THE APPLICATION
You only need <b>Docker</b> to build this application
- Build a Docker image: <br>
`docker build -t <image name> .`
- Working application: <br>
`docker run -p 8000:8000 <image name>`
# CLOSING
To stop the application, type: <br>
`docker rm -f <container ID>` <br>
The <b>Container ID</b> can be found with: <br>
`ls docker container`