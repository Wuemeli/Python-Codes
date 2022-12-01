import speedtest

st = speedtest.speedtest()

print("Download speed: ", st.download())
print("Upload speed: ", st.upload())

