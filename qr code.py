# Hi, I'm code kudos.
## Convert any text or Web URL into a QR Code with just 4 lines of code using python
### Hope you like it!!!!
#### To see more like this Subscribe to 
##### Youtube: @codekudos
###### Instagram: @codekudos
####### Twitter: @code_kudos
import qrcode

data = 'https://www.youtube.com/channel/UC8ezO2ac6VnRrzj6T-8YdLw'

img = qrcode.make(data)
img.save('MyQRCode.png')