from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import random

from homepage import HomePage, config


root = {
    'find': ['kham_pha', 'zingchart', 'radio', 'theo_doi', 'nhac_moi', 'the_loai', 'top_100', 'mv'],

    # home
    'kham_pha': ['tab_bai_hat', 'tab_album', 'next_gallery', 'prev_gallery','find', 'zingchart', 'radio', 'theo_doi', 'nhac_moi', 'the_loai', 'top_100', 'mv'],

    'tab_bai_hat': ['kham_pha', 'play_bai_hat', 'play_bai_hat2', 'play_bai_hat3', 'next_gallery', 'prev_gallery'],
    'tab_album': ['kham_pha', 'play_album', 'play_album2', 'next_gallery', 'prev_gallery'],

    'play_bai_hat': ['tab_bai_hat'],
    'play_bai_hat2': ['tab_bai_hat'],
    'play_bai_hat3': ['tab_bai_hat'],

    'next_gallery': ['kham_pha', 'tab_bai_hat'],
    'prev_gallery': ['kham_pha', 'tab_album'],

    'play_album': ['tab_album'],
    'play_album2': ['tab_album'],
    # zing
    'zingchart': ['play_random_song', 'find', 'play_top_song', 'kham_pha'],
    'play_top_song': ['zingchart'],
    'play_random_song': ['zingchart'],
    # radio
    'radio': ['play_radio', 'find', 'kham_pha', 'zingchart', 'theo_doi', 'nhac_moi', 'the_loai', 'top_100', 'mv'],
    'play_radio': ['radio', 'back_radio'],
    'back_radio': ['play_radio'],
    # theo doi
    'theo_doi': ['tab_viet_nam', 'tab_us_uk', 'tab_k_pop', 'tab_hoa_ngu', 'tab_noi_bat', 'click_post', 'kham_pha', 'find'],
    'tab_viet_nam': ['theo_doi'],
    'tab_us_uk': ['theo_doi'],
    'tab_k_pop': ['theo_doi'],
    'tab_hoa_ngu': ['theo_doi'],
    'tab_noi_bat': ['theo_doi'],
    'click_post': ['theo_doi', 'out_post'],
    'out_post': ['click_post'],
    # nhac moi
    'nhac_moi': ['play_music_top', 'play_random', 'find', 'kham_pha'],
    'play_music_top': ['nhac_moi'],
    'play_random': ['nhac_moi'],
    # the loai
    'the_loai': ['the_loai_1_tt_va_hd', 'the_loai_2_tt_va_hd', 'the_loai_3_tt_va_hd', 'find', 'kham_pha'],
    'the_loai_1_tt_va_hd': ['the_loai', 'the_loai_1_tt_va_hd_top'],
    'the_loai_2_tt_va_hd': ['the_loai', 'the_loai_2_tt_va_hd_top'],
    'the_loai_3_tt_va_hd': ['the_loai', 'the_loai_3_tt_va_hd_top'],
    'the_loai_1_tt_va_hd_top': ['the_loai_1_tt_va_hd', 'listen_category'],
    'the_loai_2_tt_va_hd_top': ['the_loai_2_tt_va_hd', 'listen_category'],
    'the_loai_3_tt_va_hd_top': ['the_loai_3_tt_va_hd', 'listen_category'],
    'listen_category': ['the_loai_1_tt_va_hd_top', 'the_loai_2_tt_va_hd_top', 'the_loai_3_tt_va_hd_top'],
    # top 100
    'top_100': ['t100_nhac_tre', 't100_pop_au_my', 't100_rap_vn', 'find', 'kham_pha'],
    't100_nhac_tre': ['top_100', 'listen_song'],
    't100_pop_au_my': ['top_100', 'listen_song'],
    't100_rap_vn': ['top_100', 'listen_song'],
    'listen_song': ['t100_nhac_tre', 't100_pop_au_my', 't100_rap_vn'],
    # mv
    'mv': ['mv_viet_nam', 'mv_us_uk', 'mv_kpop', 'mv_hoa_tau', 'watch_mv', 'find', 'filter', 'kham_pha'],
    'mv_viet_nam': ['mv', 'watch_mv', 'filter'],
    'mv_us_uk': ['mv', 'watch_mv', 'filter'],
    'mv_kpop': ['mv', 'watch_mv', 'filter'],
    'mv_hoa_tau': ['mv', 'watch_mv', 'filter'],
    'filter': ['filter_nghe_nhieu', 'filter_noi_bat', 'filter_moi_nhat', 'mv_viet_nam', 'mv_us_uk', 'mv_kpop', 'mv_hoa_tau', 'watch_mv'],
    'watch_mv': ['back_watch_mv', 'full_screen', 'next_mv', 'pause_or_play_mv'],

    'back_watch_mv': ['mv_viet_nam', 'mv_us_uk', 'mv_kpop', 'mv_hoa_tau', 'watch_mv'],
    'pause_or_play_mv': ['full_screen', 'next_mv', 'out_full_screen'],
    'next_mv': ['back_watch_mv', 'full_screen', 'out_full_screen', 'pause_or_play_mv'],
    'full_screen': ['out_full_screen', 'next_mv', 'pause_or_play_mv'],
    'out_full_screen': ['next_mv', 'pause_or_play_mv', 'back_watch_mv'],

    'filter_nghe_nhieu': ['mv_viet_nam', 'mv_us_uk', 'mv_kpop', 'mv_hoa_tau', 'watch_mv'],
    'filter_noi_bat': ['mv_viet_nam', 'mv_us_uk', 'mv_kpop', 'mv_hoa_tau', 'watch_mv'],
    'filter_moi_nhat': ['mv_viet_nam', 'mv_us_uk', 'mv_kpop', 'mv_hoa_tau', 'watch_mv'],
}

box_left = ['kham_pha', 'zingchart', 'radio', 'theo_doi', 'nhac_moi', 'the_loai', 'top_100', 'mv']

listMusic = ['Yêu 5', 'nên chờ hay nên quên', 'phía sau một cô gái', 'sau tất cả', 'yêu không cần hứa', 'không lấy được vợ', 'thất tình']



driver = webdriver.Chrome(r'C:\Program Files\Google\Chrome\Application\chromedriver.exe')
mp = HomePage(driver)
mp.get_home()
time.sleep(3)

for i in range(5):
    acc1 = random.choice(box_left)
    print('acc1', acc1)
    mp.my_acction(config[acc1])
    time.sleep(3)
    acc2 = random.choice(root[acc1])
    mp.my_acction(config[acc2])
    time.sleep(3)
    while True:
        acc2 = random.choice(root[acc2])
        if acc2 == 'find':
            mp.find_any_song(config[acc2], random.choice(listMusic))
        else:
            try:
                mp.my_acction(config[acc2])
            except:
                driver.back()
                # mp.my_acction(config['back'])
        print(acc2)
        time.sleep(3)



