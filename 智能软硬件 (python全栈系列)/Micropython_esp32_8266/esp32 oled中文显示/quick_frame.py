import framebuf
##############################################
##创建oled对象
#############
buffer = bytearray (16*64)
fb1 = framebuf.FrameBuffer(buffer,128,64, framebuf.MVLSB)
##
fb1.fill(0)
fb1.hline(0,0,100,1)
oled.write_data(buffer)

fb1.scroll(10,10)
##
fb1.text('MicroPython!', 0, 0, 1) #1为颜色
oled.write_data(buffer)

#####################################################




import machine,myssd
import struct
i2c=machine.I2C(scl=machine.Pin(2),sda=machine.Pin(0))
#i2c.scan()

oled=myssd.SSD1306_I2C(128,64,i2c)
#oled.buffer
oled.framebuf.text("abc",0,0)
oled.show()
################################################################
oled.fill(0)

oled.buffer[6]=0x0f
oled.show()


##加载图片
f=open('bili.TXT','r')
data = f.read() #str
data = data.split("{")[1:-1]
for ii in range(len(data)):
    data[ii] = data[ii].split("}")[0]

width = 128
start_page = 1 
start_x = 40

temp_index = start_page*width+start_x
for ii in range(len(data)):
    temp = data[ii].split(",")
    temp_b = b''
    for jj in range(len(temp)):
        #temp[jj]='0x00'
        temp_data = (int)(temp[jj],16)
        temp_b += struct.pack("B",temp_data)
    #赋值
    oled.buffer[temp_index:(temp_index+len(temp))] = temp_b
    temp_index += width
oled.show()


#滚动
oled.hw_scroll_h()
oled.hw_scroll_off()