#!/usr/bin/env python

import sys
import zlib
import pprint
import urllib.request, json
import math

#import PIL.Image
#import pyzbar.pyzbar
import base45
import cbor2

## Image as Argument
#data = pyzbar.pyzbar.decode(PIL.Image.open(sys.argv[1]))
#cert = data[0].data.decode()

## Probeweise einen vorbereiteten String nutzen
cert = "HC1:6BFMX1LUN5VOO137BC5T1MJO/12K9H3ENG%P*KE1QFFKRID8CPK NJ%C8:3WU K6AJGLMHG5 KGVIN-T2N$QXO3K4F*47NFR 8K7BATS3J.OX6OZKV3+1H/G*%RYRJICJRDU65G$EE%HT-N0Q*PS333176H7YOD :U.H56+6VCL5ZRT.8X8S*L7XUJO UV$I+KCZHA./J554CG3%N2C.U5PJ1$2$ID9$I:/VUTB/RIW:18JQ7CWIQ5G70CZN.QGLV8BU8WNK*1T.52HW5W368K7:PK0RL0ET9R3QICL7JA12H*VPF52ACRJNQPR5HIACIP%4S6BTA1TWPRGAS 9N20-ZLJ*AR94:50T68WG9J*A*%KKA2*419GCN3496IDRNRNSY5I14T4.5ZAV16IT0AM5DO HNWIC2F:SENJBEND00JO3PRQ1 2P01A949UTV7RKS2Q71QT-ANNU+3VFWS:PE+SRQ2ANVNB*UV3VQNV2/1.RBL4H:YQ62QMT5AF248IUUJGLMBDV28KC:7AOKC3"
#cert = "HC1:6BFOXN*TS0BI$ZD8UHILPSGHMM6ZJC109YRUNDC2LE $C$K9JMB20J.I5%MHV0MNO4*J8OX4W$C2VLWLI2P53O8J.V J8$XJK*LFP1$XBTZ7N P$R14WH-1VUUOMVB-Z5H%BN/V2-J*E03$HCG0+J4J*FE$B:PI:IG7Y47%S7Y48YIZ73423ZQT+EJEG32R4N%2%R0O05L%2A550AT56D7OF$W2AWCDZI+T4D-4HRVUMNMD3323R130$AC-4A+2XEN QT QTHC31M3+E3CP456L X4CZKHKB-43.E3KD3OAJ5%IKTCMD3QHBZQJLIFHJP7NVDEBU1JD*2X/G2RJUVI/E2$4JY/KWYC7:4X+S//CLXK7Y4 CTYXV$/IJZC+5L6AL**IKZ0BUF7KNARN/Y08ALD-I9YVK.GTEFUTNV7J$%25I3HC3X83767E09R5WIDN37F+XV-JMNV5E8N4A6DU7.KVR6MXTRFQ9.-2BIDZ9RHQ3EEC4AHR*T2/MGQQWD6KXLK$T9ATY8E .V9E20$6E.V2V93361QKQ$F"

b45data = cert.replace("HC1:", "")
zlibdata = base45.b45decode(b45data)
cbordata = zlib.decompress(zlibdata)
decoded = cbor2.loads(cbordata)
data = cbor2.loads(decoded.value[2])
data = data[-260][1]
#pprint.pprint(data)



baseUrl = "https://raw.githubusercontent.com/ehn-dcc-development/ehn-dcc-valuesets/main/"

medicalProducts= 'vaccine-medicinal-product.json'
countryCodes = 'country-2-codes.json'
manufacturers = 'vaccine-mah-manf.json'
testResults = 'test-result.json'
testTypes = 'test-type.json'
diseaseTarget = 'disease-agent-targeted.json'
typeUsed = 'vaccine-prophylaxis.json'

with urllib.request.urlopen(baseUrl + medicalProducts) as url:
    medicalProducts = json.loads(url.read().decode())

with urllib.request.urlopen(baseUrl + countryCodes) as url:
    countryCodes = json.loads(url.read().decode())

with urllib.request.urlopen(baseUrl + manufacturers) as url:
    manufacturers = json.loads(url.read().decode())

with urllib.request.urlopen(baseUrl + testResults) as url:
    testResults = json.loads(url.read().decode())

with urllib.request.urlopen(baseUrl + testTypes) as url:
    testTypes = json.loads(url.read().decode())

with urllib.request.urlopen(baseUrl + diseaseTarget) as url:
    diseaseTarget = json.loads(url.read().decode())

with urllib.request.urlopen(baseUrl + typeUsed) as url:
    typeUsed = json.loads(url.read().decode())


finalData = {
    "version": data['ver'],
    "sig": data['v'][0]['ci'],
    "forname": data['nam']['gnt'],
    "lastname": data['nam']['fnt'],
    "dob": data['dob'],
    "date": data['v'][0]['dt'],
    "country": countryCodes['valueSetValues'][data['v'][0]['co']]['display'],
    "tdos": data['v'][0]['dn'], # total doses 
    "ndos": data['v'][0]['sd'], # needed doeses
    "issuer": data['v'][0]['is'],
    "disease": diseaseTarget['valueSetValues'][data['v'][0]['tg']]['display'],
    "type": typeUsed['valueSetValues'][data['v'][0]['vp']]['display'],
    "product": medicalProducts['valueSetValues'][data['v'][0]['mp']]['display'],
    "manufacturer": manufacturers['valueSetValues'][data['v'][0]['ma']]['display']
}
pprint.pprint(finalData)


# check certifcate id
codePoints = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ/#:' # 39 char


def checksum(number, alphabet='0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ/#:'):
    """Calculate the Luhn checksum over the provided number. The checksum
    is returned as an int. Valid numbers should have a checksum of 0."""
    n = len(alphabet)
    number = tuple(alphabet.index(i)
                   for i in reversed(str(number)))
    return (sum(number[::2]) +
            sum(sum(divmod(i * 2, n))
                for i in number[1::2])) % n

def calc_check_digit(number, alphabet='0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ/#:'):
    """Calculate the extra digit that should be appended to the number to
    make it a valid number."""
    ck = checksum(str(number) + alphabet[0], alphabet)
    return alphabet[-ck]


def validateCheckCharacter(input):
    factor = 1
    sum = 0
    n = len(codePoints)
    count = len(input)-1

    for i in reversed(input):
        codePoint = codePoints.index(input[count])
        addend = factor * codePoint

        factor = 1 if factor == 2 else 2

        addend = (math.floor(addend / n)) + (addend % n)
        sum += addend
        
        if count > 0: count = count-1
        else: break

    remainder = sum % n
    checkCodePoint = (n - remainder) % n
    return codePoints[checkCodePoint]



checkNum = data['v'][0]['ci'].split("#")
checkedID = validateCheckCharacter(checkNum[0]+'')
print(checkedID)

if (checkedID == checkNum[1]):
    print("certificate ok")
else:
    print("certificate failed")