# ArticlesMicroservicesV2
A continuation of the Articles Microservice project, but introducing a reverse proxy and load balancer, running multiple load-balanced instances of each microservice, and implementing the Backend for Frontend pattern to generate RSS feeds for your blog platform.

# Foreman
run this command in the directory of the procfile: "foreman start --formation "comments=3, articles=3, user=3, tag=3"" to start 3 services of each app.
