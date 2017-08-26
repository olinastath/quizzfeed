# QuizzFeed
#### a random BuzzFeed quiz generator

This is the first web application I have built entirely on my own. It scrapes BuzzFeed's various quiz pages, stores the quizzes in a database and then generates a random quiz. I built the scraper using Scrapy and the rest of the application using Django. This was my first time writing any sort of scraping script and also my first time building a Django project (I had used Queries and Models in the past when working on other people's projects).

### Prerequisites

##### In root directory, run 'pip install -r requirements.txt'

* Scrappy 1.4.0 ('pip install scrapy')
* DjangoItem 1.1.1 ('pip install scrapy-djangoitem')
* Django 1.8.7

### Running the project

I'm currently working on deploying it on heroku, but until then, here's how to run the program locally:
1. run 'python manage.py makemigrations' in the root directory
2. run 'python manage.py migrate' in the root directory
3. cd into the quizz_scraper directory and run 'scrapy crawl quizz_spider'
4. back in the root directory, run python manage.py runserver (points to localhost:8000)

The project is up and running at http://localhost:8000!

### Project Structure

* app/ - contains django web app
	* static/ - contains css stylesheets and images
	* templates/ contains html files to be served by django
* quizz_scraper/quizz_scraper - contains scraper 
	* spiders - contains scraping script
* requirements.txt - contains reqs to run project