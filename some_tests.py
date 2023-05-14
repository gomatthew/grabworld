import time
import undetected_chromedriver as uc

options = uc.ChromeOptions()
# options.add_argument("start-maximized")
# options.add_argument("--headless")  # 配置chrome不显示
driver = uc.Chrome(options=options)
driver.get('https://wallstreetcn.com/news/global')
print(driver.title)
time.sleep(5)
roll = 0
while 1:

    driver.execute_script(f'window.scrollTo(0,{roll + 1000})')
    time.sleep(5)
    roll += 1000
