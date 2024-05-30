import requests

def fetch(url, params):
  headers = params["headers"]
  body = params["body"]
  match params["method"]:
    case "GET":
      return requests.get(url, headers=headers)
    case "POST":
      return requests.post(url, headers=headers, data=body)

hyundai = fetch("https://auto.ru/-/ajax/desktop-search/listing/", {
  "headers": {
    "accept": "*/*",
    "accept-language": "be-BY,be;q=0.9,en-US;q=0.8,en;q=0.7,uk;q=0.6,pl;q=0.5,ru;q=0.4",
    "content-type": "application/json",
    "priority": "u=1, i",
    "sec-ch-ua": "\"Google Chrome\";v=\"125\", \"Chromium\";v=\"125\", \"Not.A/Brand\";v=\"24\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "same-origin",
    "sec-fetch-site": "same-origin",
    "x-client-app-version": "100.0.14091663",
    "x-client-date": "1717079328666",
    "x-csrf-token": "878b8d999a5c99636b65375e52d438d40651953aadf68beb",
    "x-page-request-id": "3bbda4964f073756507eee9d988994e4",
    "x-requested-with": "XMLHttpRequest",
    "x-retpath-y": "https://auto.ru/cars/hyundai/all/",
    "x-yafp": "{\"a1\":\"FfrkisjTsm3RYA==;0\",\"a2\":\"FegbGCU8acMoLpr2WePvRzojfSOlog==;1\",\"a3\":\"xDVkAM7K67uoA/WzoarH4w==;2\",\"a4\":\"sa6/jZJ0aojqGk4r0gXGT+UgNd3EJYD7x1jd5pP6J4gFw5p8QOnrTEZjD6aiOL4KzLvJYA==;3\",\"a5\":\"AxYrGdQtjc4SFQ==;4\",\"a6\":\"V5s=;5\",\"a7\":\"1dRe/7wfplk4bQ==;6\",\"a8\":\"eJdFcvCGn2k=;7\",\"a9\":\"3MfuhCVP1+JUtQ==;8\",\"b1\":\"uAS5XKHFC34=;9\",\"b2\":\"VtD/gMQwdXf5jQ==;10\",\"b3\":\"1rYgfocdqYNlZA==;11\",\"b4\":\"DEkyjR0Mp6I=;12\",\"b5\":\"jadM5bHH5B44CQ==;13\",\"b6\":\"NzmIr9EB34RWEQ==;14\",\"b7\":\"cAaPBX8Ea3/n/Q==;15\",\"b8\":\"kG9+W9aO3Iz9Ag==;16\",\"b9\":\"J6z2JN8r9VQA+Q==;17\",\"c1\":\"P6GBwA==;18\",\"c2\":\"LqC5O00D+7kSQZkQ/uQQOg==;19\",\"c3\":\"q47cw6+Oj68bDznXQduSPQ==;20\",\"c4\":\"o9adC80Obtg=;21\",\"c5\":\"GXYMkX3cTL0=;22\",\"c6\":\"QbYGMw==;23\",\"c7\":\"baXIX6OXLU4=;24\",\"c8\":\"Tyg=;25\",\"c9\":\"Sml8Ki244sY=;26\",\"d1\":\"6Lbeok7NIps=;27\",\"d2\":\"+4w=;28\",\"d3\":\"SdLspV8EfMTKiA==;29\",\"d4\":\"NUkHeuzgUuk=;30\",\"d5\":\"/aZE57c+Pd4W3w==;31\",\"d7\":\"IvFb1BPKZ0g=;32\",\"d8\":\"/F5uIwGl6WiClCQ1ddyGEc8V+Y6sQoBs17U=;33\",\"d9\":\"8X2wFMmzWNk=;34\",\"e1\":\"kyDUXfhXJbve8g==;35\",\"e2\":\"z59MZbPOtNQ=;36\",\"e3\":\"jgynYhIoFdE=;37\",\"e4\":\"YIHjc3S5nDU=;38\",\"e5\":\"ru5cuyqlmpCF2A==;39\",\"e6\":\"VmfaiqtmarU=;40\",\"e7\":\"fCUJBSVWOf1Jfg==;41\",\"e8\":\"L4Xgvoa3Wjs=;42\",\"e9\":\"SoD5wbK4Pyo=;43\",\"f1\":\"v4y34gSAY3UNVg==;44\",\"f2\":\"Xa/fcLjDaIM=;45\",\"f3\":\"BQfMBwjxXwWJTA==;46\",\"f4\":\"TgBO9bnA9eM=;47\",\"f5\":\"/5b8/SqloHfChg==;48\",\"f6\":\"XRuucEkRgCgxJg==;49\",\"f7\":\"GEw0iUTSLZkZqQ==;50\",\"f8\":\"GiX7/wCrg3grGg==;51\",\"f9\":\"+Z7aLgI7hdk=;52\",\"g1\":\"4x2qfMF9ascJCw==;53\",\"g2\":\"ZIgdIAzhTH8GhQ==;54\",\"g3\":\"tu+ckKWR44I=;55\",\"g4\":\"txq259Dxd1luCg==;56\",\"g5\":\"cTBTCOTGqYQ=;57\",\"g6\":\"P+/0l/fgjGw=;58\",\"g7\":\"ZlXk99uesM0=;59\",\"g8\":\"8tfgPqAB0CU=;60\",\"g9\":\"rh2ziV08HN8=;61\",\"h1\":\"4RDpljoj+yq64A==;62\",\"h2\":\"DLl9WUToK4G73g==;63\",\"h3\":\"xTiq+PuvADoI9w==;64\",\"h4\":\"FP46uGIt9hDr2A==;65\",\"h5\":\"IXkqyB9Vbng=;66\",\"h6\":\"KtfeF0vx8wzYCw==;67\",\"h7\":\"lTccHqG6MhfW0xlYiOSIKNjRTQZxe3g30INveTbDoHkBVINW;68\",\"h8\":\"bqfJhXcGQ5f1/w==;69\",\"h9\":\"M4vsTEhlqg1V6w==;70\",\"i1\":\"99q2KcXsZkU=;71\",\"i2\":\"u+piaKeKm5+ngw==;72\",\"i3\":\"kKb/F7VaPe03nw==;73\",\"i4\":\"PwZRApFzPDQfvg==;74\",\"i5\":\"JQvll53GS61wVA==;75\",\"z1\":\"v5z0iII8GSSJEayi32kAhPc1qTHceQa2eH9V7N+hqbYJJOYLUskKLq5z6gRb1tKVt0bCd+3LYpt7rBIx7XcZaQ==;76\",\"z2\":\"23Ir5vzCdjNhMl7aP/DYDcIW7iiKGlDIii/3qk0B9ZkK/qHvHWBOW6URVopfADEzvwOI2ZfuZUW6P/ZDcIng3A==;77\",\"y2\":\"crvp6GtfiVJYQw==;78\",\"y3\":\"0cpBsQWWu1PrLQ==;79\",\"y6\":\"GfchG9iIkAIWBA==;80\",\"y8\":\"Sn79p6vLOAesPQ==;81\",\"x4\":\"HqIrLt6cn/731A==;82\",\"z4\":\"wlegWf7nDQ6ipw==;83\",\"z5\":\"tmpVmmGpFXE=;84\",\"z6\":\"Dyc6IHgjXelc1S8g;85\",\"z7\":\"Uj/LvLHD5CfQuQSt;86\",\"z8\":\"fpTYnkKwj9ibjJQy;87\",\"z9\":\"2OW0487PBbBwdDog;88\",\"y1\":\"5hVEo4+u6jXJ9gZL;89\",\"y4\":\"6RIFzCR22mW2RASD;90\",\"y5\":\"4MkOnf6QS5YreSasRM8=;91\",\"y7\":\"P8c/AXV3y5KKNJ2t;92\",\"y9\":\"aVOuodvIEMQPfjyD/9M=;93\",\"y10\":\"1weFQmXHeX6NB7zk0jk=;94\",\"x1\":\"VaKN1YAePKNt+3ZB;95\",\"x2\":\"Hq1FS2/aKcp0YjQhpAw=;96\",\"x3\":\"atU/uavUQcrfz3xw;97\",\"x5\":\"uwqPCkqUYyzsmxMp;98\",\"z3\":\"3XbMBpnc/xtDKfFxkugcC/HRd5Zb/Ne+lYcPBJ6/CV4=;99\",\"v\":\"6.3.1\",\"pgrdt\":\"eM/T2JlwoC2ZdkQTdpNVfIMvvhI=;100\",\"pgrd\":\"kSxGnyBsHG9bkWIfIcfCjaFaetduj1bp5als+1mmT0FJVuhPJz04XR5tV+jZ7GeRAppVv7TP4m0ZLB+bTxJn4s62aaWQPwEU/MC/PBEP2u6pZjujqyxWOFWhdTpTuIun56EBZ9o3tyO12wQAqd1kRHUlMhBYrTPSdxTJiUN0XWYxuhJFOqdZvRHmanxuIg0fMXXvC9zCU1RRuRIeQBBNTB0PKSk=\"}",
    "cookie": "autoru_gdpr=1; suid=c6ebe0594fa0e1bf9399ff0f34685a2a.103bb6299f02a96c006c8c7ba8982409; yandex_login=; yandexuid=633120651653736360; my=YwA=; _csrf_token=878b8d999a5c99636b65375e52d438d40651953aadf68beb; autoru_sid=a%3Ag66588acd2gu9d3jk79m21rove948rer.6b9f86abb8ef0e9478e7355ed02f8d63%7C1717078733647.604800.dAJV0PGFc_JFqJWh2KR4-w.kONimM--bNPkxQ5vEPJ_0jkzlJLoNfeDRtbGT-f_nqc; autoruuid=g66588acd2gu9d3jk79m21rove948rer.6b9f86abb8ef0e9478e7355ed02f8d63; from=direct; autoru_sso_blocked=1; Session_id=noauth:1717078733; sessar=1.1190.CiCPg1EE3G_OxnHgLeEHwihQG7utzcPiq-zThJ_Bf-MVMA.vBW69NN-Go-CKOSA5ZVmrYw8RyxtzCfJYu5Pqntf0a8; ys=c_chck.3069220565; i=/huFxO6pPsBcxbpjKBlndzSYxSDs/PqMUPk/EAuQ6hOAwwdG6YwhaVEEZjrSjUfQ1Fl5PzVBZhCAgA60IrbdyA6/qQ4=; mda2_beacon=1717078733989; sso_status=sso.passport.yandex.ru:synchronized; crookie=iXzRhDzx9xyDqQ+h3p+EUoDKVVYvmSujOUp2QaIqrepmCHZ/RzIY+yVYqbqNoHCyR+VTae2rhXP/HA88r1fohtr2yTE=; cmtchd=MTcxNzA3ODczNjg4NQ==; _ym_uid=1703076285936444921; yaPassportTryAutologin=1; popups-dr-shown-count=1; _ym_isad=1; los=1; bltsr=1; coockoos=4; _yasc=vqBNNpv9UNNrbmn8wjL9s5znwT1J6vj/5qyIuWQ76MYs0FlkwRBNoPWpcLYYUQkibWk=; _ym_d=1717079233; count-visits=4; from_lifetime=1717079258661; layout-config={\"screen_height\":864,\"screen_width\":1536,\"win_width\":919.2000122070312,\"win_height\":686.4000244140625}",
    "Referer": "https://auto.ru/cars/hyundai/all/",
    "Referrer-Policy": "no-referrer-when-downgrade"
  },
  "body": "{\"catalog_filter\":[{\"mark\":\"HYUNDAI\"}],\"section\":\"all\",\"category\":\"cars\",\"output_type\":\"list\",\"geo_id\":[]}",
  "method": "POST"
})

print(hyundai.status_code)
print(hyundai.json().keys())
cars = hyundai.json()["offers"]  # Список машин
for car in cars:
  mark = car["vehicle_info"]["mark_info"]
  model = car["vehicle_info"]["model_info"]
  tech = car["vehicle_info"]["tech_param"]
  print(f'{mark["name"]} {model["name"]} за {car["price_info"]["USD"]} дол. / {tech["human_name"]}')
