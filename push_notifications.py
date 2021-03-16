from pushbullet import Pushbullet

pb = Pushbullet("API KEY HERE")
print(pb.devices)

phone= pb.get_device('Google Pixel 5')
push = phone.push_note("TestHeading", "Test Message")
