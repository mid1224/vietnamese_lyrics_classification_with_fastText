import time
import os
import re

from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Insert URLs of playlist in MP3
list_urls = [
    "https://zingmp3.vn/playlist/Nhung-Bai-Hat-Hay-Nhat-Ve-Gia-Dinh/ZWZCZ008.html",
    "https://zingmp3.vn/tim-kiem/bai-hat?q=cha%20m%E1%BA%B9",
    "https://zingmp3.vn/tim-kiem/bai-hat?q=cha%20con",
    "https://zingmp3.vn/tim-kiem/bai-hat?q=l%E1%BB%9Di%20ru%20con",
    "https://zingmp3.vn/album/Valentine-2025-Nghe-Gi-AMEE-ERIK-Duc-Phuc-Quan-A-P/ZWZCW608.html",
    "https://zingmp3.vn/tim-kiem/bai-hat?q=t%C3%ACnh%20y%C3%AAu",
    "https://zingmp3.vn/playlist/Giai-Dieu-Tinh-Yeu/ZWZ9F80U.html",
    "https://zingmp3.vn/playlist/Rap-Tha-Thinh/ZU6A7FIU.html",
    "https://zingmp3.vn/album/Nhac-Que-Huong-Hom-Nay-Khuu-Huy-Vu-Duong-Hong-Loan-Ngoc-Phung-Pham-Tuyet-Nhung/ZODDIAW9.html",
    "https://zingmp3.vn/tim-kiem/bai-hat?q=qu%C3%AA%20h%C6%B0%C6%A1ng",
    "https://zingmp3.vn/album/Que-Huong-Toi-Be-Ngoc-Ngan/ZWZCZ69O.html",
    "https://zingmp3.vn/tim-kiem/bai-hat?q=mi%E1%BB%81n%20qu%C3%AA",
    "https://zingmp3.vn/tim-kiem/bai-hat?q=%C4%91%E1%BB%9Di",
    "https://zingmp3.vn/tim-kiem/bai-hat?q=m%C6%B0u%20sinh",
    "https://zingmp3.vn/album/Cach-Song-O-Doi-Various-Artists/6OEEOUEO.html",
    "https://zingmp3.vn/album/Rap-Viet-Tao-Dong-Luc-Dick-Obito-HIEUTHUHAI-Lil-Wuyn/ZU6C0ZFA.html",
    "https://zingmp3.vn/playlist/Tet-Sum-Vay/ZOBI7ZIE.html",
    "https://zingmp3.vn/album/Giang-Sinh-Ron-Rang-MIN-RHYDER-Tien-Tien-Bui-Cong-Nam-Kai-Dinh/ZWZCWI6C.html",
    "https://zingmp3.vn/playlist/Tet-100--Zing-Choice/67OAAOCF.html",
    "https://zingmp3.vn/album/Nhac-Mung-Sinh-Nhat-Hay-Nhat-Phan-Dinh-Tung-Wanbi-Tuan-Anh-Anne-Marie-Kiroro/ZWZ97ZCC.html",
    "https://zingmp3.vn/tim-kiem/bai-hat?q=h%E1%BB%8Dc%20tr%C3%B2",
    "https://zingmp3.vn/tim-kiem/bai-hat?q=th%E1%BA%A7y%20c%C3%B4",
    "https://zingmp3.vn/album/Hoc-Tro-Oi-Duong-Hue/ZBZB709E.html",
    "https://zingmp3.vn/album/Nam-Thang-Hoc-Tro-Lynk-Lee-Thuy-Chi-OPlus-Han-Sara/ZWZ99OZW.html"
]

max_song_per_playlist = 350 
urls_per_folder = 4 

def setup_driver():
    options = Options()
    options.add_experimental_option("excludeSwitches", ["enable-automation", "enable-logging"])
    options.add_experimental_option('useAutomationExtension', False)
    options.add_argument("--disable-notifications")
    options.add_argument("--start-maximized")
    
    current_folder = os.path.dirname(os.path.abspath(__file__))
    driver_path = os.path.join(current_folder, "msedgedriver.exe")
    
    service = Service(driver_path)
    driver = webdriver.Edge(service=service, options=options)
    return driver

def save_to_txt(folder_name, title, lyrics):
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
    
    filename = re.sub(r'[\\/*?:"<>|]', "", title) + ".txt"
    file_path = os.path.join(folder_name, filename)
    
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(lyrics) 

    print(f"Saved [{folder_name}]: {filename}")
    return True

