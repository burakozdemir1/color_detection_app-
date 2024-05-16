import sensor,image

sensor.reset()

sensor.get_pixformat(sensor.RGB565)

sensor.set_framesize(sensor.QVGA)

sensor.skip_frames(time = 2000)

thresholds = (58,33,-17,2,-27-109)

while True:

    img = sensor.snapshot()

    blobs = img.find_blobs( [thresholds] , area_threshold = 1000, merge = True)

    for blob in blobs:
        img.draw_rectangle(blob.rect() , color = (0,255,0))
        img.draw_cross(blob.cx , blob.cy ,color = (255,0,0))


