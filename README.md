### Setting Up the Project
1. After cloning the project open it up in the Compiler.
2. Press the combination of `Ctrl+j` or open the terminal from the upper "main menu" -> "Terminal" -> "new Terminal".
3. First, make sure you have virtualenv installed. If not, install it using command:

   `pip install virtualenv`
4. Create a new virtual environment with the name "virtual-environment" using this command:
   
   `virtualenv virtual-environment`
5. This will create a new directory named 'virtual-environment' in your current directory, which will contain the virtual environment.
6. Activate the virtual environment by the following command:
7. 
   `virtual-environment\Scripts\activate`
7. After activating the virtual environment, you should see the name of the environment in your command prompt or terminal, 
   indicating that you are now working within the virtual environment.
8. Now Install the module using the command in the terminal:
   
   `pip install qrcode`
9. After all the above steps run the file by running command:
   
   `python main.py`
10. Then enter your URL to which you wanted to generate the QR Code.
11. The ".png" file will be downloaded in the local directory where code is saved.
