import scrapy
from ..items import QuizzItem
import django
django.setup()


class QuotesSpider(scrapy.Spider):
    name = "quizz_spider"    # identify spider

    # set up base urls for different categories of quizzes
    main_base_url = 'https://www.buzzfeed.com/us/feedpage/feed/quizzes?page=%s&page_name=quizzes'
    personality_base_url = 'https://www.buzzfeed.com/us/feedpage/feed/quizzes-personality?page=%s&page_name=quizzes'
    disney_base_url = 'https://www.buzzfeed.com/us/feedpage/feed/quizzes-disney?page=%s&page_name=quizzes'
    guess_base_url = 'https://www.buzzfeed.com/us/feedpage/feed/quizzes-can-we-guess?page=%s&page_name=quizzes'
    food_base_url = 'https://www.buzzfeed.com/us/feedpage/feed/quizzes-food?page=%s&page_name=quizzes'
    wyr_base_url = 'https://www.buzzfeed.com/us/feedpage/feed/quizzes-would-you-rather?page=%s&page_name=quizzes'
    love_base_url = 'https://www.buzzfeed.com/us/feedpage/feed/quizzes-love?page=%s&page_name=quizzes'
    trivia_base_url = 'https://www.buzzfeed.com/us/feedpage/feed/quizzes-trivia?page=%s&page_name=quizzes'
    page = 1
    start_urls = [main_base_url % page,
                  personality_base_url % page,
                  disney_base_url % page,
                  guess_base_url % page,
                  food_base_url % page,
                  wyr_base_url % page,
                  love_base_url % page,
                  trivia_base_url % page]

    def parse(self, response):
        for quiz in response.css('div.card--article'):
            # find 'category' attribute in html
            data = quiz.css('div.js-card__content a.link-gray::attr(data-bfa)').extract_first().strip()
            beg = data.find("post_category:") + len("post_category:")
            end = data.find(",data_source:")

            # create QuizzItem and populate fields
            quizz = QuizzItem()
            quizz['title'] = quiz.css('div.js-card__content a.link-gray h2::text').extract_first().strip()
            quizz['subtitle'] = quiz.css('div.js-card__content a.link-gray p::text').extract_first().strip()
            quizz['category'] = data[beg:end]
            quizz['link'] = quiz.css('div.js-card__content a.link-gray::attr(href)').extract_first().strip()
            yield quizz


        # increment page number to scrape next page
        self.page += 1
        next_page = self.page

        # continue callback while there are more pages
        if next_page < 8:
            yield scrapy.Request(self.main_base_url % next_page)
            yield scrapy.Request(self.personality_base_url % next_page)
            yield scrapy.Request(self.disney_base_url % next_page)
            yield scrapy.Request(self.guess_base_url % next_page)
            yield scrapy.Request(self.food_base_url % next_page)
            yield scrapy.Request(self.wyr_base_url % next_page)
            yield scrapy.Request(self.love_base_url % next_page)
            yield scrapy.Request(self.trivia_base_url % next_page)
