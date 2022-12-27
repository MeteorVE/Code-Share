import os 
import requests

def image_download(img_url, filename='example.png'):
    """
    ### Download image to specific folder.
    """
    isExist = os.path.exists(filename)
    if isExist == True:
        print("[Info] file exist, pass !")
        return
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, 'wb') as f:
        try:
            im = requests.get(img_url)
            f.write(im.content)
            print("[Info] Download ", filename, "\n\tfrom", img_url)
        except requests.exceptions.ConnectionError as e:
            print("[Error] ConnectionError.", "\n\tError Detail:", e)
        except requests.exceptions.RequestException as e:
            print("[Error] RequestException.", "\n\tURL (image):", img_url,"\n\tError Detail:", e)
            # raise SystemExit(e)
    return 