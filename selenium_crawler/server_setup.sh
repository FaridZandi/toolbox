###################################################################
# How selenium crawler can be set up an on ubuntu server.

# Tested on Ubuntu 20.04 Aug 28, 2022.
# Tested on Sim-04 and Sim-08 machines from Nu-Lab.

# inspired by: https://withr.github.io/set-up-selenium-headless-on-ubuntu-16.04/
###################################################################

### install pip 
# check if there is a pip: python3 -m pip freeze
# if no pip: sudo apt-get intall python3-pip

### install selenium
sudo apt install python3-selenium 
# which will also chromium-browser and chromium-driver 
# it gets stuck for a while at certain points through the progress
# this might help if that happens: sudo service snapd restart

### install Xvfb & PyVirtualDisplay
sudo apt-get install xvfb
sudo python3 -m pip install pyvirtualdisplay

### test script:
# add the test-script and run it 
python3 test.py
# which is supposed to printe Google in the end. 



