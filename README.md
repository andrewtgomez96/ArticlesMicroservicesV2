# ArticlesMicroservicesV2
A continuation of the Articles Microservice project, but introducing a reverse proxy and load balancer, running multiple load-balanced instances of each microservice, and implementing the Backend for Frontend pattern to generate RSS feeds for your blog platform.

# Foreman
run this command to install nginx: "sudo apt install --yes nginx-extras"
run this command to install foreman: "sudo apt install --yes ruby-foreman"
run this command in the directory of the procfile: "foreman start --formation comments=3, articles=3, user=3, tag=3, rss=1" to start 3 services of each app.

# Nginx
Server blocks are set up in the etc/nginx/sites-enabled folder
Upstream is set up for each microservice to load balance the three apps that are running for each service from foreman --formation
Each microservice endpoint needs to be prefixed with the microservice name to the Nginx server on port 80. An example of this is supplied in the PDF in the repository under the Nginx heading





# RSS
To use RSS, open mail reader. Select 'Manage Subrcription'. Enter URL: http://localhost:5400/articles/rss . Press 'Add'.
