# Controlling ZAP with the Python script

Controlling DAST scanner via the script is quite usefull, since you can call it right after your unit tests or in any other situation where manual interaction is not prefered. 
This python script will help you achieve this, by the way, you are welcome to change the script as you like. 


## Steps to successfully launch the scan

  - Download the ZAP scanner and place it somewhere on the disk. [Download link](https://github.com/zaproxy/zaproxy/releases/download/2.5.0/ZAP_2.5.0_Cross_Platform.zip)
  - Open the `scan.py` file and edit the `startZapPath` variable. You will find the syntax inside the file
  - Navigate to the root folder and launch the script
    ```sh
    $ python scan.py http://127.0.0.1:8080
    ```
