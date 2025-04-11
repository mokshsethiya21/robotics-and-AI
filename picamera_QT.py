from picamera2 import Picamera2, Preview
import time
from libcamera import Transform

picam2 = Picamera2()
camera_config = picam2.create_preview_configuration({"size":(320,240)},transform=Transform(vflip=True),controls={"ExposureValue":0.6,"Contrast":1.3,"Sharpness":3,"ColourTemperature":3600,"NoiseReductionMode":"HighQuality"})
picam2.configure(camera_config)
picam2.start_preview(Preview.QTGL)
picam2.start()
time.sleep(2)
#picam2.capture_file("test5.jpg")
