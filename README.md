# FastAPI Keycloak Integration

![Integrating FastAPI with Keycloak for Authentication](./assets/Integrating%20FastAPI%20with%20Keycloak%20for%20Authentication.jpg)

This project demonstrates how to integrate [Keycloak](https://www.keycloak.org/) with a [FastAPI](https://fastapi.tiangolo.com/) application using Docker and Docker Compose for authentication.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Authentication Flow](#authentication-flow)
- [Testing the Authentication](#testing-the-authentication)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgments](#acknowledgments)

## Introduction

This project provides a template for securing a FastAPI application using Keycloak as the identity provider. It uses Docker and Docker Compose for containerization and easy deployment. Dependency management is handled using Poetry.

## Features

- **FastAPI Application**: A modern, fast web framework for building APIs with Python 3.12+.
- **Keycloak Integration**: Secure your API endpoints with Keycloak's robust authentication and authorization features.
- **Custom Login Endpoint**: Authenticate users via a `/login` endpoint that returns an access token.
- **Dockerized Setup**: Use Docker and Docker Compose for seamless development and deployment.
- **Poetry for Dependency Management**: Simplify your Python dependencies and virtual environments.

## Prerequisites

- [Python 3.11](https://www.python.org/downloads/)
- [Docker](https://www.docker.com/get-started)
- [Docker Compose](https://docs.docker.com/compose/install/)
- [Git](https://git-scm.com/)
- **Up and Running Keycloak Server**

  Ensure that you have a Keycloak server up and running, configured with the appropriate realm, client, and user. This can be set up separately or included in your Docker Compose configuration.

## Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/anqorithm/fastapi-keycloak.git
   cd fastapi-keycloak
   ```

2. **Copy Environment Variables File**

   Navigate to the `src` directory and copy the `.env.example` file to `.env`:

   ```bash
   cd src
   mv .env.example .env
   ```

3. **Configure Environment Variables**

   Open the `.env` file and update the following variables with your Keycloak configuration:

   - `KEYCLOAK_SERVER_URL`: The URL where your Keycloak server is running (e.g., `http://keycloak:8080/`).
   - `KEYCLOAK_REALM`: Your Keycloak realm name (e.g., `fastapi-realm`).
   - `KEYCLOAK_CLIENT_ID`: The client ID you set up in Keycloak (e.g., `fastapi-client`).
   - `KEYCLOAK_CLIENT_SECRET`: The client secret obtained from Keycloak.

4. **Set Up Keycloak**

   Ensure that Keycloak is configured with the appropriate realm, client, and user. Refer to the [Configuration](#configuration) section for detailed steps.

## Configuration

### Setting Up Keycloak Server

1. **Start Keycloak**

   - Ensure your Keycloak server is up and running.
   - You can run Keycloak separately or include it in your `docker-compose.yml`.

2. **Access the Keycloak Admin Console**

   - Open your browser and navigate to `http://localhost:8080/` (or the appropriate URL).
   - Log in with your admin credentials.

3. **Create a New Realm**

   - Click on **Add Realm** in the admin console.
   - Provide a name for your realm (e.g., `fastapi-realm`).
   - Click **Create**.

4. **Create a New Client**

   - Navigate to the **Clients** section within your realm.
   - Click **Create**.
   - Enter your client ID (e.g., `fastapi-client`).
   - Set the Client Protocol to `openid-connect`.
   - Click **Save**.
   - In the client settings:
     - Set **Access Type** to `confidential`.
     - Enable **Standard Flow Enabled** and **Direct Access Grants Enabled**.
     - In **Valid Redirect URIs**, add `http://localhost:8000/*`.
     - Click **Save**.

5. **Obtain Client Secret**

   - Go to the **Credentials** tab of your client.
   - Copy the **Secret** value.
   - Update your `.env` file with this secret.

6. **Create a Test User**

   - Navigate to the **Users** section.
   - Click **Add User**.
   - Fill out the required fields (e.g., username: `testuser`).
   - Click **Save**.
   - Go to the **Credentials** tab.
   - Set a password and disable the **Temporary** option.
   - Click **Set Password**.

## Usage

### Running the Application

- Start the application using Docker Compose:

  ```bash
  docker-compose up --build
  ```

- This command builds the Docker image and starts the containers specified in the `docker-compose.yml` file.

### Accessing the Services

- **FastAPI Application**: `http://localhost:8000/`
- **Keycloak Admin Console**: `http://localhost:8080/`

## Authentication Flow

### Login Endpoint

The application includes a `/login` endpoint that allows users to authenticate by providing their username and password. Upon successful authentication, an access token is returned, which can be used to access protected routes.

- **Endpoint**: `/login`
- **Method**: `POST`
- **Parameters**:
  - `username`: The user's username.
  - `password`: The user's password.
- **Response**:
  - Returns a JSON object containing the access token.

**Note**: The `/login` endpoint accepts form data (`application/x-www-form-urlencoded`).

### Protected Endpoint

- **Endpoint**: `/protected`
- **Method**: `GET`
- **Headers**:
  - `Authorization`: `Bearer <access_token>`
- **Response**:
  - Returns a greeting message containing the username.

## Testing the Authentication

1. **Access Protected Endpoint Without Token**

   - Navigate to `http://localhost:8000/protected`.
   - You should receive a `401 Unauthorized` response.

2. **Obtain an Access Token via Login Endpoint**

   - Use a tool like `curl` or Postman to make a POST request to the `/login` endpoint.

     - **Example using `curl`**:

       ```bash
       curl -X POST http://localhost:8000/login \
         -H "Content-Type: application/x-www-form-urlencoded" \
         -d "username=testuser&password=yourpassword"
       ```

       Replace `testuser` and `yourpassword` with the credentials of the user you created in Keycloak.

   - **Response**:

     The response will be a JSON object containing the `access_token`. For example:

     ```json
     {
       "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
     }
     ```

3. **Access Protected Endpoint With Token**

   - Use the obtained `access_token` to access the protected endpoint.

     - **Example using `curl`**:

       ```bash
       curl -X GET http://localhost:8000/protected \
         -H "Authorization: Bearer your_access_token"
       ```

       Replace `your_access_token` with the token received from the `/login` endpoint.

   - **Expected Response**:

     ```json
     {
       "message": "Hello, testuser"
     }
     ```

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue.

## License

This project is licensed under the MIT License.