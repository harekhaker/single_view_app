# Single view works

The app powered to collect music reports provided from anyone and share to people meta information about compositions by ISWC

## Getting Started

### Prerequisites

It is necessary to have installed docker on your machine. Example for Ubuntu

```
sudo apt install docker
```

### Installing


```
$ git clone https://github.com/harekhaker/single_view_app.git
```

Then:

```
$ cd single_view_app/
```

Finally:


```
$ docker-compose up
```

## Using

* GET -- /api/music/                    -- get all compositions in db
* GET -- /api/music/?iswc=YOUR_ISWC     -- get report by direct iswc
* GET -- /api/generate_report/          -- get you csv report with all compositions
* GET -- /api/generate_report/?iswc=YOUR_ISWC -- get you csv report with a current composition
* POST-- /upload_file/                   -- upload file to server and will worked by watchdog

Simple uploading script in folder /example/

Running:

```
$ cd /example/
$ python upload.py
```


## Running the tests

At the moment autotests are underworking.
## Deployment

In production is recommended run web app by wsqi under nginx and control by supervisord.


## Authors

* **Vladimir Kyrylchuk** - *FS-Group* - https://group-fs.com/

