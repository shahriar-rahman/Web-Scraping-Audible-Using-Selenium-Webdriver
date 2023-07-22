import time
import asyncio
import time as t
import pandas as pd
from selenium.webdriver import Chrome, ChromeOptions
# from selenium.webdriver.common.by import By
from caqui.caqui import AsyncDriver
from caqui.by import By

MAX_CONCURRENCY = 3  # number of webdriver instances running
semaphore = asyncio.Semaphore(3)
semaphore_new_session = asyncio.Semaphore(5)


class SeleniumDriver:
    def __init__(self):
        # Webdriver object with set-ups
        options = ChromeOptions()
        options.add_experimental_option("detach", True)
        # self.driver = Chrome(options=options)
        remote = "http://127.0.0.1:9999"
        capabilities = {
            "desiredCapabilities": {
                By.NAME: "webdriver",
                "browserName": "chrome",
                "applicationCacheEnabled": True,
                "acceptInsecureCerts": True,
                "locationContextEnabled": False,
                "pageLoadStrategy": "eager",
                # uncomment to run in headless mode
                # "goog:chromeOptions": {"extensions": [], "args": ["--headless"]},
            }
        }
        self.driver = AsyncDriver(remote, capabilities)

        self.pages = 0
        self.current_page = 1
        self.titles = []
        self.authors = []
        self.regular_prices = []
        self.release_dates = []

        # DataFrame Initialization
        self.df = pd.DataFrame(columns=['titles', 'authors', 'regular_prices', 'release_dates'])

    async def pagination_setup(self, url):
        # Establish Navigational Link
        get_task = self.driver.get(url)
        maximize_task = self.driver.maximize_window()

        # run tasks concurrently
        await asyncio.gather(
            get_task,
            maximize_task,
        )
        # # Locate indexed values
        # page_index = await self.driver.find_elements(By.XPATH, "//html/body/div[1]/div[5]/div[5]/div/div[2]/div[6]/form"
        #                                                  "/div/div/div[2]/div/span/ul/li")
        # self.pages = int(page_index[-2].text)

    async def scraping(self, page):
        # while self.current_page <= self.pages:
        await self.pagination_setup(page)

        # print('◘ Scraping page #', self.current_page, " - Progress: ", (self.current_page/self.pages)*100, "%")
        print(f"◘ Scraping page '{page}'")
        # t.sleep(3)
        # await asyncio.sleep(3)

        # Scrape all Titles
        titles_task = self.driver.find_elements(By.XPATH, "//h3[contains(@class, 'bc-heading')]")
        # Scrape all Authors
        authors_task = self.driver.find_elements(By.XPATH, "//li[contains(@class, 'authorLabel')]")
        # Scrape all Prices
        regular_prices_task = self.driver.find_elements(By.XPATH, "//p[contains(@id, 'buybox-regular-price')]")
        # Scrape all Dates
        release_dates_task = self.driver.find_elements(By.XPATH, "//li[contains(@class, 'releaseDateLabel')]")

        # run all tasks concurrently
        titles, authors, regular_prices, release_dates = await asyncio.gather(
            titles_task,
            authors_task,
            regular_prices_task,
            release_dates_task
        )

        for title in titles:
            if title.text != '':
                temp_title = title.text.strip().split('. ')
                self.titles.append(temp_title[1])


        for author in authors:
            if author.text != '':
                self.authors.append(author.text.replace('By: ', '').strip())

        for regular_price in regular_prices:
            if regular_price.text != '':
                self.regular_prices.append(regular_price.text.split(' ')[-1])


        for release_date in release_dates:
            if release_date.text != '':
                self.release_dates.append(release_date.text.split(' ')[-1])

        self.current_page += 1

        # try:
        #     # Load next elements
        #     next_button = await self.driver.find_element(By.XPATH, "//span[contains(@class, 'nextButton')]")

        # except Exception as ex:
        #     print("Failed to locate the next page.", ex)

        # else:
        #     await next_button.click()

        # t.sleep(5)
        # await asyncio.sleep(5)
        self.driver.quit()

    async def store_values(self):
        try:
            # Transfer to DataFrame
            for row in range(0, len(self.titles)):
                self.df.loc[len(self.df)] = {'titles': self.titles[row], 'authors': self.authors[row],
                                             'regular_prices': self.regular_prices[row],
                                             'release_dates': self.release_dates[row]}
            print(self.df)

        except Exception as ex:
            print("Transfer into the DataFrame Failed.", ex)

        else:
            # CSV, XML, JSON & Excel files
            self.df.to_csv('audible_best_sellers.csv', sep=',')
            self.df.to_xml('audible_best_sellers.xml')
            self.df.to_json('audible_best_sellers.json')
            self.df.to_excel("audible_best_sellers.xlsx")
            print("DataFrame storage successful.\n")

        finally:
            # Confirmation / Diagnosis
            print('Size of Lists- \nTitles: ', len(self.titles), '\nAuthors', len(self.authors),
                  '\nPrices', len(self.regular_prices), '\nRelease Dates', len(self.release_dates))


async def __collect_data(page):
    async with semaphore_new_session:
        drv = SeleniumDriver()

    async with semaphore:
        await drv.scraping(page)
        await drv.store_values()

async def __schedule_tasks():
    # Audible Site Link
    start_urls = 'https://www.audible.com/adblbestsellers'
    all_pages = []
    all_pages.append(start_urls)
    all_pages.append(f"{start_urls}?page=2")
    all_pages.append(f"{start_urls}?page=3")
    all_pages.append(f"{start_urls}?page=4")
    all_pages.append(f"{start_urls}?page=5")
    tasks = [asyncio.ensure_future(__collect_data(page)) for page in all_pages]
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    start = time.time()
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(__schedule_tasks())
    finally:
        loop.run_until_complete(loop.shutdown_asyncgens())
        loop.close()
        end = time.time()
        print(f"Time: {end-start:.2f} sec")
