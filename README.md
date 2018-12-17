# CL_scraper
This is a dead-simple scraper for Craigslist using Python, ChromeDriver, and Selenium. The purpose is largely to demonstrate the relationship between python, selenium, and chromedriver. 

The purpose of this tool is to paginate through Craigslist and search for items one might want. Here we look for
the string 'ikea'. We are guaranteed to find something as people just throw that stuff away or toss it on CL. 

To run:

Set up a virtual environment on your flavor of Ubuntu. 

If you are using something like pycharm, install the requirements.txt, otherwise run 
`python3.6 -m pip install -r requirements.txt` after you install the correct version of pip

for me, I use `sudo apt install python3-pip`

If you use this, make sure to install the correct version of python. 

Navigate to http://chromedriver.chromium.org/downloads and download the latest version of chromedriver for Ubuntu

Often, you might get an error where chrome driver will fail to connect to a website with status connection of 200.
It is important to remember to update the chromedriver binary every once in a while. You don't know how many
times I have painstakingly gone through the code base only to realize that the error is resolved by updating chromedriver.

You have been warned. 

Activate your virtual environment and go `python3.6 CL_scraper.py <input url. ex. https://portland.craigslist.org>`... 

Any questions hit me up on here. 
