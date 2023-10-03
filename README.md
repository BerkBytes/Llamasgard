# Llamasgard API Package Documentation

---

## Table of Contents

1. [Overview](#overview)
2. [Installation](#installation)
3. [API Tunneling and Connection](#api-tunneling)
4. [How to Use](#how-to-use)
5. [API Parameters](#api-parameters)
6. [Error Handling](#error-handling)
7. [License and Acceptable Use](#license-and-acceptable-use)

---

## <a name="overview"></a>1. Overview

**Code Llama** is a state-of-the-art Large Language Model (LLM) proficient in generating code, and natural language about code, from both code and natural language prompts. This documentation details the client-side package that interfaces with the Code Llama's 34B Instruct model via an API endpoint.

**Key Features**:
- Generate code using text prompts.
- Supports various popular programming languages.
- Built on top of the Llama 2 framework.

---

## <a name="installation"></a>2. Installation

To install the Llamasgard API client package, you cab manually download it from the GitHub repository and then install it using `pip`. Ensure you also have the `requests` library installed:

1. Navigate to [https://github.com/BerkBytes/Llamasgard/blob/main/dist/](https://github.com/BerkBytes/Llamasgard/blob/main/dist/).
2. Find the `llamasgard.0.0.4.tar.gz` file in the `dist` directory.
3. Click on it, then click "Download".

Once downloaded, you can install it using `pip`:

```bash
# Navigate to the download directory
cd path/to/download/directory

# Install the package
pip install llamasgard.0.0.4.tar.gz

# Install the requests library
pip install requests
```

---

## <a name="api-tunneling"></a>3. API Tunneling and Connection

### SSH Tunneling

SSH (Secure Shell) tunneling is a method of transporting arbitrary networking data over an encrypted SSH connection. It can be used to add encryption to legacy applications, to provide secure remote access to an intranet resource or to forward otherwise insecure TCP traffic through encrypted channels. 

In the context of the Llamasgard API, an SSH tunnel is utilized to securely forward requests to the API server. The following command is used for setting up port forwarding:

```bash
ssh -N -f -L localhost:8000:localhost:8000 username@10.19.2.120
```

Breaking down the command:

- `-N`: Do not execute a remote command. This is useful for just forwarding ports.
- `-f`: Requests SSH to go to the background just before command execution.
- `-L [bind_address:]port:host:hostport`: Specifies that the given port on the local (client) host is to be forwarded to the given host and port on the remote side.
  - `localhost:8000`: Local machine address and port number.
  - `localhost:8000`: Remote machine address and port number to bind the forwarding.
- `username@10.19.2.120`: Username and IP address of the remote server.

### Connecting via Python

To establish an SSH tunnel and make requests to the API via Python, you can utilize the `paramiko` and `sshtunnel` libraries. Here's an example demonstrating how to establish an SSH tunnel and connect to the API through Python:

```python
import requests
from sshtunnel import SSHTunnelForwarder
import paramiko

# SSH Tunnel Configuration
ssh_config = {
    'ssh_address_or_host': ('10.19.2.120', 22),  # Remote SSH server IP and port
    'ssh_username': 'username',  # SSH Username
    'ssh_password': 'password',  # SSH Password (use ssh_pkey parameter for key file)
    'remote_bind_address': ('localhost', 8000),  # API server IP and port
    'local_bind_address': ('localhost', 8000),  # Local machine IP and port
}

# Ensure you have the API endpoint
api_url = "http://localhost:8000/predict

# Example API Parameters
params = {
    "user": "Write a Python function to calculate factorial.",
    "max_new_tokens": 1024,
    "temperature": 0.9,
}

# Establishing SSH Tunnel and Making the API Request
with SSHTunnelForwarder(**ssh_config) as tunnel:
    print(f"Tunnel opened at localhost:{tunnel.local_bind_port}")
    
    # Making the API Request
    response = requests.post(api_url, data=params)
    
    # Handling the Response
    if response.status_code == 200:
        print("Success:", response.json())
    else:
        print("Failed:", response.status_code, response.text)
```

In this example, `paramiko` is used as the SSH client by `sshtunnel`. Ensure to replace `'password'` and other placeholder values with actual credentials. Also, ensure that the SSH server is configured to allow port forwarding.

To run the above Python code, you need to install the `sshtunnel` and `requests` libraries. If not installed, you can add them using pip:

```bash
pip install sshtunnel requests paramiko
```

Ensure the SSH credentials are secured and stored safely when implementing in production environments.

---

## <a name="how-to-use"></a>4. How to Use

To utilize the package, simply import the `CodeLlama` function and call it with the desired parameters.

Example:

```python
from Llamasgard import CodeLlama

user_prompt = "Write a Python function to calculate factorial."
response = CodeLlama(user=user_prompt)
print(response)
```

---

## <a name="api-parameters"></a>5. API Parameters

- **user**: The user's input prompt.
  
- **system** (default="Your name is Code Llama, a state-of-the-art large language model (LLM) specialized in generating and discussing code. As an advanced descendant of Llama 2, you've been trained extensively on code-specific datasets, granting you the capability to generate code, understand natural language related to code, complete code fragments, and assist in debugging. You are proficient in many popular programming languages such as Python, C++, Java, PHP, Typescript, C#, Bash, and more. Keep responses concise and be friendly towards users."): A description of Code Llama to provide context.

- **prefix** (optional): A prefix to the generated response.

- **max_new_tokens** (default=1024): Max tokens for the generated output.

- **temperature** (default=0.9): Sampling temperature.

- **top_p** (default=0.95): Nucleus sampling parameter.

- **repetition_penalty** (default=1.2): Penalty for repeated tokens.

- **top_k** (default=50): K-top sampling.

- **num_return_sequences** (default=1): Number of sequences to return.

---

## <a name="error-handling"></a>6. Error Handling

The `CodeLlama` function handles HTTP errors gracefully. If the API returns any status code other than 200, the function will return the error code and the associated error text.

---

## <a name="license-and-acceptable-use"></a>7. License and Acceptable Use

While **Code Llama** is free for research and commercial use, users must adhere to the associated license and acceptable use policy. Before deploying or integrating this package, please ensure you're compliant with all terms and conditions.

---

