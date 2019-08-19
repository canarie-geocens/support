This is a a simple REST service for GeoCENS [CANARIE Registry and Monitoring System](https://www.canarie.ca/wpdm-package/research-platform-support-for-the-canarie-registry-and-monitoring-system/?wpdmdl=10245).

`<base_url>`: `geocens-support.sensorup.com.`

- Smart Air (GeoCENS): `<base_url>/`

### Development

This RESTful API is built based on Flask.
Install python virtual environment and necessary dependencies

```bash
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
python3 appserver.py
```

Then go to `http://localhost:5000/info/` and it should return a json response.

### Deployment

We will be setting up a Python application using the Flask micro-framework on Ubuntu 18.04. We will set up the uWSGI application server to launch the application and Nginx to act as a back-end reverse proxy.

1. Upload the code to the server
2. Install necessary packages

```bash
apt-get update
apt-get install python3-pip python3-dev python3-venv nginx
```

3. cd into application folder and create a virtual environment in the folder for an isolated Python3 interpreter to run the flask application

```bash
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
python3 appserver.py
```

4. Setting up uWSGI container server and enable application automaic starting each time the system boots up

```bash
sudo mv geocens_api.service /etc/systemd/system/
sudo systemctl enable geocens_api
```

You can use `sudo systemctl start geocens_api` to start the platform, or use `sudo systemctl status geocens_api` to check its status

5. Setting up Nginx
   Nginx acts as a reverse proxy the request to the uWsgi server.
   Change the `server_name` to the right IP address

```bash
sudo mv geocens /etc/nginx/sites-available/
sudo ln -s /etc/nginx/sites-available/geocens /etc/nginx/sites-enabled
sudo ufw allow 'Nginx Full'
sudo systemctl restart nginx
```

6. Bind a domain to the server IP address

# Smart Air User Portal:

1.Platform Info

URI - `<base>/info/`

**HTTP GET**

`geocens-support.sensorup.com/info/`

**Example**

```JSON
{
    "name" : "<name of platform>",
    "synopsis": "<one or two sentences describing what the platform is for>",
    "version" : "<platform version identifier>",
    "institution": "<the name of the institution that contributed this platform>", "releaseTime": "<time at which this version of the platform was released>", "researchSubject":"<the research area to which this platform applies>",
    "supportEmail": "<email address for support in case of platform outage>",
    "tags":"[<terms describing this platform – to be used in searches>]"
}
```

```JSON
{
    "name": "Smart Air (GeoCENS)",
    "synopsis": "Smart Air extends the existing GeoCENS platform to collect and analyze hyper-local and real-time air quality data across Canada. Smart Air will provide street-level air quality data with an unprecedented spatio-temporal resolution, leading to transformative new innovations with direct impacts to the health of Canadians.",
    "version": "v1.0",
    "institution": "University of Calgary",
    "releaseTime": "2019-08-08T18:00:00Z",
    "researchSubject": "Geographic Information Systems", "supportEmail": "smart.cities@sensorup.com",
    "tags": ["GeoCENS", "Air Quality", "Smart Cities"]
}
```

2.Platform Statistics

URI - <base>/stats

**HTTP GET**

`geocens-support.sensorup.com/stats/`

**Example**

```JSON
{
    "<usage type>" : "<platform usage count since last reset>",
    "lastReset": "<the time and date at which the <usage type> field was last reset to zero>",
}
```

```JSON
{
    "sensor counts": 265,
    "lastReset": "2019-08-12T21:43:40Z"
}
```

3.Platform Documentation

URI - <base>/doc

**HTTP GET**

`geocens-support.sensorup.com/doc/`

HTTP redirect to <https://smart-air-geocens.github.io>

The HTTP redirect may be returned in response to this request. This URI must also support HTTP HEAD requests. The content type for the response should specify “text/html”.

4.Platform Release Notes

URI - <base>/releasenotes

**HTTP GET**

`geocens-support.sensorup.com/releasenotes/`

HTTP redirect to <https://smart-air-geocens.github.io#releasenotes>
content type: "text/html"

5.Platform Support

URI - <base>/support

**HTTP GET**

`geocens-support.sensorup.com/support/`

Support is available from the SensorUp. Please feel free to contact us on info@sensorup.com.

6.Platform Source Code

URI - <base>/source

**HTTP GET**

`geocens-support.sensorup.com/source/`

HTTP redirect to <https://github.com/smart-air-geocens/>

7.Platform Try Me

URI - <base>/tryme

**HTTP GET**

`geocens.sensorup.com`

HTTP redirect to <http://geocens.sensorup.com/>

8.Platform Licence

URI - <base>/licence

**HTTP GET**

`geocens-support.sensorup.com/licence/`

HTTP redirect to <https://smart-air-geocens.github.io#licence>

content type: "text/html"

9.Platform Provenance

URI - <base>/provenance

**HTTP GET**

`geocens-support.sensorup.com/provenance/`

HTTP redirect to <https://smart-air-geocens.github.io#provenance>

content type: "text/html"

10.Fact Sheet

URI - <base>/factsheet

**HTTP GET**

`geocens-support.sensorup.com/factsheet/`

HTTP redirect to <https://smartcities.sensorup.com/faq/>