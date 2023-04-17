import pychromecast
import time

chromecasts, browser = pychromecast.get_listed_chromecasts(friendly_names=["Gabriel TV"])
  
try:
    cast = chromecasts[0]
    cast.wait()
    mc = cast.media_controller
    mc.play_media('https://img.ibxk.com.br/materias/5866/21577.jpg', 'image/jpeg')
    mc.block_until_active()
    mc.play()
    time.sleep(20)
    mc.stop()
except Exception as e:
    print(repr(e))
