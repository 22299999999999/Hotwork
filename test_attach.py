import allure


def test_attach_text():
    allure.attach("这是一个纯文本", attachment_type=allure.attachment_type.TEXT)


def test_attach_html():
    allure.attach("<body>这是一个htmlbody块</body>", "html测试块", attachment_type=allure.attachment_type.HTML)


def test_attach_photo():
    allure.attach.file("D:/27.png", name="这是一个图片", attachment_type=allure.attachment_type.PNG)


def test_attach_video():
    allure.attach.file("C:/Users/15937/Desktop/音视频/1.mp4", "这是一个纯文本", attachment_type=allure.attachment_type.MP4)
