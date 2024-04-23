import qrcode
import json

def generate_qr(dataObj):
    try:
        dataJson = json.dumps(dataObj)
        img = qrcode.make(dataJson)
        # type(img)  # qrcode.image.pil.PilImage
        img.save("app/static/img/qr.png")
    except Exception:
        raise Exception
    