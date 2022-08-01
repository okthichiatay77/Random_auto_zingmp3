import random
import time


from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    def get_home(self):
        self.driver.get('https://zingmp3.vn/')
        self.driver.find_element(By.XPATH, "//div[@id='adtimapopup-closebutton']").click()
        time.sleep(3)
        self.driver.find_element(By.CSS_SELECTOR, '#react-cool-portal > div > div > div > div > button').click()

    def my_acction(self, xpath):
        self.driver.find_element(By.XPATH, xpath).click()

    def find_any_song(self, xpath, name_song):
        self.driver.find_element(By.XPATH, xpath).click()
        self.driver.find_element(By.XPATH, xpath).send_keys(name_song)
        time.sleep(3)
        self.driver.find_element(By.XPATH, xpath).send_keys(Keys.ENTER)
        time.sleep(3)
        self.driver.find_element(By.XPATH, '//*[@id="body-scroll"]/div[1]/div/div[2]/div/div[1]/div/div[1]/div[1]/div[2]').click()

config = {
    # 'ca_nhan': '//*[@id="root"]/div[1]/aside/div/nav[2]/ul/li[1]',
    'kham_pha': "//a[@title='Khám Phá']",
    'zingchart': "//li[@class='zm-navbar-item']//a[@title='#zingchart']",
    'radio': "//a[@title='Radio']",
    'theo_doi': "//a[@title='Theo Dõi']",

    'nhac_moi': "//a[@title='Nhạc Mới']",
    'the_loai': "//a[contains(@title,'Thể Loại')]",
    'top_100': "//a[contains(@title,'Top 100')]",
    'mv': "//a[contains(@title,'MV')]",
    'find': "//input[@placeholder='Tìm kiếm bài hát, nghệ sĩ, lời bài hát...']",
    'setting': "//body/div[@id='root']/div[@class='zm-section zm-layout has-player']/header[@class='zm-header']/div[@class='level']/div[@class='level-right']/div[1]",


    'tab_bai_hat': "//button[normalize-space()='Bài hát']",
    'tab_album': "//button[normalize-space()='Album']",
    'play_bai_hat': "//body/div/div/div/div/main/div/div/div/div/div/div/div/div/div/div[1]/div[1]/button[1]",
    'play_bai_hat2': '//*[@id="body-scroll"]/div[1]/div[4]/div[2]/div[2]/div/div[1]/div/div[1]/div[1]/div[2]/div/button[1]',
    'play_bai_hat3': '//*[@id="body-scroll"]/div[1]/div[4]/div[2]/div[3]/div/div[1]/div/div[1]/div[1]/div[2]/div/button[1]',
    'play_album': "(//div[@class='thumb-action'])[1]",
    'play_album2': "(//div[contains(@class,'thumb-action')])[4]",
    'prev_gallery': "//div[contains(@class,'zm-gallery-next')]//button[contains(@class,'zm-btn zm-carousel-control-next button')]",
    'next_gallery': "//button[contains(@class,'zm-btn zm-carousel-control-prev button')]",


    # zingchart
    'play_random_song': "//div[contains(@class,'chart-title')]//button[contains(@class,'zm-btn button')]",
    'play_top_song': "//body/div[@id='root']/div[contains(@class,'zm-section zm-layout has-player')]/div[contains(@class,'zm-box zm-mainpage')]/div/main[@id='body-scroll']/div[contains(@class,'container')]/div[contains(@class,'container rt-chart-section')]/div[contains(@class,'list mar-b-20')]/div[contains(@class,'chart-song-item on-top first')]/div[contains(@class,'list-item bor-b-1 media-item hide-right')]/div[contains(@class,'media')]/div[contains(@class,'media-left')]/div[contains(@class,'song-thumb')]/div[contains(@class,'zm-actions-container')]/div[contains(@class,'zm-box zm-actions')]/button[1]",
    # radio
    'play_radio': f'//*[@id="body-scroll"]/div[1]/div[1]/div[2]/div/div/div/div/div[{random.randint(1, 7)}]',
    'back_radio': "//div[@class='zm-live-middle-content']//div[1]//button[1]",
    # theo doi
    'tab_viet_nam': "//a[contains(text(),'Việt Nam')]",
    'tab_us_uk': "//a[normalize-space()='US-UK']",
    'tab_k_pop': "//a[normalize-space()='K-POP']",
    'tab_hoa_ngu': "//a[contains(text(),'Hoa Ngữ')]",
    'tab_noi_bat': "//a[contains(text(),'Nổi bật')]",
    'click_post': "//body/div[@id='root']/div[@class='zm-section zm-layout']/div[@class='zm-box zm-mainpage']/div/main[@id='body-scroll']/div[@class='container']/div/div[@role='grid']/div[1]/div[1]",
    'out_post': "//button[@class='zm-btn close-feed-modal button']",
    # nhac moi
    'play_music_top': "//div[@class='title']//button[@class='zm-btn button']",
    'play_random': "//body/div[@id='root']/div[contains(@class,'zm-section zm-layout')]/div[contains(@class,'zm-box zm-mainpage')]/div/main[@id='body-scroll']/div[contains(@class,'container top-new-relesase-container')]/div[contains(@class,'container new-release-chart-container')]/div[contains(@class,'list mar-b-20')]/div[contains(@class,'chart-song-item on-top first')]/div[contains(@class,'list-item bor-b-1 media-item hide-right')]/div[contains(@class,'media')]/div[contains(@class,'media-left')]/div[contains(@class,'song-thumb')]/div[contains(@class,'zm-actions-container')]/div[contains(@class,'zm-box zm-actions')]/button[1]",
    # the loai
    'the_loai_1_tt_va_hd': '//*[@id="body-scroll"]/div[1]/div[2]/div[2]/div[1]/div[1]/div/a[1]',
    'the_loai_2_tt_va_hd': '//*[@id="body-scroll"]/div[1]/div[2]/div[2]/div[1]/div[2]/div/a[1]',
    'the_loai_3_tt_va_hd': '//*[@id="body-scroll"]/div[1]/div[2]/div[2]/div[1]/div[3]/div/a[1]',
    'the_loai_1_tt_va_hd_top': '//*[@id="body-scroll"]/div[1]/div[2]/div[1]/div/div/div/div/div[1]',
    'the_loai_2_tt_va_hd_top': '//*[@id="body-scroll"]/div[1]/div[2]/div[1]/div/div/div/div/div[1]',
    'the_loai_3_tt_va_hd_top': '//*[@id="body-scroll"]/div[1]/div[2]/div[1]/div/div/div/div/div[1]',
    'listen_category': '//*[@id="body-scroll"]/div[1]/div[2]/div[1]/div[1]/div[2]/div[2]/button',
    # top 100
    't100_nhac_tre': '//*[@id="body-scroll"]/div[1]/div[3]/div/div/div/div/div[1]',
    't100_pop_au_my': '//*[@id="body-scroll"]/div[1]/div[3]/div/div/div/div/div[2]',
    't100_rap_vn': '//*[@id="body-scroll"]/div[1]/div[3]/div/div/div/div/div[3]',
    'listen_song': '//*[@id="body-scroll"]/div[1]/div[2]/div[1]/div[1]/div[2]/div[2]/button',
    # mv
    'mv_viet_nam': '//*[@id="body-scroll"]/div[1]/nav/div/ul/li[1]',
    'mv_us_uk': '//*[@id="body-scroll"]/div[1]/nav/div/ul/li[2]',
    'mv_kpop': '//*[@id="body-scroll"]/div[1]/nav/div/ul/li[3]',
    'mv_hoa_tau': '//*[@id="body-scroll"]/div[1]/nav/div/ul/li[4]',
    'watch_mv': '//*[@id="body-scroll"]/div[1]/div[2]/div[2]/div[1]',
    'back_watch_mv': '//*[@id="video-scroll"]/div/div[2]/div[1]/div[1]/div/div[2]/button[2]',
    'filter': '//*[@id="body-scroll"]/div[1]/div[2]/div[1]/div[2]',
    'filter_nghe_nhieu': '//*[@id="body-scroll"]/div[1]/div[2]/div[1]/div[2]/div[2]/div[1]',
    'filter_noi_bat': '//*[@id="body-scroll"]/div[1]/div[2]/div[1]/div[2]/div[2]/div[2]',
    'filter_moi_nhat': '//*[@id="body-scroll"]/div[1]/div[2]/div[1]/div[2]/div[2]/div[3]',

    'pause_or_play_mv': "//button[@class='--z--control --z--btn --z--control-play']",
    'next_mv': "//div[@class='--z--control-left']//div[2]",
    'full_screen': "//button[@title='Toàn màn hình']",
    'out_full_screen': "//button[@title='Thoát chế độ toàn màn hình']",


    'back': '//*[@id="root"]/div[1]/header/div/div[1]/button[1]',
}
