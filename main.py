import img2pdf
import os
import glob
import urllib.request

# https://img.yumpu.com/55158270/1/1070x769/192641wz.jpg?quality=100
# https://img.yumpu.com/55158270/86/400x400/192641wz.jpg?quality=100

def main():
    for i in range(1,86+1):
        download_file(i)
    v = [i for i in os.listdir('.') if i.endswith(".jpg")]
    v = sorted(v)
    with open("output.pdf", "wb") as f:
        f.write(img2pdf.convert(v))
    for f in glob.glob("*.jpg"):
        os.remove(f)

def download_file(i):
    download_url = "https://img.yumpu.com/55158270/"+str(i)+"/1000x1000/192641wz.jpg?quality=100"
    req = urllib.request.build_opener()
    req.addheaders = [('User-Agent',"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36")]
    response = req.open(download_url)
    file = open("page"+str(i).zfill(3)+".jpg", 'wb')
    file.write(response.read())
    file.close()
    print("Page "+str(i)+" Completed")

if __name__ == "__main__":
    main()
