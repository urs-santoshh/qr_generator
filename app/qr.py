import qrcode
import json

def generate_qr(dataObj):
    try:
        dataJson = json.dumps(dataObj)
        img = qrcode.make(dataJson)
        # type(img)  # qrcode.image.pil.PilImage
        img.save("app/static/img/qr.png")
        return {"success":"QR code has been generated"}
    except Exception as e:
        return {"error":"QR code could not be generated "}
    