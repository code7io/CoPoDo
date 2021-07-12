#!/usr/bin/env python

import sys
import zlib
import pprint

#import PIL.Image
#import pyzbar.pyzbar
import base45
import cbor2

## Image as Argument
#data = pyzbar.pyzbar.decode(PIL.Image.open(sys.argv[1]))
#cert = data[0].data.decode()

## Probeweise einen vorbereiteten String nutzen
cert = "HC1:6BFMX1LUN5VOO137BC5T1MJO/12K9H3ENG%P*KE1QFFKRID8CPK NJ%C8:3WU K6AJGLMHG5 KGVIN-T2N$QXO3K4F*47NFR 8K7BATS3J.OX6OZKV3+1H/G*%RYRJICJRDU65G$EE%HT-N0Q*PS333176H7YOD :U.H56+6VCL5ZRT.8X8S*L7XUJO UV$I+KCZHA./J554CG3%N2C.U5PJ1$2$ID9$I:/VUTB/RIW:18JQ7CWIQ5G70CZN.QGLV8BU8WNK*1T.52HW5W368K7:PK0RL0ET9R3QICL7JA12H*VPF52ACRJNQPR5HIACIP%4S6BTA1TWPRGAS 9N20-ZLJ*AR94:50T68WG9J*A*%KKA2*419GCN3496IDRNRNSY5I14T4.5ZAV16IT0AM5DO HNWIC2F:SENJBEND00JO3PRQ1 2P01A949UTV7RKS2Q71QT-ANNU+3VFWS:PE+SRQ2ANVNB*UV3VQNV2/1.RBL4H:YQ62QMT5AF248IUUJGLMBDV28KC:7AOKC3"

b45data = cert.replace("HC1:", "")
zlibdata = base45.b45decode(b45data)
cbordata = zlib.decompress(zlibdata)
decoded = cbor2.loads(cbordata)
data = cbor2.loads(decoded.value[2])

# TODO: fetch valueset from ehc github repo and map them

pprint.pprint(data)