## ttk_docker

This repository contains all the necessary files to create a Docker container for the TARSQI Toolkit (TTK). TTK is used for temporal processing of natural language text, including tasks such as temporal tagging and event extraction. This containerized version includes a Flask-based web server (server.py) that exposes an API to receive text input and document creation time (DCT), and returns TARSQI-annotated string output.

*Features:*

Containerized version of the TARSQI Toolkit for temporal text processing.
Flask-based API for easy interaction and integration with other services.
Supports text input and document creation time (DCT) as parameters.

*Requirements:* The following dependencies are installed via requirements.txt:

Flask==2.2.2
future==0.18.3
requests==2.28.2
six==1.16.0
spacy==3.5.0


*Installation:*


1. Clone the repository:
git clone https://github.com/neostrange/ttk_docker.git
cd ttk_docker

2. Build the Docker image:
   docker build -t ttk-docker .

3. Run the Docker container:
   docker run -p 5050:5000 ttk-docker

The application will be available at http://localhost:5000.

*Usage:* Once the container is running, you can interact with the TARSQI Toolkit via the REST API. Send a POST request to the /process endpoint, passing the text and document creation time (DCT) as parameters. The API will return the TARSQI-annotated output.

*Example:*

```bash
curl -X POST http://localhost:5000/process \
  -H "Content-Type: application/json" \
  -d '{
    "text": "Your input text here",
    "dct": "2023-09-11"
  }'


**This will return the annotated text processed by the TARSQI Toolkit.***

Contributing: We welcome contributions to this repository! If you encounter any bugs, have feature requests, or would like to contribute improvements, feel free to open an issue or submit a pull request.

License: This repository is licensed under the MIT License.
