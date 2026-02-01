import re

input_file = "final_dataset_test.txt"
output_file = "final_dataset_test_translated.txt"

# TỪ ĐIỂN DỊCH
MUSIC_DICT = {
    "a": "một", "about": "về", "accords": "hiệp ước", "account": "tài khoản", "acoustic": "mộc", "act": "hành động", "acting": "diễn xuất",
    "adam": "người", "ae": "anh em", "afraid": "sợ hãi", "after": "sau", "afternoon": "buổi chiều", "again": "lại", "age": "tuổi",
    "ah": "à", "aha": "à ha", "ahh": "à", "ahhh": "àà", "aim": "mục tiêu", "air": "không khí", "airbnb": "Airbnb", "airplane": "máy bay",
    "ain": "không", "alarms": "báo động", "album": "album", "alcohol": "rượu", "ali": "Ali", "alive": "còn sống", "all": "tất cả",
    "alldays": "cả ngày", "alone": "một mình", "alright": "ổn", "altogether": "tổng cộng", "always": "luôn luôn", "am": "là", "amen": "amen",
    "america": "Mỹ", "amp": "âm ly", "ampli": "âm ly", "an": "một", "and": "và", "anime": "anime", "another": "khác", "antifan": "ghét",
    "anymore": "không còn", "anything": "mọi thứ", "anytime": "mọi lúc", "apart": "tách rời", "app": "ứng dụng", "arc": "hình cung",
    "are": "là", "argh": "bực mình", "arms": "cánh tay", "around": "xung quanh", "art": "nghệ thuật", "artist": "nghệ sĩ", "artists": "nghệ sĩ",
    "as": "như", "asap": "càng sớm càng tốt", "ashe": "Ashe", "ask": "hỏi", "asking": "hỏi", "ass": "mông", "at": "tại", "atm": "ATM",
    "attends": "tham dự", "attitude": "thái độ", "audi": "Audi", "audio": "âm thanh", "avatar": "ảnh đại diện", "awake": "tỉnh táo",
    "away": "xa", "aw": "ôi", "ayo": "ê", "ayy": "yo", "babe": "em yêu", "baby": "cưng", "back": "lưng", "backpack": "ba lô",
    "bad": "tệ", "badboy": "trai hư", "badgirl": "cô gái hư", "badvibe": "cảm giác xấu", "bag": "túi", "bake": "nướng", "ball": "quả bóng",
    "ballad": "ballad", "ballin": "sang chảnh", "balling": "chơi bóng", "band": "ban nhạc", "bang": "tiếng nổ", "bank": "ngân hàng",
    "bar": "quán", "bass": "âm trầm", "bat": "con dơi", "bay": "vịnh", "be": "là", "beach": "bãi biển", "beat": "giai điệu",
    "beating": "nhịp đập", "beautiful": "đẹp", "because": "bởi vì", "become": "trở thành", "bed": "giường", "been": "từng", "before": "trước",
    "begin": "bắt đầu", "behind": "sau", "believe": "tin", "bell": "chuông", "belong": "thuộc về", "belongs": "thuộc về", "ben": "bên",
    "best": "tốt nhất", "bestfriend": "bạn thân", "beter": "tốt hơn", "better": "tốt hơn", "big": "to", "bigboi": "trai", "bigdaddy": "bố",
    "bikini": "đồ bơi bikini", "bill": "hóa đơn", "billy": "Billy", "bin": "thùng", "birthday": "sinh nhật", "bitch": "chó", "bitchen": "tệ",
    "bitten": "bị cắn", "black": "màu đen", "blame": "đổ lỗi", "bless": "ban phước", "blessed": "hạnh phúc", "blessing": "phước lành",
    "blind": "mù", "bling": "lấp lánh", "blow": "thổi", "blue": "màu xanh", "bmx": "xe", "body": "cơ thể", "boi": "chàng trai",
    "bolero": "bolero", "bom": "bom", "bong": "ống", "book": "sách", "boom": "bùng nổ", "boo": "cưng", "borrowed": "đã mượn", "boss": "sếp",
    "both": "cả hai", "bottom": "đáy", "bout": "về", "bowling": "bowling", "boy": "con trai", "boyfriend": "bạn trai", "boys": "con trai",
    "bra": "áo ngực", "brah": "anh em", "brain": "bộ não", "brand": "thương hiệu", "breaking": "phá vỡ", "bridge": "cây cầu", "bright": "sáng",
    "bring": "mang đến", "brings": "mang đến", "bro": "anh em", "brought": "đã mang", "buff": "vạm vỡ", "build": "xây dựng", "building": "tòa nhà",
    "bully": "bắt nạt", "bum": "kẻ lười", "bump": "va chạm", "burning": "đang cháy", "business": "kinh doanh", "butt": "mông", "but": "nhưng",
    "buy": "mua", "bye": "tạm biệt", "by": "bởi", "cabernet": "nho", "cacao": "ca cao", "cafe": "cà phê", "cakes": "bánh", "calendar": "lịch",
    "cali": "Cali", "call": "gọi", "callin": "gọi", "calling": "gọi", "calm": "bình tĩnh", "came": "đã đến", "camera": "máy ảnh",
    "cam": "máy", "can": "có thể", "candles": "nến", "candy": "kẹo", "cannot": "không thể", "cant": "không thể", "capital": "thủ đô",
    "cap": "mũ", "car": "xe hơi", "cara": "mặt", "carat": "cara", "card": "thẻ", "care": "chăm sóc", "careful": "cẩn thận",
    "careless": "cẩu thả", "cares": "quan tâm", "carey": "Carey", "carried": "đã mang", "caster": "người", "catch": "bắt", "cause": "nguyên nhân",
    "cd": "đĩa", "celebrate": "ăn mừng", "centimet": "cm", "certain": "chắc chắn", "chain": "dây chuyền", "chains": "dây chuyền",
    "champ": "vô địch", "champagne": "rượu", "champion": "vô địch", "chance": "cơ hội", "change": "thay đổi", "changed": "thay đổi",
    "chanel": "Chanel", "chardonnay": "rượu", "chat": "tán", "cheap": "rẻ", "check": "kiểm tra", "checklist": "danh sách", "cheer": "cổ vũ",
    "cheers": "chúc mừng", "chest": "ngực", "chill": "thư giãn", "chillin": "thư giãn", "chilling": "thư giãn", "chibi": "nhỏ",
    "chirstmas": "Giáng sinh", "chistmas": "Giáng sinh", "chocolates": "sô-cô-la", "chords": "hợp âm", "chorus": "điệp khúc",
    "christian": "Kitô", "christmas": "Giáng sinh", "church": "nhà thờ", "circle": "vòng tròn", "city": "thành phố", "clap": "vỗ tay",
    "classy": "sang trọng", "claus": "Noel", "clef": "khóa", "clip": "video", "clo": "quần áo", "clow": "clow", "cm": "cm", "close": "đóng",
    "closed": "đã đóng", "closing": "kết thúc", "cloud": "đám mây", "cloudy": "nhiều mây", "club": "hội", "coaster": "lót", "cocky": "kiêu",
    "coda": "đoạn kết", "code": "mã", "cody": "Cody", "coffee": "cà phê", "cold": "lạnh", "college": "đại học", "combo": "gói",
    "come": "đến", "comeback": "trở lại", "comes": "đến", "comfort": "thoải mái", "coming": "đang đến", "comin": "đến", "comment": "bình luận",
    "communist": "cộng sản", "complain": "phàn nàn", "comple": "bộ đồ", "confessed": "thú nhận", "connect": "kết nối", "content": "nội dung",
    "control": "kiểm soát", "con": "lừa", "cook": "nấu", "cookie": "bánh quy", "coolin": "mát", "cooling": "làm mát", "cool": "ngầu",
    "cosplay": "hóa trang", "could": "có thể", "count": "đếm", "countdown": "đếm ngược", "cover": "cover", "covid": "Covid",
    "cowboy": "cao bồi", "cozy": "ấm cúng", "crawl": "bò", "crazy": "điên", "crew": "đội", "crown": "vương miện", "crush": "thích",
    "cry": "khóc", "cub": "thú", "cum": "cùng", "cup": "cốc", "cupid": "cupid", "cute": "dễ thương", "cuz": "vì", "cypher": "mật mã",
    "daddy": "bố", "damn": "chết tiệt", "dance": "nhảy", "dancing": "nhảy", "dare": "dám", "dark": "bóng tối", "date": "hẹn hò",
    "dats": "đó", "davis": "Davis", "dawn": "bình minh", "dawg": "bạn", "day": "ngày", "days": "ngày", "deadline": "hạn chót",
    "deal": "thỏa thuận", "dear": "thân mến", "deep": "sâu", "delay": "trì hoãn", "demo": "mẫu", "den": "hang", "deny": "từ chối",
    "descend": "xuống", "design": "thiết kế", "designer": "nhà thiết kế", "desires": "khao khát", "dessine": "vẽ", "destiny": "định mệnh",
    "details": "chi tiết", "devil": "ác quỷ", "diamond": "kim cương", "dick": "tồi", "did": "đã làm", "die": "chết", "dim": "mờ",
    "ding": "chuông", "dior": "Dior", "disappear": "biến mất", "display": "hiển thị", "distance": "khoảng cách", "diva": "diva",
    "dive": "lặn", "dizz": "mắng", "dj": "DJ", "dm": "tin", "do": "làm", "doesn": "không", "doin": "đang làm", "dolce": "ngọt",
    "dollar": "đô la", "don": "mặc", "done": "xong", "dont": "không", "door": "cửa", "dopamine": "dopamine", "dope": "ngầu", "dory": "Dory",
    "dose": "liều lượng", "dot": "chấm", "double": "gấp đôi", "down": "xuống", "draco": "súng", "drillin": "nhạc", "drama": "kịch",
    "dream": "giấc mơ", "dreaming": "mơ", "dreams": "giấc mơ", "drinking": "uống rượu", "drip": "phong cách", "drive": "lái xe",
    "drop": "thả", "duck": "vịt", "dude": "bạn", "duo": "cặp", "dust": "bụi", "each": "mỗi", "easy": "dễ", "eat": "ăn", "echo": "tiếng vang",
    "edm": "EDM", "edward": "Edward", "ego": "tôi", "eight": "tám", "eleven": "mười một", "else": "khác", "email": "email",
    "end": "kết thúc", "english": "tiếng Anh", "enough": "đủ", "enter": "vào", "even": "thậm chí", "ever": "từng", "everest": "Everest",
    "every": "mỗi", "everybody": "mọi người", "everyday": "hàng ngày", "everyone": "mọi người", "everything": "mọi thứ",
    "everywhere": "mọi nơi", "eyo": "chào", "exists": "tồn tại", "existe": "có", "explode": "nổ", "eye": "mắt", "eyes": "mắt",
    "fa": "độc thân", "face": "mặt", "fact": "sự thật", "facebook": "Facebook", "fade": "phai", "fail": "thất bại", "fake": "giả",
    "fall": "rơi", "fallin": "đang yêu", "falling": "rơi", "fam": "gia đình", "fame": "danh tiếng", "families": "gia đình",
    "family": "gia đình", "famous": "nổi tiếng", "fan": "fan", "fancy": "sang chảnh", "fanmade": "fan làm", "far": "xa",
    "fashion": "thời trang", "fate": "số phận", "favourite": "ưa thích", "fear": "nỗi sợ", "fears": "nỗi sợ", "feat": "thuộc",
    "feed": "bài đăng", "feel": "cảm thấy", "feeling": "cảm giác", "feelings": "cảm xúc", "felt": "cảm thấy", "feliz": "vui",
    "festival": "lễ hội", "fight": "chiến đấu", "fighter": "chiến binh", "fill": "lấp đầy", "filled": "đầy", "filter": "bộ lọc",
    "final": "cuối cùng", "finally": "cuối cùng", "fin": "hết", "find": "tìm", "fine": "tốt", "fire": "lửa", "fireworks": "pháo hoa",
    "first": "đầu tiên", "fit": "vừa", "five": "năm", "fix": "sửa", "fixing": "sửa", "flag": "cờ", "flame": "ngọn lửa", "flames": "ngọn lửa",
    "flash": "chớp", "flashback": "hồi tưởng", "flex": "khoe", "flexin": "khoe", "flexing": "khoe", "floor": "sàn", "flow": "flow",
    "fly": "bay", "flying": "bay", "fm": "đài", "focus": "tập trung", "fold": "gấp", "follow": "theo dõi", "followers": "người theo dõi",
    "fond": "thích", "font": "phông chữ", "food": "thức ăn", "fool": "ngốc", "fooling": "đùa giỡn", "footprints": "dấu chân",
    "footsteps": "bước chân", "for": "cho", "force": "ép buộc", "ford": "Ford", "forever": "mãi mãi", "forevermore": "mãi mãi",
    "forget": "quên", "forgive": "tha thứ", "form": "hình dáng", "forth": "về trước", "found": "tìm thấy", "four": "bốn", "free": "tự do",
    "freefire": "Free Fire", "freaky": "kỳ quặc", "freaking": "kinh", "freestyle": "ngẫu hứng", "frequency": "tần số", "fresh": "tươi",
    "friday": "thứ sáu", "friend": "bạn", "friendzone": "friendzone", "from": "từ", "froze": "đông băng", "frozen": "đông băng",
    "ft": "hợp tác", "fuck": "chửi", "full": "đầy", "funny": "vui", "gala": "tiệc", "gal": "gái", "game": "trò chơi", "gang": "băng",
    "gangz": "băng", "garden": "vườn", "gave": "đã cho", "gay": "đồng tính", "gd": "gia đình", "gemini": "Gemini", "gen": "gen",
    "gentle": "nhẹ nhàng", "gentleman": "quý ông", "get": "lấy", "gettin": "lấy", "ge": "thế", "gift": "quà", "gifts": "quà",
    "gimme": "cho tôi", "gin": "rượu", "girl": "cô gái", "girls": "cô gái", "give": "cho", "glow": "tỏa sáng", "glowing": "tỏa sáng",
    "go": "đi", "goal": "mục tiêu", "god": "chúa", "goes": "đi", "going": "đi", "gone": "biến mất", "gonna": "sẽ", "good": "tốt",
    "goodboy": "trai ngoan", "goodbye": "tạm biệt", "goodnight": "ngủ ngon", "google": "Google", "got": "đã có", "gotta": "phải",
    "goyard": "Goyard", "grace": "ân sủng", "green": "xanh lá", "ground": "mặt đất", "grow": "phát triển", "gta": "GTA", "gucci": "Gucci",
    "guess": "đoán", "guitar": "guitar", "guitarist": "người chơi guitar", "gun": "súng", "guy": "chàng trai", "guys": "mọi người",
    "gym": "phòng", "had": "có", "hailey": "Hailey", "hair": "tóc", "hand": "bàn tay", "hands": "đôi tay", "happy": "vui vẻ",
    "hard": "khó", "harmony": "hòa âm", "has": "có", "hate": "ghét", "hater": "kẻ ghét", "haters": "người ghét", "have": "có",
    "hawaii": "Hawaii", "he": "anh ấy", "head": "đầu", "headlights": "đèn pha", "heal": "chữa lành", "healthy": "khỏe mạnh",
    "hear": "nghe", "heard": "đã nghe", "heart": "trái tim", "heartbeat": "nhịp tim", "heartbreak": "tan vỡ", "hearts": "trái tim",
    "heat": "nhiệt", "heavy": "nặng", "helen": "Helen", "hello": "chào", "her": "cô ấy", "here": "đây", "hey": "này", "hi": "chào",
    "hide": "ẩn", "hiding": "đang ẩn", "high": "cao", "higher": "cao hơn", "highlight": "điểm nhấn", "highway": "xa lộ", "him": "anh ấy",
    "hiphop": "hiphop", "hip": "hông", "his": "của anh ấy", "histoire": "chuyện", "hit": "hit", "hiv": "HIV", "hoe": "cuốc",
    "hold": "giữ", "home": "nhà", "homies": "bạn", "homie": "bạn thân", "honda": "Honda", "honey": "người yêu", "hoodie": "áo hoodie",
    "hood": "khu", "hook": "điệp khúc", "hope": "hy vọng", "hoppin": "nhảy", "hot": "nóng", "hours": "giờ", "house": "nhà",
    "how": "thế nào", "hmm": "ừm", "humble": "khiêm tốn", "hunger": "cơn đói", "hungry": "đói", "hurt": "đau", "hurray": "hoan hô",
    "hustle": "cày cuốc", "ice": "đá", "iced": "có đá", "icon": "biểu tượng", "icy": "lạnh", "idea": "ý tưởng", "idol": "thần tượng",
    "if": "nếu", "ignite": "châm ngòi", "im": "tôi là", "imma": "tôi sẽ", "in": "trong", "inbox": "nhắn tin", "inside": "bên trong",
    "instead": "thay vì", "insta": "ảnh", "instagram": "ảnh", "into": "vào", "intro": "mở đầu", "invite": "mời", "invited": "được mời",
    "iphone": "iPhone", "iran": "Iran", "is": "là", "isaac": "Isaac", "isn": "không", "issa": "là", "it": "nó", "its": "của nó",
    "jack": "Jack", "jacket": "áo khoác", "jackson": "Jackson", "james": "James", "jazz": "jazz", "jingle": "chuông", "jinx": "đen",
    "job": "công việc", "john": "John", "johnny": "Johnny", "joy": "niềm vui", "juliet": "Juliet", "jun": "tháng sáu", "just": "chỉ",
    "justify": "biện minh", "justin": "Justin", "karma": "nghiệp", "karaoke": "karaoke", "keep": "giữ", "keepin": "giữ",
    "keeping": "giữ", "kelvin": "Kelvin", "kendrick": "Kendrick", "key": "khóa", "kiwi": "kiwi", "kick": "đá", "kicks": "giày",
    "kill": "giết", "killin": "giết", "kinda": "kiểu", "kiss": "hôn", "kissed": "đã hôn", "kitkat": "Kitkat", "knew": "biết",
    "knock": "gõ cửa", "know": "biết", "knowing": "biết", "knows": "biết", "kobe": "Kobe", "kpi": "KPI", "kr": "Hàn",
    "kute": "dễ thương", "lab": "phòng thí nghiệm", "lady": "quý cô", "lag": "trễ", "lambor": "Lamborghini", "lamborghini": "Lamborghini",
    "last": "cuối cùng", "late": "muộn", "later": "sau này", "law": "luật", "leader": "lãnh đạo", "learn": "học", "leave": "rời đi",
    "legal": "hợp pháp", "legend": "huyền thoại", "legit": "uy tín", "lemme": "để tôi", "lemonade": "nước chanh", "let": "để",
    "level": "cấp độ", "liberty": "tự do", "lick": "liếm", "lie": "nói dối", "life": "cuộc sống", "lift": "nâng", "light": "ánh sáng",
    "lights": "đèn", "like": "thích", "lil": "nhỏ", "line": "dòng", "lines": "dòng", "listen": "nghe", "lit": "tuyệt", "little": "nhỏ",
    "live": "sống", "lives": "sống", "liveshow": "show", "livestream": "trực tiếp", "loaded": "đầy", "local": "địa phương", "lock": "khóa",
    "lofi": "lofi", "london": "Luân Đôn", "lonely": "cô đơn", "lonlely": "cô đơn", "long": "dài", "longer": "dài hơn", "look": "nhìn",
    "lookin": "nhìn", "lord": "chúa", "lose": "mất", "lost": "lạc", "lot": "nhiều", "loud": "ồn", "louis": "Louis", "love": "yêu",
    "loved": "được yêu", "lover": "người yêu", "loves": "yêu", "loving": "yêu", "low": "thấp", "lowkey": "kín đáo", "lyrics": "lời",
    "macao": "Ma Cao", "made": "làm", "magic": "ma thuật", "mafia": "mafia", "making": "làm", "makes": "làm", "makin": "làm",
    "mama": "mẹ", "man": "đàn ông", "mandy": "Mandy", "manipulate": "thao túng", "many": "nhiều", "map": "bản đồ", "marijuana": "cỏ",
    "maria": "Maria", "mariah": "Mariah", "marry": "kết hôn", "marshmallow": "marshmallow", "marvel": "Marvel", "masked": "mặt nạ",
    "massage": "mát xa", "match": "khớp", "matcha": "trà xanh", "matching": "phù hợp", "matrix": "ma trận", "matter": "vấn đề",
    "mary": "Mary", "mashup": "trộn", "max": "hết", "may": "có thể", "maybe": "có lẽ", "me": "tôi", "meant": "nghĩa là",
    "medicine": "thuốc", "meet": "gặp", "melody": "giai điệu", "meme": "meme", "men": "đàn ông", "merry": "vui vẻ", "mess": "tin nhắn",
    "message": "tin nhắn", "messi": "Messi", "michael": "Michael", "micro": "mic", "midas": "Midas", "midnight": "nửa đêm",
    "might": "có thể", "migos": "Migos", "miley": "Miley", "milly": "Milly", "mind": "tâm trí", "mine": "của tôi", "minute": "phút",
    "minzy": "Minzy", "miracle": "phép", "miss": "nhớ", "missing": "thiếu", "mistakes": "sai lầm", "mistletoe": "tầm gửi",
    "mistle": "tầm", "mix": "trộn", "miu": "Miu", "mm": "mm", "mob": "băng đảng", "mochi": "bánh", "moet": "rượu", "mofo": "tồi",
    "moi": "tôi", "molly": "Molly", "moment": "khoảnh khắc", "monday": "thứ hai", "money": "tiền", "mono": "đơn", "mommy": "mẹ",
    "momy": "mẹ", "moon": "mặt trăng", "moonwalking": "đi lùi", "more": "nhiều hơn", "morning": "buổi sáng", "most": "nhất",
    "mother": "mẹ", "motherfucking": "chết tiệt", "move": "di chuyển", "moved": "xúc động", "moves": "chuyển động", "moving": "di chuyển",
    "movin": "đi", "movier": "phim", "mr": "ông", "mtv": "kênh", "much": "nhiều", "music": "âm nhạc", "must": "phải", "mustang": "ngựa",
    "my": "của tôi", "myself": "bản thân", "myfriend": "bạn tôi", "name": "tên", "nasty": "tệ", "near": "gần", "neck": "cổ",
    "need": "cần", "needed": "cần thiết", "neko": "mèo", "nemo": "Nemo", "neon": "neon", "neo": "mới", "nerd": "mọt", "netflix": "Netflix",
    "net": "mạng", "never": "không bao giờ", "neverland": "vùng đất hứa", "new": "mới", "newfeed": "tin", "newmusic": "nhạc",
    "news": "tin tức", "newsfeed": "tin", "next": "kế tiếp", "nicotine": "nicotine", "nick": "biệt danh", "nickname": "biệt danh",
    "night": "đêm", "nights": "đêm", "nike": "Nike", "nine": "số chín", "no": "không", "nobel": "Nobel", "nobody": "không ai",
    "noel": "Giáng sinh", "noid": "lo lắng", "noise": "ồn", "none": "không", "nonstop": "không dừng", "nor": "cũng không",
    "north": "phía bắc", "not": "không", "note": "ghi chú", "notes": "ghi chú", "nothing": "không có gì", "now": "bây giờ",
    "numb": "tê", "number": "số", "object": "vật thể", "ocean": "đại dương", "of": "của", "off": "tắt", "og": "cũ", "oh": "ồ",
    "ok": "được", "okay": "được", "old": "cũ", "omega": "cuối", "on": "trên", "once": "một lần", "one": "một", "online": "trực tuyến",
    "onl": "trực tuyến", "only": "chỉ", "open": "mở", "opened": "đã mở", "opera": "opera", "or": "hoặc", "order": "đơn hàng",
    "oscar": "Oscar", "ost": "nhạc", "other": "khác", "others": "khác", "our": "của chúng ta", "out": "ra ngoài", "outfit": "trang phục",
    "outro": "kết bài", "outside": "bên ngoài", "over": "qua", "overdose": "quá liều", "overthinking": "nghĩ nhiều", "own": "sở hữu",
    "pablo": "Pablo", "pack": "gói", "pain": "đau", "panama": "Panama", "panda": "gấu", "pants": "quần", "papa": "bố", "paper": "giấy",
    "paradise": "thiên đường", "parents": "cha mẹ", "paris": "Paris", "park": "công viên", "part": "phần", "participle": "phân từ",
    "party": "tiệc", "pass": "vượt qua", "passed": "vượt qua", "past": "quá khứ", "pause": "tạm dừng", "pay": "trả tiền",
    "peace": "hòa bình", "pen": "nhà lầu", "penthouse": "nhà lầu", "people": "mọi người", "per": "mỗi", "perfect": "hoàn hảo",
    "pestilence": "dịch", "peter": "Peter", "ph": "PH", "phone": "điện thoại", "piano": "piano", "picasso": "Picasso", "pick": "chọn",
    "picture": "hình ảnh", "piece": "mảnh", "pier": "bến tàu", "pit": "hố", "pinky": "hồng", "pixel": "pixel", "place": "nơi",
    "plan": "kế hoạch", "play": "chơi", "playing": "chơi", "please": "làm ơn", "plus": "cộng", "poker": "poker", "point": "điểm",
    "polaroid": "Polaroid", "pop": "pop", "poppin": "sôi động", "porter": "người vác", "pose": "tạo dáng", "post": "bài đăng",
    "poster": "áp phích", "pour": "rót", "poured": "rót", "power": "sức mạnh", "pow": "nổ", "prada": "Prada", "praising": "khen",
    "pray": "cầu", "prayers": "cầu", "prefix": "tiền tố", "pre": "trước", "preparations": "chuẩn bị", "present": "hiện tại",
    "pretty": "đẹp", "price": "giá", "priceless": "vô giá", "prob": "vấn đề", "prod": "sản xuất", "pro": "chuyên nghiệp",
    "producer": "nhà sản xuất", "profile": "hồ sơ", "promise": "lời hứa", "prospero": "thịnh vượng", "protect": "giữ",
    "pt": "điểm", "pull": "kéo", "push": "đẩy", "put": "đặt", "quad/qt": "đơn vị", "queen": "nữ hoàng", "quit": "từ bỏ",
    "radar": "ra đa", "radio": "radio", "rai": "nhạc Rai", "rain": "mưa", "raise": "nâng lên", "random": "ngẫu nhiên",
    "rap": "rap", "rapper": "rapper", "rappin": "đang rap", "raptor": "chim săn mồi", "rate": "tỉ lệ", "rave": "cuồng nhiệt",
    "raw": "thô", "reach": "vươn tới", "read": "đọc", "ready": "sẵn sàng", "reality": "thật", "really": "thật sự",
    "receiver": "người nhận", "recognize": "nhận", "record": "ghi âm", "red": "đỏ", "rejoice": "vui mừng", "relate": "hợp",
    "release": "ra", "remain": "còn", "remix": "phối", "repeat": "lại", "rep": "đại diện", "represent": "diễn", "resist": "chống",
    "ressemble": "giống", "respect": "tôn trọng", "rest": "nghỉ ngơi", "review": "đánh giá", "rewind": "tua lại",
    "rhythm": "nhịp", "richkid": "giàu", "rick": "Rick", "ride": "đi xe", "rider": "người lái", "ring": "nhẫn", "ringing": "reo",
    "riri": "Riri", "rise": "tăng", "road": "đường", "robber": "cướp", "rock": "rock", "rocket": "tên lửa", "roll": "cuộn",
    "roller": "lăn", "rolling": "đang lăn", "rollin": "lăn", "room": "phòng", "rose": "hoa hồng", "round": "tròn", "rtee": "Rtee",
    "rum": "rượu", "run": "chạy", "running": "chạy", "runway": "đường băng", "rv": "Rap Việt", "sad": "buồn", "safe": "an toàn",
    "said": "đã nói", "saint": "thánh", "salem": "Salem", "sale": "bán", "sales": "doanh số", "same": "giống", "santa": "Noel",
    "satan": "quỷ", "saturday": "thứ bảy", "save": "lưu", "say": "nói", "saying": "nói", "scared": "sợ", "scarlett": "đỏ tươi rực rỡ",
    "scene": "cảnh", "sea": "biển", "search": "tìm kiếm", "seatbelt": "dây an toàn", "second": "giây", "secret": "bí mật",
    "see": "thấy", "seek": "tìm kiếm", "seem": "có vẻ", "seems": "có vẻ", "seen": "đã thấy", "selfie": "tự sướng", "self": "bản thân",
    "send": "gửi", "sent": "đã gửi", "seo": "sao", "series": "loạt", "serious": "nghiêm túc", "service": "dịch vụ", "set": "đặt",
    "season": "mùa", "seven": "bảy", "sexy": "gợi cảm", "shady": "mờ", "sh": "xe SH", "shake": "lắc", "shakin": "đang lắc",
    "shame": "ngại", "shang": "sang", "share": "chia sẻ", "shawty": "cô em", "she": "cô ấy", "shine": "tỏa sáng", "shining": "tỏa sáng",
    "shin": "Shin", "ship": "ghép đôi", "shit": "tệ", "shogun": "Shogun", "shoot": "bắn", "shootin": "đang bắn", "shop": "cửa hàng",
    "shopping": "mua sắm", "shopee": "Shopee", "shot": "phát bắn", "shouldn": "không", "shout": "hét", "show": "trình diễn",
    "shows": "chương trình", "showin": "đang thể hiện", "shy": "ngại", "side": "bên", "sigh": "thở dài", "sight": "tầm", "sign": "ký",
    "sim": "sim", "simba": "Simba", "simple": "đơn giản", "sing": "hát", "singer": "ca sĩ", "singing": "hát", "single": "đơn",
    "sings": "hát", "sins": "tội", "sin": "tội", "siri": "Siri", "sister": "chị em", "sit": "ngồi", "six": "sáu", "size": "kích cỡ",
    "skill": "kỹ năng", "skills": "kỹ", "sky": "bầu trời", "sleep": "ngủ", "slow": "chậm", "slowly": "chậm", "slowmo": "quay chậm",
    "small": "nhỏ", "smartphone": "điện thoại", "smile": "nụ cười", "smoke": "khói", "snitch": "kẻ mách lẻo", "snowman": "người tuyết",
    "snow": "tuyết", "soda": "soda", "sofa": "ghế", "sold": "bán", "solo": "đơn", "some": "vài", "someone": "ai đó", "something": "thứ gì đó",
    "sometimes": "thỉnh thoảng", "song": "bài hát", "songs": "bài hát", "soon": "sớm", "sorry": "xin lỗi", "soul": "linh hồn",
    "sound": "âm thanh", "south": "phía nam", "space": "không gian", "special": "đặc biệt", "spend": "tiêu", "spending": "đang tiêu",
    "spicy": "cay", "spin": "xoay", "spinning": "xoay", "spirits": "linh hồn", "spotify": "Spotify", "split": "tách", "spot": "điểm",
    "spring": "mùa xuân", "squad": "đội", "st": "số", "stage": "sân khấu", "stand": "đứng", "standing": "đứng", "star": "ngôi sao",
    "stars": "ngôi sao", "start": "bắt đầu", "stare": "nhìn", "state": "trạng thái", "status": "tin", "stave": "khuông nhạc",
    "stay": "ở lại", "steal": "lấy", "step": "bước", "stee": "phong cách", "still": "vẫn", "stop": "dừng", "store": "cửa hàng",
    "story": "câu chuyện", "straigh": "thẳng", "straight": "thẳng", "stream": "trực tuyến", "street": "đường", "string": "dây",
    "strings": "dây", "studio": "phòng thu", "stu": "phòng thu", "stuck": "mắc kẹt", "stunning": "tuyệt đẹp", "style": "phong cách",
    "sublimation": "thăng hoa", "suck": "tệ", "summer": "mùa hè", "sun": "mặt trời", "sunrise": "bình minh", "sunset": "hoàng hôn",
    "superman": "siêu nhân", "superstar": "siêu sao", "sure": "chắc chắn", "surprise": "ngạc nhiên", "swag": "ngầu", "swear": "thề",
    "sweet": "ngọt", "sweetie": "cưng", "swervin": "lạng lách", "swing": "đung đưa", "switch": "đổi", "system": "hệ thống",
    "take": "lấy", "taking": "lấy", "talk": "nói", "talking": "nói", "tall": "cao", "taste": "vị", "tasty": "ngon", "tattoo": "hình xăm",
    "team": "đội", "tears": "nước mắt", "teen": "thiếu niên", "telephone": "điện thoại", "tell": "nói", "telling": "nói", "tend": "xu hướng",
    "ten": "mười", "thank": "cảm ơn", "thanks": "cảm ơn", "that": "đó", "thats": "đó là", "the": "mạo từ", "them": "họ", "then": "sau đó",
    "there": "đó", "these": "những cái này", "they": "họ", "thing": "vật", "things": "mọi thứ", "think": "nghĩ", "thinking": "đang nghĩ",
    "third": "ba", "this": "cái này", "those": "những cái kia", "though": "mặc dù", "three": "ba", "through": "xuyên qua", "throw": "ném",
    "thursday": "thứ năm", "tiamo": "yêu", "tidings": "tin tức", "ties": "dây", "tight": "chặt", "tiktok": "TikTok", "till": "đến khi",
    "timberland": "giày", "time": "thời gian", "tiny": "nhỏ xíu", "tivi": "ti vi", "today": "nay", "toddy": "đồ uống nóng",
    "together": "cùng nhau", "tomorrow": "mai", "tonight": "tối nay", "too": "quá", "top": "đỉnh", "touch": "chạm", "tour": "chuyến lưu diễn",
    "town": "thị trấn", "track": "bản nhạc", "tracy": "Tracy", "train": "tàu", "trance": "trance", "trap": "trap", "trappin": "buôn trap",
    "trapping": "bẫy", "trauma": "chấn thương", "travel": "du lịch", "treasure": "kho báu", "treat": "đối", "tree": "cây",
    "trees": "cây", "trend": "xu hướng", "triple": "gấp ba", "trippin": "ảo giác", "triste": "buồn", "tronie": "Tronie", "trop": "quá",
    "trust": "tin tưởng", "true": "đúng", "try": "thử", "trying": "đang thử", "tryna": "muốn", "tuesday": "thứ ba", "turn": "quay",
    "turning": "xoay", "turnin": "đang quay", "tut": "chậc", "tv": "ti vi", "twenty": "hai mươi", "twerk": "lắc mông",
    "twerking": "đang lắc mông", "twice": "hai", "tyga": "Tyga", "type": "loại", "u": "bạn", "uh": "ồ", "uhm": "ừm", "um": "ừm",
    "un": "một", "under": "dưới", "underdog": "yếu", "underground": "ngầm", "unit": "đơn vị", "unite": "đoàn kết", "until": "đến khi",
    "up": "lên", "us": "chúng ta", "use": "dùng", "used": "đã dùng", "user": "người dùng", "usher": "dẫn dắt", "valentine": "tình",
    "vali": "vali", "valse": "van", "various": "nhiều", "var": "va chạm", "vein": "mạch", "vengeance": "thù", "vents": "lỗ",
    "verse": "lời", "version": "bản", "very": "rất", "vest": "vét", "vibe": "vibe", "vibes": "vibe", "vibing": "vui", "vibrato": "rung",
    "vicky": "Vicky", "vida": "đời", "video": "video", "vieon": "VieON", "vienamese": "người Việt", "vietnamese": "người Việt",
    "vietnam": "Việt Nam", "viettelpay": "ViettelPay", "view": "xem", "villa": "biệt thự", "vincom": "Vincom", "vinmart": "Vinmart",
    "vinz": "Vinz", "viral": "lan truyền", "visa": "thẻ", "vis": "mặt", "viu": "Viu", "viva": "vui", "vivo": "sống", "vivra": "sống",
    "vn": "Việt Nam", "vodka": "rượu", "voient": "thấy", "vois": "thấy", "volume": "âm", "voudras": "muốn", "vow": "thề", "vrt": "rap",
    "vuitton": "Vuitton", "vvs": "đá", "wah": "chà", "wait": "chờ", "waiting": "chờ", "wake": "thức dậy", "walk": "đi bộ",
    "walking": "đang đi", "wanna": "muốn", "want": "muốn", "wanted": "đã muốn", "warmth": "ấm", "war": "chiến tranh",
    "wars": "chiến tranh", "warm": "ấm", "was": "đã là", "wassup": "có chuyện gì", "waste": "phí", "watch": "xem", "water": "nước",
    "wave": "sóng", "waves": "sóng", "way": "cách", "ways": "cách", "we": "chúng ta", "week": "tuần", "welcome": "chào mừng",
    "well": "tốt", "wendy": "Wendy", "were": "đã là", "what": "gì", "whatever": "gì", "when": "khi", "where": "đâu", "wherever": "đâu",
    "while": "trong khi", "whisky": "rượu", "whisper": "thầm", "who": "ai", "whole": "toàn bộ", "whoo": "vui", "whut": "gì",
    "why": "tại sao", "wifi": "wifi", "wild": "hoang dã", "will": "sẽ", "winter": "mùa đông", "winx": "Winx", "wish": "ước",
    "wishes": "ước", "wishlist": "danh", "wit": "với", "with": "với", "without": "không có", "wo": "ồ", "woman": "phụ nữ",
    "won": "tiền Hàn", "wonhae": "muốn", "wonder": "tự hỏi", "work": "làm việc", "working": "làm việc", "woring": "làm việc",
    "world": "thế giới", "worry": "lo lắng", "worth": "đáng", "would": "sẽ", "wow": "uầy", "write": "viết", "written": "đã viết",
    "year": "năm", "years": "năm", "young": "trẻ", "your": "của bạn", "yours": "của bạn", "yourself": "chính bạn", "yes": "có",
    "yeucahat": "yêu ca hát", "zero": "không", "zone": "vùng", "yahoo": "Yahoo", "yakuza": "Yakuza", "yard": "sân", "yay": "vui quá",
    "yeah": "vâng", "yearly": "hàng năm", "yeogi": "đây", "yeux": "mắt", "young": "trẻ", "your": "của bạn", "yours": "của bạn",
    "yourself": "chính bạn", "yup": "được", "zalo": "Zalo", "zone": "khu vực", 
    "make":"làm", "mic":"micro", "movie":"phim", "nc":"không có", "rack":"giá đỡ", "racks":"nhiều giá", "real":"thật", "renewed":"được gia hạn", "replay":"phát lại",
    "reply":"trả lời", "resell":"bán lại", "right":"đúng", "rollie":"đồng hồ Rolex", "rules":"luật lệ", "showbiz":"giới giải trí", "spread":"lan rộng",
    "stalk":"theo dõi", "stops":"dừng lại", "stress":"căng thẳng", "sunday":"chủ nhật", "tag":"gắn thẻ", "tee":"áo thun", "tequila":"rượu tequila",
    "text":"tin nhắn", "tone":"giọng điệu", "tore":"xé", "two":"hai", "voice":"giọng nói", "wan":"muốn", "wednesday":"thứ tư", "weed":"cần sa",
    "weird":"kỳ lạ", "whoa":"ồ", "win":"thắng", "wrapped":"được bọc", "yo":"này", "you":"bạn"
}

