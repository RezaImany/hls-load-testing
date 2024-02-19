# HLS Load Tester With Locust

As a member of a streaming service reliability team, one key challenge involved load testing HLS media streams and accurately simulating user viewing behavior. Over the years, I utilized various tools for this purpose, from headless browsers to specialized testing software.

Recently, I developed a new Python script using the Locust library to simulate video player interactions rather than approximate overall user actions. By focusing directly on the streaming video player API calls, I was able to achieve more precise and reproducible load testing results.

I'm sharing this Locust implementation in hopes that it may help others working to evaluate and improve streaming service resilience. By modeling player API patterns instead of user behaviors, this approach can provide valve engineering insights. Please feel free to leverage and modify this script as needed to suit your streaming load testing needs.

I'm happy to share this solution that I believe solves a common challenge for HLS video engineering teams.
# Docker Compose

As you may know, Locust is a single-threaded load testing tool. To leverage multi-threading and distributed loads, I've created a Docker Compose configuration that runs Locust in master-worker mode.

This Docker setup separates the single Locust master node from multiple worker nodes. Making workers scalable facilitates straightforward distributed load testing.

To scale up, simply adjust the number of desired worker nodes using the following command:

    docker-compose up --scale worker=<num_threads>

Where <num_threads> is the number of concurrent test threads you wish to run. This approach makes it easy to utilize the full parallel testing capacity of your available hardware.

By containerizing the Locust roles and cluster, we can now easily distribute the load generation for more realistic and demanding stress testing of our streaming video infrastructure.

Let me know if you have any other questions!
