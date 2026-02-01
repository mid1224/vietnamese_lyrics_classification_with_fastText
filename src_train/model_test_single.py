import fasttext
import re

model = fasttext.load_model("trained_models/model_1.bin")

text_to_predict = "Ngắm em qua phone Anh chỉ ước được bên em ngay Để ta cùng nắm tay Đi dạo dưới biển Ánh mắt ấy tươi cười Cùng những điều em mê say Khiến anh như chết lặng vài giây Anh vẫn ngồi đây cầm guitar đàn Gửi cho em những thanh âm rộn ràng Qua mạng không dây nhưng sao hôm nay Đường truyền hơi chập chờn thế này Ah ah ah ah Ah ah ah ah Ah ah ah ah Wanna say Điều mơ ước giờ này Là mình được ở bên nhau Đôi môi sẽ cùng hàn gắn Hai tâm hồn Đừng lo lắng vì chập chờn Chập chờn thì không lâu Sẽ không lâu đâu babe Ah ah ah ah Ah ah ah ah ah Ah ah ah ah Ah ah ah ah ah ah ah Đi đâu mà vội vàng Ta cần có một chút nghỉ ngơi yeah You know, chẳng có một cách nào Khác ngoài hai chữ chờ đợi Chập chờn một chút không sao đâu babe Đôi khi làm đong đầy thêm Mà như mình nêm gia vị Vì anh luôn biết anh cũng ra gì Luôn mang tình yêu cộng thêm độ feel Điều mơ ước giờ này Là mình được ở bên nhau Đôi môi sẽ cùng hàn gắn Hai tâm hồn Đừng lo lắng vì chập chờn Chập chờn thì không lâu Sẽ không lâu đâu babe Điều mơ ước giờ này Là mình được ở bên nhau Đôi môi sẽ cùng hàn gắn Hai tâm hồn Đừng lo lắng vì chập chờn Chập chờn thì không lâu Sẽ không lâu đâu babe yeah yeah Ah ah ah ah Ah ah ah ah ah Ah ah ah ah Ah ah ah ah ah ah ah Hi world, I just wanna say I’m Dương Domic And thank you everybody For listening to my music Enjoy it Điều mơ ước giờ này Là mình được ở bên nhau Đôi môi sẽ cùng hàn gắn Hai tâm hồn Đừng lo lắng vì chập chờn Chập chờn thì không lâu Sẽ không lâu đâu babe Điều mơ ước giờ này Là mình được ở bên nhau Đôi môi sẽ cùng hàn gắn Hai tâm hồn Đừng lo lắng vì chập chờn Chập chờn thì không lâu Sẽ không lâu đâu babe Ah ah ah ah Ah ah ah ah ah Ah ah yeah yeah yeah yeah"

def preprocess_vietnamese_lyrics(text: str) -> str:
    # Lowercase
    text = text.lower()
    # Remove special characters
    text = re.sub(r"[^a-zA-Z0-9\s]", "", text)
    # Remove digits
    text = re.sub(r"\d+", "", text)
    # Remove extra spaces
    text = re.sub(r"\s+", " ", text).strip()
    return text

processed_text = preprocess_vietnamese_lyrics(text_to_predict)

prediction = model.predict(processed_text, k=-1, threshold=0.05)

print(f"Prediction for '{processed_text}':")
print(prediction) 