def is_english(word):
    """Kiểm tra nhanh xem từ này có cần tra từ điển không"""
    w = word.lower()
    # Bo qua nếu có dấu TV
    if re.search(r'[àáạảãâầấậẩẫăằắặẳẵèéẹẻẽêềếệểễìíịỉĩòóọỏõôồốộổỗơờớợởỡùúụủũưừứựửữỳýỵỷỹđ]', w): return False
    # Bo qua nếu không phải chữ cái
    if not re.match(r'^[a-zA-Z]+$', word): return False
    # Nếu la tu 1 ky tu (1 ký tự, trừ i, u, a)
    if len(w) == 1 and w not in ['i', 'u', 'a']: return False
    return True

def translate_line(text):
    # Tách cac tu
    words = re.split(r'(\W+)', text)
    new_words = []
    
    for word in words:
        if is_english(word):
            word_lower = word.lower()
            if word_lower in MUSIC_DICT:
                translated = MUSIC_DICT[word_lower] # Dich theo dictionary
                
                new_words.append(translated)
            else:
                new_words.append(word) # Không có trong từ điển
        else:
            new_words.append(word) # Không phải tiếng Anh
            
    return "".join(new_words)

with open(input_file, 'r', encoding='utf-8') as input, open(output_file, 'w', encoding='utf-8') as output:
    
    for line in input:
        line = line.strip()
        
        # Tách nhãn (Label) để không dịch nhầm vào nhãn
        parts = line.split(' ', 1)
        
        label = parts[0]
        content = parts[1]
        
        translated_content = translate_line(content)
        
        output.write(f"{label} {translated_content}\n")

print(f"Tranlated done: {output_file}")