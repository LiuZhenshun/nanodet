import cv2
import json
import os
import argparse

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--JsonPath", help="Json's path")
    parser.add_argument("--ResultPath", help="The path of Detection's result")
    args = parser.parse_args()
    return args
args = parse_args()

bytesJson = open(args.JsonPath, "r")
DictJson = json.load(bytesJson)

for index,ImgInformation in enumerate(DictJson):
    ImgPath = ImgInformation["image_path"]
    Bbox = ImgInformation["bbox"]

    imag_brg = cv2.imread(ImgPath)
    image_rgb = cv2.cvtColor(imag_brg, cv2.COLOR_BGR2RGB)
    image = image_rgb.copy()

    cv2.rectangle(image, (Bbox[0],Bbox[1]), (Bbox[2],Bbox[3]), color=(0, 0, 255), thickness=2)

    os.makedirs(args.ResultPath, exist_ok = True)
    imagPath = os.path.join(args.ResultPath, (str(index) + ".png") )
    cv2.imwrite(imagPath, image)
