Go to the chromedriver releases page. Find the suitable version of the driver for your platform and download it. For example:
wget https://chromedriver.storage.googleapis.com/96.0.4664.45/chromedriver_linux64.zip

Extract the file with:
unzip chromedriver_linux64.zip

Make it executable:
chmod +x geckodriver

Add the driver to your PATH so other tools can find it:
export PATH=$PATH:/path-to-extracted-file/.

OR

Move file to PATH
sudo mv geckodriver /usr/local/bin/