# Controlling ZAP with the Python script

Controlling DAST scanner via the script is quite usefull, since you can call it right after your unit tests or in any other situation where manual interaction is not prefered. 
This python script will help you achieve this, by the way, you are welcome to change the script as you like. 

You will need the ZAPv2 library as a prerequisite. It's a library to interact with the ZAP api. The documentation about it can be found here: [ZapV2](https://github.com/zaproxy/zap-api-python/tree/master/src/zapv2)

## Steps to successfully launch the scan

  - Launch ZAP scanner somewhere (it doesn't even need to be on your machine)
  - Have in mind the IP address where the ZAP is running and the port on which it listens
  - Open the `params.py` file and edit the `zap` variable. You will find the syntax inside the file
  - On ZAP again and navigate to the `Preferences`, pick the `API` node
  - Your value of interest is the `API Key`. It looks something like this: `olthv41fjb67953u863ddaj6ej`. 
  - This key has to go to the `params.py` file as well. There's a variable called `apikey`.
  - In the same `params.py` define what is your target
  - Now you can launch the script by easily typing
    ```
    python scan.py
    ```
