### Prerequisites
[Python 3](https://www.python.org/downloads/)

[Appium](http://appium.io/docs/en/about-appium/getting-started/#installing-appium)

[Android Debug Bridge (adb)](https://developer.android.com/studio/command-line/adb)

### Installing

 1. Clone the repository.
 2. Go to the cloned directory. 
    ```
    cd <PATH-TO-YOUR-CLONED-DIRECTORY>
    ```
 3. Create and activate virtual environment (e.g. mobile_automation_course).
    ```
    pyenv virtualenv mobile_automation_course
    pyenv activate mobile_automation_course
    ```
 4. Install packages from "requirements file"
    ```
    pip install -r requirements.txt 
    ``` 

## Running the tests

 1. [Start Appium Server.](http://appium.io/docs/en/about-appium/getting-started/#starting-appium)
 2. Run an emulator with installed Wikipedia app
    
    If the app is not installed, 
    add the path to the app as the desired capability in webdriver.py
    ```
    app='<PATH-TO-YOUR-CLONED-DIRECTORY>/PythonAppiumAutomation/apks/org.wikipedia.apk'
    ```
 3. Make sure it is the only connected device.
    ```
    adb devices
    ```
 4. Run tests.
    ```
    pytest test_one.py
    ``` 