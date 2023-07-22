import time as t
import pandas as pd
import my_package
from selenium.webdriver.common.by import By
from selenium.webdriver import Chrome, ChromeOptions
global_path = "../scraping_data/"
headless_mode = 1


class SeleniumDriver:
    def __init__(self):
        # Webdriver object with set-ups
        options = ChromeOptions()
        options.add_experimental_option("detach", True)

        if headless_mode:
            options.add_argument('headless')
            options.add_argument('window-size=1920x1080')

        self.driver = Chrome(options=options)

        self.pages = 0
        self.current_page = 1
        self.titles = []
        self.authors = []
        self.regular_prices = []
        self.release_dates = []

        # DataFrame Initialization
        self.df = pd.DataFrame(columns=['titles', 'authors', 'regular_prices', 'release_dates'])

    def pagination_setup(self, url):
        # Establish Navigational Link
        self.driver.get(url)
        self.driver.maximize_window()

        # Locate indexed values
        page_index = self.driver.find_elements(By.XPATH, "//html/body/div[1]/div[5]/div[5]/div/div[2]/div[6]/form"
                                                         "/div/div/div[2]/div/span/ul/li")
        try:
            self.pages = int(page_index[-2].text)

        except Exception as exc:
            print("! ", exc)
            self.pages = page_index[-2].text

        finally:
            print("Transition to the next page successful.")

    def scraping(self):
        while self.current_page <= self.pages:
            print('◘ Scraping page #', self.current_page, " - Progress: ", (self.current_page/self.pages)*100, "%")
            t.sleep(3)

            # Scrape all Titles
            titles = self.driver.find_elements(By.XPATH, "//h3[contains(@class, 'bc-heading')]")

            for title in titles:
                if title.text != '':
                    temp_title = title.text.strip().split('. ')
                    self.titles.append(temp_title[1])

            # Scrape all Authors
            authors = self.driver.find_elements(By.XPATH, "//li[contains(@class, 'authorLabel')]")

            for author in authors:
                if author.text != '':
                    self.authors.append(author.text.replace('By: ', '').strip())

            # Scrape all Prices
            regular_prices = self.driver.find_elements(By.XPATH, "//p[contains(@id, 'buybox-regular-price')]")

            for regular_price in regular_prices:
                if regular_price.text != '':
                    self.regular_prices.append(regular_price.text.split(' ')[-1])

            # Scrape all Dates
            release_dates = self.driver.find_elements(By.XPATH, "//li[contains(@class, 'releaseDateLabel')]")

            for release_date in release_dates:
                if release_date.text != '':
                    self.release_dates.append(release_date.text.split(' ')[-1])

            self.current_page += 1

            try:
                # Load next elements
                next_button = self.driver.find_element(By.XPATH, "//span[contains(@class, 'nextButton')]")

            except Exception as ex:
                print("Failed to locate the next page.", ex)

            else:
                next_button.click()

        t.sleep(5)
        self.driver.quit()

    def store_values(self):
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
            self.df.to_csv(global_path + 'csv/audible_best_sellers.csv', sep=',')
            self.df.to_json(global_path + 'json/audible_best_sellers.json')
            self.df.to_excel(global_path + 'excel/audible_best_sellers.xlsx')
            self.df.to_xml(global_path + 'xml/audible_best_sellers.xml')
            print("DataFrame storage successful.\n")

        finally:
            # Confirmation / Diagnosis
            print('Size of Lists- \nTitles: ', len(self.titles), '\nAuthors', len(self.authors),
                  '\nPrices', len(self.regular_prices), '\nRelease Dates', len(self.release_dates))


if __name__ == "__main__":
    start = t.time()

    drv = SeleniumDriver()

    # Audible Site Link
    start_urls = 'https://www.audible.com/adblbestsellers?ref=a_hp_t1_navTop_pl0cg1c0r0&pf_rd_p=c592ea51-' \
                'fd36-4dc9-b9af-f665ee88670b&pf_rd_r=ZZTKEW7RNC9WX81TKH8K&pageLoadId=FwsYKeyG8zKtt9sK&creativeId' \
                '=711b5140-9c53-4812-acee-f4c553eb51fe'


    drv.pagination_setup(start_urls)
    drv.scraping()
    drv.store_values()
    end = t.time()
    print(f"Time: {end-start:.2f} sec")


