from logging import Logger
from tqdm import tqdm
from tqdm.contrib.logging import logging_redirect_tqdm
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import time


def crawlTagImg(tag: str, query: str, link: str, n_scroll: int, log: Logger) -> dict:
    op = webdriver.ChromeOptions()
    op.add_argument("--headless")
    op.add_argument("disable-gpu")
    op.add_argument("incognito")
    op.add_argument("--blink")

    driver = webdriver.Chrome(options=op)
    driver.get(url=link)
    driver.maximize_window()

    while True:
        try:
            load_button = driver.find_element(By.CLASS_NAME, "rx4AP").find_element(By.TAG_NAME, "button")
            load_button.click()
            time.sleep(0.3)
        except NoSuchElementException:
            break

    actions = driver.find_element(By.CSS_SELECTOR, "body")

    for i in range(n_scroll):
        actions.send_keys(Keys.PAGE_DOWN)
        time.sleep(0.4)

    imgs = []
    cnt = 0
    figures = driver.find_elements(By.TAG_NAME, "figure")

    for figure in tqdm(figures, position=0, leave=True):
        with logging_redirect_tqdm():
            try:
                omfF5 = figure.find_element(By.CLASS_NAME, "omfF5")
                MorZF = omfF5.find_element(By.CLASS_NAME, "MorZF")
                img = MorZF.find_element(By.TAG_NAME, "img")
                src = img.get_attribute("src")
                imgs.append({"Tag": tag, "query": query, "path": src})
                log.info("- %s", src)
            except Exception as e:
                log.exception(e)
                cnt += 1
    driver.close()

    return imgs, cnt
