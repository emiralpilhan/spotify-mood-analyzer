import os
import webbrowser
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv

# 📌 Çevresel değişkenleri yükle (.env dosyasından)
load_dotenv()

# 📌 Spotify Kimlik Bilgileri (Kendi Spotify API bilgilerini gir)
CLIENT_ID = os.getenv("SPOTIPY_CLIENT_ID")  # Spotify Client ID
CLIENT_SECRET = os.getenv("SPOTIPY_CLIENT_SECRET")  # Spotify Client Secret
REDIRECT_URI = "http://127.0.0.1:8888/callback"  # Redirect URI (Spotify Dashboard'da eklediğinden emin ol!)

# 📌 Yetkilendirme için gerekli scope'lar
SCOPE = "user-read-private user-read-email user-top-read"

# 🌐 Spotify OAuth Yetkilendirmesi
sp_oauth = SpotifyOAuth(client_id=CLIENT_ID, client_secret=CLIENT_SECRET, redirect_uri=REDIRECT_URI, scope=SCOPE)

# 🌐 Kullanıcıyı Yetkilendirme Sayfasına Yönlendir
auth_url = sp_oauth.get_authorize_url()
print(f"🔗 Yetkilendirme için tarayıcıdan bu linke girin ve kodu alın: \n{auth_url}")
webbrowser.open(auth_url)

# 📌 Kullanıcıdan yetkilendirme kodunu al
auth_code = input("👉 Yetkilendirme kodunu buraya yapıştırın: ")

# 🔑 Yetkilendirme Kodunu Access Token'a Çevir
token_info = sp_oauth.get_access_token(auth_code)
access_token = token_info["access_token"]
refresh_token = token_info["refresh_token"]
print(f"✅ Access Token Alındı: {access_token}")

# 📌 Spotipy ile Spotify API'yi Kullanıma Aç
sp = spotipy.Spotify(auth_manager=sp_oauth)

# 🎵 Kullanıcı Bilgilerini Çek
user_info = sp.current_user()
print(f"🎤 Kullanıcı: {user_info['display_name']}, Email: {user_info['email']}, Ülke: {user_info['country']}")

# 🎶 Örnek Şarkının ID'si (Blinding Lights - The Weeknd)
track_id = "0VjIjW4GlUZAMYd2vXMi3b"

# 🎼 Şarkı Özelliklerini Çek
audio_features = sp.audio_features([track_id])[0]

if audio_features:
    print("\n🎵 Şarkı Özellikleri:")
    print(f"🎼 Dans Edilebilirlik: {audio_features['danceability']}")
    print(f"⚡ Enerji: {audio_features['energy']}")
    print(f"🔊 Ses Yüksekliği: {audio_features['loudness']} dB")
    print(f"🎶 Tempo: {audio_features['tempo']} BPM")
    print(f"😊 Mutluluk (Valence): {audio_features['valence']}")
else:
    print("⚠️ Şarkının analiz bilgileri bulunamadı!")

# ✅ Başarıyla tamamlandı
print("\n✅ Spotify API işlemi tamamlandı!")