def process_one_playlist(driver, url, idx, total, global_memory, current_folder_name):
    print(f"\n[{idx}/{total}] Entering Playlist: {url}")
    driver.get(url)
    time.sleep(3) 

    ActionChains(driver).send_keys(Keys.ESCAPE).perform()
    
    count_success = 0
    current_index = 0 
    
    while count_success < max_song_per_playlist:
        songs = driver.find_elements(By.CSS_SELECTOR, ".media-item")
        if not songs: songs = driver.find_elements(By.CSS_SELECTOR, ".select-item")
        
        # Scroll down
        if current_index >= len(songs):
            print(f"Đã duyệt {current_index} bài. Cuộn xuoong de tìm thêm...")
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(3) 
            
            new_songs = driver.find_elements(By.CSS_SELECTOR, ".media-item")
            if not new_songs: new_songs = driver.find_elements(By.CSS_SELECTOR, ".select-item")
            
            if len(new_songs) <= len(songs):
                print(f"Dung lai. Dừng voi {count_success} bài.")
                break
            
            songs = new_songs
            if current_index >= len(songs): continue 

        row = songs[current_index]
        driver.execute_script("arguments[0].scrollIntoView({behavior: 'auto', block: 'center'});", row)
        time.sleep(0.5)

        # Get Title
        title = row.find_element(By.CSS_SELECTOR, ".item-title, .title").text.strip()
        
        # Luu lai ten file da xu ly de tranh trung lap
        check_key = re.sub(r'[\\/*?:"<>|]', "", title).lower().strip()
        if check_key in global_memory:
            current_index += 1
            continue
        global_memory.add(check_key)

        print(f"\nProcessing [{current_index + 1}]: {title}")

        # Open 'More' Menu
        more_btn = row.find_element(By.XPATH, ".//div[contains(@class, 'media-right')]//button[.//i[contains(@class, 'ic-more')]]")
        driver.execute_script("arguments[0].click();", more_btn)
        time.sleep(1.0) 
        
        # Click 'Lyrics'
        lyric_btn = driver.find_element(By.XPATH, "//button//span[contains(text(), 'Lời bài hát')]/..")
        driver.execute_script("arguments[0].click();", lyric_btn)
        time.sleep(2) 

        # Extract Text
        wait = WebDriverWait(driver, 5)
        modal_content = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".modal-content")))
        
        # Handle structural variance
        content_container_list = modal_content.find_elements(By.CSS_SELECTOR, "ul.scroll-content")
        content_container = content_container_list[0] if content_container_list else modal_content

        raw_text = driver.execute_script("return arguments[0].textContent;", content_container)
        
        # Process Lyrics
        clean_lines = []
        for line in raw_text.split('\n'):
            line = line.strip()
            if not line: continue
            line_lower = line.lower()
            if line_lower.startswith("lời bài hát"):
                content_only = re.sub(r'^lời bài hát[:\s-]*', '', line, flags=re.IGNORECASE).strip()
                if content_only: clean_lines.append(content_only)
                continue
            if line_lower in ["đóng góp lời bài hát", "đóng", "đóng góp"]: continue
            if "đóng góp" in line_lower: continue
            if line_lower == "đóng": continue
            clean_lines.append(line)
        
        final_lyrics = "\n".join(clean_lines)

        if final_lyrics:
            save_to_txt(current_folder_name, title, final_lyrics)
            count_success += 1
            print(f"Tiến độ: {count_success}/{max_song_per_playlist}")
            
        # Close window
        ActionChains(driver).send_keys(Keys.ESCAPE).perform()
        time.sleep(0.5)
        
        current_index += 1
            
    return count_success

def crawl_zing():
    driver = setup_driver()
    total_songs_all = 0
    global_memory = set() 
    
    # Removed generic try-except block
    print(f"Dang truy cập trang chủ zingmp3")
    driver.get("https://zingmp3.vn")

    print(f"BẮT ĐẦU CHỜ {60} GIÂY ĐỂ ĐĂNG NHẬP")
    for i in range(60, 0, -5):
        print(f"Còn {i} giây...")
        time.sleep(5)
    
    print("Bắt đầu...")
    
    for idx, url in enumerate(list_urls):
        folder_num = (idx // urls_per_folder) + 6
        current_folder_name = f"data {folder_num}"
        
        songs_crawled = process_one_playlist(driver, url, idx + 1, len(list_urls), global_memory, current_folder_name)
        total_songs_all += songs_crawled
        print(f"Link {idx + 1} da xong. Lưu: {songs_crawled} bài.")
        time.sleep(2)

    driver.quit()
    print(f"\nĐã tìm duoc {total_songs_all} bài.")

crawl_zing()