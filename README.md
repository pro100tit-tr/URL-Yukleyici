## URL-Yükleyici
---

Bağlantıları Yüklemek için Telegram Botu.

**Özellikleri**:

👉 [YTDL Desteklenen Bağlantıları](https://ytdl-org.github.io/youtube-dl/supportedsites.html) Telegram'a yükleyin.

👉 HTTP/HTTPS'yi Dosya/Video olarak Telegram'a yükleyin.

👉 ZippyShare, HxFile ve AnonFiles URL'lerini yükleyin

👉 Mesaj yayınla, yasakla, yasağı kaldır, toplam kullanıcıları kontrol et


#### Heroku'da çalıştırın

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

#### Railway'da çalıştırın

[![Deploy on Railway](https://railway.app/button.svg)](https://railway.app/new/template?template=https%3A%2F%2Fgithub.com%2FTurkce-Botlar-Sohbet%2FURL-Yukleyici&envs=WEBHOOK%2CTG_BOT_TOKEN%2CAPP_ID%2CAPI_HASH%2COWNER_ID%2CDATABASE_URL%2CSESSION_NAME%2CBANNED_USERS%2CUPDATE_CHANNEL%2CLOG_CHANNEL%2CDEF_THUMB_NAIL_VID_S%2CCHUNK_SIZE%2CHTTP_PROXY&optionalEnvs=UPDATE_CHANNEL%2CLOG_CHANNEL%2CDEF_THUMB_NAIL_VID_S%2CHTTP_PROXY&WEBHOOKDesc=Bunu+ANYTHING+ayarlamak%2C+env+modundayken+web+kancalar%C4%B1n%C4%B1+etkinle%C5%9Ftirir&TG_BOT_TOKENDesc=https%3A%2F%2Ft.me%2FBotFather+adresinden+bir+bot+olu%C5%9Fturarak+edinin.&APP_IDDesc=https%3A%2F%2Fmy.telegram.org%27da+bir+uygulama+olu%C5%9Fturarak+edinin.&API_HASHDesc=https%3A%2F%2Fmy.telegram.org%27da+bir+uygulama+olu%C5%9Fturarak+edinin.&OWNER_IDDesc=Telegram+ID+numaran%C4%B1z&DATABASE_URLDesc=MongoDB+URI%27niz&SESSION_NAMEDesc=Oturum+Ad%C4%B1n%C4%B1z%3A+%C3%96rnek%3A+urlyukleyici&BANNED_USERSDesc=Yasaklanan+%C4%B0stenmeyen+%C3%BCyeler.&UPDATE_CHANNELDesc=Zorla+abone+yapmak+i%C3%A7in+kanal%C4%B1n%C4%B1z%C4%B1n+kullan%C4%B1c%C4%B1+ad%C4%B1n%C4%B1+yaz%C4%B1n+%28%40+olmadan%29.&LOG_CHANNELDesc=G%C3%BCnl%C3%BCkler+i%C3%A7in+Kanal+ID+-+Telegram+ID+numaran%C4%B1z+olabilir.&DEF_THUMB_NAIL_VID_SDesc=Videolarda+kullan%C4%B1lacak+varsay%C4%B1lan+k%C3%BC%C3%A7%C3%BCk+foto%C4%9Fraf.&CHUNK_SIZEDesc=%C4%B0steklerde+kullan%C4%B1lmas%C4%B1+gereken+y%C4%B1%C4%9F%C4%B1n+boyutu&HTTP_PROXYDesc=K%C4%B1s%C4%B1tl%C4%B1+Alanlarda+youtube-dl%27ye+eri%C5%9Fmek+i%C3%A7in+proxy.+https%3A%2F%2Fgithub.com%2Frg3%2Fyoutube-dl%2Fissues%2F1091%23issuecomment-230163061+adresinden+kendi+proxy%27nizi+al%C4%B1n&WEBHOOKDefault=ANYTHING&CHUNK_SIZEDefault=128&referralCode=BOTSOHBET)


#### VPS'nizde çalıştırın

```sh
git clone https://github.com/Turkce-Botlar-Sohbet/URL-Yukleyici
cd URL-Yukleyici
pip3 install -r requirements.txt
# <config.py'yi uygun şekilde yapılandırın>
python3 bot.py

```
## Komutlar
Komut                   | Açıklama
----------------------- | ----------------------------------------    
`/broadcast`            | Kullanıcılara toplu olarak mesaj gönderme.
`/help`                 | Yardım komutu.     
`/genthumb`             | Thumbnail eklemek için bir fotoğrafa yanıtlayın.
`/delthumb`             | Thumbnail silmek için.
`/total`                | Veritabanında kayıtlı toplam kullanıcı sayısını verir.
`/ban`                  | Kullanıcıyı bottan yasaklamak için.
`/unban`                | Kullanıcının yasağını kaldırmak için.
`/banned_users`         | Yasaklı kullanıcı sayısını verir.

## Kredi ve Teşekkürler

* [X-URL-Uploader](https://github.com/X-Gorn/X-URL-Uploader/tree/database) için [@X-Gorn](https://t.me/xgorn)
* [TG-URL-Uploader](https://github.com/TGExplore/TG-URL-Uploader) için [@TGExplore](https://t.me/ViruZs)
* [AnyDLBot](https://telegram.dog/AnyDLBot) için [@SpEcHlDe](https://t.me/ThankTelegram)
* [Pyrogram Library](https://github.com/pyrogram/pyrogram) için [Dan Tès](https://t.me/haskell)
* [UploaditBot](https://telegram.dog/UploaditBot) için [Yoily](https://t.me/YoilyL)
* [database.py](https://github.com/AbirHasan2005/VideoCompress/blob/main/bot/database/database.py) için [@AbirHasan2005](https://t.me/AbirHasan2005)

#### LİSANS
- GPLv3
