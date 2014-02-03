This is a fork from [https://github.com/arachnys/cabot](https://github.com/arachnys/cabot) 


This is meant to be deployed on Heroku. If most of your infrastructure are not hosted on AWS, it is actually a good option to put Cabot on Heroku! Another reason to use Heroku is because you can easily hook up new relic to monitor your cabot app.

<pre>
heroku create
heroku addons:add mandrill
heroku addons:add newrelic
heroku addons:add rabbitmq-bigwig
heroku config:add AWS_ACCESS_KEY_ID="YOUR_OWN_DETAILS_HERE"
heroku config:add AWS_SECRET_ACCESS_KEY="YOUR_OWN_DETAILS_HERE"
heroku config:add AWS_STORAGE_BUCKET_NAME="YOUR_OWN_DETAILS_HERE"
heroku config:add ADMIN_EMAIL="YOUR_OWN_DETAILS_HERE"
heroku config:add DJANGO_SECRET_KEY="YOUR_OWN_DETAILS_HERE"
heroku config:add CABOT_FROM_EMAIL="YOUR_OWN_DETAILS_HERE"

heroku config:add BUILDPACK_URL=https://github.com/ddollar/heroku-buildpack-multi.git

git push heroku master
heroku ps:scale web=1 scheduler=1 worker=1
heroku run python manage.py syncdb
heroku run python manage.py migrate
heroku run python manage.py collectstatic --noinput
heroku run python manage.py compress
</pre>

