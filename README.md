# ArticlesMicroservicesV2
A continuation of the Articles Microservice project, but introducing a reverse proxy and load balancer, running multiple load-balanced instances of each microservice, and implementing the Backend for Frontend pattern to generate RSS feeds for your blog platform.

# Foreman
run this command in the directory of the procfile: "foreman start --formation comments=3, articles=3, user=3, tag=3, rss=1" to start 3 services of each app.

# RSS
To use RSS, open mail reader. Select 'Manage Subrcription'. Enter URL: http://localhost:5400/articles/rss . Press 'Add'.
