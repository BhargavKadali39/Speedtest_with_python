
import speedtest

speed  = speedtest.Speedtest()

print("Download Speed is ", speed.download())

print("Upload Speed is ", speed.upload())
