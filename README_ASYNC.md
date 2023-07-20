# Run the asynchronous crawler
## Simple start
Install the lastest version of **Caqui**

```
pip install caqui==2.0.0rc1
```
Start the WebDriver as a server
```
$ ./chromedriver --port=9999

Starting ChromeDriver 94.0.4606.61 (418b78f5838ed0b1c69bb4e51ea0252171854915-refs/branch-heads/4606@{#1204}) on port 9999
Only local connections are allowed.
Please see https://chromedriver.chromium.org/security-considerations for suggestions on keeping ChromeDriver safe.
ChromeDriver was started successfully.
```
Run the crawler
```
$ cd src/
$ python selenium_audible_async.py
```