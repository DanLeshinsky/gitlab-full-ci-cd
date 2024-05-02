# API Full CI/CD Project

This project demonstrates a comprehensive setup for API testing incorporating GitLab CI/CD pipelines, Docker, and Allure reports. It's designed to showcase best practices in creating and managing a robust testing environment using advanced technologies.

https://github.com/DanLeshinsky/gitlab-full-ci-cd/assets/87087121/7468818d-b43b-4aa2-8f46-67522f278cbe

## Technologies/Tools used in building the framework
Pycharm - IDE

Python - Programming language

Pytest - Test Management library

Allure Reports - Reporting framework

Git - Version control

Gitlab - CI/CD functionality

## Project Setup Locally
- Clone the project
- Navigate to the project directory
- Install requirements (dependencies) by running the following command:

    `pip install -r requirements.txt`

- install Docker environment

### Creating the Project in GitLab for CI/CD
- Push the project to the GitLab. 
- Create and add Access Token for handling artifacts to the project's CI/CD settings under Variables.


## API Reference
https://qa-playground.com/en/profile/backlog/auto

### Development Environments
- PROD STAGE: https://release-gs.qa-playground.com/api/v1
- QA STAGE: https://dev-gs.qa-playground.com/api/v1

### Setup - Sets up API, cleans DB and populates with sample data

```http
  POST  /setup
```

|  Parameter  | Type     | Description                |
| :---------- | :------- | :------------------------- |
| `API_TOKEN` | `string` | **Required Header**. Your API_TOKEN |


### Create a new user. Limit is 20 users

```http
  POST  /users
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `api_key` | `string` | **Required Header**. Your API_TOKEN |

```
    Body:
        {
            "email": "dan@gmail.com",
            "password": "123abc",
            "name": "Dan",
            "nickname": "Dan"
        }
```

#### Get user - Returns a user based on a single UUID.

```http
  GET /users/{uuid}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `uuid`      | `string` | **Required**. Id of user to fetch |



## Run Locally

-  To run tests locally, run the following command
  
     `$env:STAGE="prod"; pytest -sv`

-  To run tests locally with allure report, run the following command
  
    `$env:STAGE="prod"; pytest -sv --alluredir=allure_results`

    `allure serve allure_results`

- To run tests locally in docker with generating allure report

    `docker-compose up api-tests`

    `docker-compose up report`
https://github.com/DanLeshinsky/gitlab-full-ci-cd/assets/87087121/09c7f6fb-c37d-42b7-91f8-c0a46644ea95a466

## Environment Variables in Gitlab

To run this project, you will need to add the following environment variables in Gitlab under Settings -> CI/CD -> Variables

`API_KEY`

`PRIVATE_KEY`


## Authors

- [@DanLeshinsky](https://www.github.com/DanLeshinsky)
- +972-50-6676741





