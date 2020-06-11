# TradeMeTest
This Project includes tests againt TradeMe(Sandbox-https://www.tmsandbox.co.nz/) Used Cars Page to get available used car brands,count  
and also checks if certain brands of cars are available.  
These tests are run on windows 10 OS and would expect similar steps in other OS as well.  
 
**SETUP**  
The following are required to run the tests:  
1)Python 3.5 or higher.Add the python folder and Scripts folder path to Path variable (This test was executed in 3.8 version)  
2)Selenium 3 or higher  
 Install selenium by running command 'pip install selenium' in command prompt (if its not already installed in the system)  
 
 **RUN**  
From IDE:  
Download or checkout the branch.  
Load the project into and IDE(IntelliJ etc.)  
Run the tests  
(OR)  
From CommandLine  
 1)Open CMD  
 2)Go to the Project directory (i.e TradeMeTest)  
 3)Run below command  
  python -m unittest discover  
   
 Viola! the test excutes and gives the results  
   
 **TroubleShooting**:  
1)Driver : The gecko driver is already in .\TradeMeTest\lib\drivers folder which it references in test.  
If the test fails because of driver instanciation,please replace existing driver with a compatable one to your browser version.You can find Firefox drivers at https://github.com/mozilla/geckodriver/releases.  
  
Tip:  
You can comment out the Firefox webdriver instantiation line and uncomment the headless browser lines if you do not want the hassle of    downloading drivers or dont want to watch the browser as test executes.  
