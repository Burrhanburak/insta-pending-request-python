# Instagram Automation Project
## Project Overview
This project automates various interactions on Instagram using Python and Selenium WebDriver. It includes functionalities such as removing pending follow requests and interacting with posts.

## Setup Instructions

### 1. Creating a Virtual Environment

First, set up a Python virtual environment to manage dependencies:

Download from Instagram your data html and put in root folder.

> pending_follow_request.html

```bash
python -m venv venv
  ```

2. Activate the virtual environment:
    - On MacOS or Linux:
        ```bash
        source venv/bin/activate
        ```
    - On Windows:
        ```bash
        .\venv\Scripts\activate
        ```
3. Open Terminal:
   - install missing packages command:
        ```bash
        pip install 'package_name'
      ```
     
### 2. Managing Environment Variables

You can manage environment variables in your project using the `python-dotenv` package. Create a `.env` file and add your Instagram username and password.

1. Create a `.env` file and add the following lines:
    ```
    INSTAGRAM_USERNAME=your_username
    INSTAGRAM_PASSWORD=your_password
    ```

2. Load environment variables in your Python code:
    ```python
    import os
    from dotenv import load_dotenv

    load_dotenv()

    username = os.getenv('INSTAGRAM_USERNAME')
    password = os.getenv('INSTAGRAM_PASSWORD')
    ```
### 3.Installing Dependencies


Install required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

### 4. Downloading and Configuring Chrome WebDriver

If you are using Selenium with Chrome, you may need to download and update the Chrome WebDriver. You can manage the WebDriver with the following steps:

1. Check your Chrome browser version and download the corresponding WebDriver version from the [ChromeDriver website](https://sites.google.com/a/chromium.org/chromedriver/downloads).

2. After downloading the WebDriver, place it in an appropriate location within your project folder and specify its path or add it to the PATH environment variable.

---