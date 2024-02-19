As a member of a streaming service reliability team, one key challenge involved load testing HLS media streams and accurately simulating user viewing behavior. Over the years, I utilized various tools for this purpose, from headless browsers to specialized testing software.

Recently, I developed a new Python script using the Locust library to simulate video player interactions rather than approximate overall user actions. By focusing directly on the streaming video player API calls, I was able to achieve more precise and reproducible load testing results.

I'm sharing this Locust implementation in hopes that it may help others working to evaluate and improve streaming service resilience. By modeling player API patterns instead of user behaviors, this approach can provide valve engineering insights. Please feel free to leverage and modify this script as needed to suit your streaming load testing needs.

I'm happy to share this solution that I believe solves a common challenge for HLS video engineering teams. Let me know if you have any other questions!
