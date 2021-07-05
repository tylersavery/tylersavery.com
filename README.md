# Wagtail Boilerplate


## Setup

## Create Virtual Environment
```
python -m venv venv
source venv/bin/activate
```

### Install Dependencies
This will install the node and python packages.
```
make install
```

### Environment
```
cp .env.template .env
```
Then update the env vars in new `.env` file


### Database Migration
```
python manage.py migrate
```

### Build Frontend
```
npm run build
```

### Run
```
make run
```
visit `http://localhost:8000/`


## Develop

### Running Backend + Frontend
Run these two commands in separate terminal windows/tabs while developing
```
npm run serve   # webpack server
make run        # django dev server
```

### Database Changes
```
python manage.py makemigrations [migration_name]
python manage.py migrate
```


## Deployment
TODO:[john]
Something something circle ci
