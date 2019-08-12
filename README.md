# Django Organic Pizza

The best organic pizzas in town

## NOTA BENE 
- this is a test project for evaluation purposes and not a production ready app
- To go faster I've just included the minified version of [theme is coreui](https://github.com/coreui/coreui-free-bootstrap-admin-template) and no SCSS files as specs says Styling of the page is NOT important. 
- I've only done traditional server side rendering and no API/GraphQL endpoint as per the spec the only CRUD operation happens in the management command  (so no react/redux/saga/graphene-django/react/cypress/apollo)
- I've not setup a CI pipeline as I'm using Gitlab-CI and this is only compatible with Gitlab but not compatible with Github. As a replacement I'm building the image locally through a docker-compose file

## Development environment installation

requirements : OSX with brew as package manager

˜˜˜ bash
brew install pyenv
brew install pyenv-virtualenv
pyenv install 3.7.4 # run below command instead in case of error related to OSX Mojave
SDKROOT=/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX10.14.sdk MACOSX_DEPLOYMENT_TARGET=10.14 pyenv install 3.7.4 # run in case of error at the previous line on OSX Mojave
pyenv virtualenv django_organic_pizza
pyenv activate django_organic_pizza
pip install -r requirements/development.txt
psql
CREATE DATABASE django_organic_pizza_development WITH OWNER '~' ENCODING 'utf-8'; # replace ~ by your username
exit
python manage.py migrate
python manage.py runserver
˜˜˜

## Run test suit

˜˜˜ bash
coverage run manage.py test
coverage html
˜˜˜

## Production installation

### Supported OS : 
- an OS dedicated for containers such as CoreOs with docker
- a Unix system such as Debian with Docker pre installed (not tested)
- [OSX with docker-for-mac installed](https://docs.docker.com/docker-for-mac/install/)

### Install docker-compose

[Docker for Mac come with docker-compose pre installed](https://docs.docker.com/docker-for-mac/install/)

CoreOs :

˜˜˜ bash
if [ ! -d "/opt/bin" ]; then
  echo "creating /opt/bin dir"
  sudo mkdir -p /opt/bin
fi

latest_targz=$(curl -s https://api.github.com/repos/docker/compose/releases/latest | grep browser_download_url | cut -d '"' -f 4 | grep Linux-x86_64 | sed '/.sha256/d')

sudo curl -L $latest_targz -o /opt/bin/docker-compose
sudo chmod +x /opt/bin/docker-compose
˜˜˜

Debian (not tested):
˜˜˜ bash
TODO
˜˜˜

### Build and run :

First copy docker-compose.yml.dist to docker-compose.yml and replace the values in ~

˜˜˜ bash
git clone my_url
cd django_organic_pizza
docker-compose up --build
docker exec -it django_organic_pizza bash
python manage.py migrate
exit
˜˜˜


