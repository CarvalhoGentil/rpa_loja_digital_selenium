HEADER_GRAPH_LOGIN = {
    'authority': 'api-loja-digital.prd.grupoboticario.digital',
    'method': 'POST',
    'path': '/auth/api/v1/auth/login',
    'scheme': 'https',
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate, br, zstd',
    'Accept-Language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7',
    'Authorization': 'undefined',
    'Content-Length': '1087',
    'Content-Type': 'application/json',
    'Origin': 'https://lojadigital.boticario.com.br',
    'Priority': 'u=1, i',
    'Referer': 'https://lojadigital.boticario.com.br/',
    'Sec-Ch-Ua': '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
    'Sec-Ch-Ua-Mobile': '?0',
    'Sec-Ch-Ua-Platform': '"Windows"',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'cross-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
    'X-Api-Un': 'BOT'
}

HEADER_FIRESTORE_REQUEST = {
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate, br, zstd',
    'Accept-Language': 'pt-BR,pt;q=0.8,en-US;q=0.5,en;q=0.3',
    'Alt-Used': 'firestore.googleapis.com',
    'Connection': 'keep-alive',
    'Content-Length': '1152',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Host': 'firestore.googleapis.com',
    'Origin': 'https://lojadigital.boticario.com.br',
    'Priority': 'u=1',
    'Referer': 'https://lojadigital.boticario.com.br/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'cross-site',
    'TE': 'trailers',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:126.0) Gecko/20100101 Firefox/126.0'
}
QUERY_PARMS = '?rememberMe=false&csrf_token={csrf}&tx={transId}&p=B2C_1A_JIT_SignUpOrSignin_PRD&diags=%7B%22pageViewId%22%3A%22925fdb4e-a37f-4388-baeb-2ad415a6315b%22%2C%22pageId%22%3A%22CombinedSigninAndSignup%22%2C%22trace%22%3A%5B%7B%22ac%22%3A%22T005%22%2C%22acST%22%3A1715345553%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T021%20-%20URL%3Ahttps%3A%2F%2Fidentityb2cextranet.grupoboticario.digital%2Flogin.html%22%2C%22acST%22%3A1715345553%2C%22acD%22%3A20%7D%2C%7B%22ac%22%3A%22T019%22%2C%22acST%22%3A1715345553%2C%22acD%22%3A3%7D%2C%7B%22ac%22%3A%22T004%22%2C%22acST%22%3A1715345553%2C%22acD%22%3A3%7D%2C%7B%22ac%22%3A%22T003%22%2C%22acST%22%3A1715345553%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1715345553%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T030Online%22%2C%22acST%22%3A1715345553%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T002%22%2C%22acST%22%3A1715351682%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T018T010%22%2C%22acST%22%3A1715351680%2C%22acD%22%3A1954%7D%5D%7D'

URL_CONFIRM = 'https://login.extranet.grupoboticario.com.br/1e6392bd-5377-48f0-9a8e-467f5b381b18/B2C_1A_JIT_SignUpOrSignin_PRD/api/CombinedSigninAndSignup/confirmed'

PAYLOAD_GRPH = {"query":"\n    query getUserTeams($id: String) {\n    data : getUserTeams(id: $id) {\n    count\n    items {\n      active\n      cpCode\n      cpName\n      stores {\n        storeId\n        storeName\n      }\n      teamId\n      teamName\n    }\n  }\n}\n    ","variables":{"id":"EbSjvaQRi1qptn1"}}

URL_LOJA_DIGITAL= 'https://login.extranet.grupoboticario.com.br/{authorization_code}?response_type=id_token&client_id={client_id}&redirect_uri=https%3A%2F%2Flojadigital.boticario.com.br%2Flogin%2Foauth2callback&prompt=login&scope=openid&p=B2C_1A_JIT_SIGNUPORSIGNIN_PRD'

HEADERS_LOJA_DIGITAL_REDIRECT = {
    'authority': 'login.extranet.grupoboticario.com.br',
    'scheme': 'https',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Origin': 'https://gboticariob2c.b2clogin.com',
    'Accept-Encoding': 'gzip, deflate, br, zstd',
    'Accept-Language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7',
    'Referer':'https://lojadigital.boticario.com.br/',
    'Sec-Ch-Ua':'"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"'
}

URL_LOGIN_LOJA_DIGITAL = 'https://login.extranet.grupoboticario.com.br{tenantId}/SelfAsserted?tx={transId}&p=B2C_1A_JIT_SignUpOrSignin_PRD'

URL_REFEREER = 'https://login.extranet.grupoboticario.com.br/{authorization_code}?response_type=id_token&client_id={client_id}&redirect_uri=https%3A%2F%2Flojadigital.boticario.com.br%2Flogin%2Foauth2callback&prompt=login&scope=openid&p=B2C_1A_JIT_SIGNUPORSIGNIN_PRD'

HEADERS_LOGIN = {
    'authority': 'login.extranet.grupoboticario.com.br',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Encoding': 'gzip, deflate, br, zstd',
    'Accept-Language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Origin': 'https://login.extranet.grupoboticario.com.br',
    'Priority':'u=0, i',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest'
}
PAYLOAD_LOGIN = {
    'request_type':'RESPONSE',
    'signInName':'glauber',
    'password':'123456'
}
HEADER_GHRP = {
    'authority': 'xh3ienjk3bgjzf7tpzenfxtqvi.appsync-api.us-east-1.amazonaws.com',
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate, br, zstd',
    'Accept-Language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7',
    # 'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJkYXRhIjp7InRva2VuQUQiOiJleUpoYkdjaU9pSlNVekkxTmlJc0ltdHBaQ0k2SW5WNllrSk1hblphYlRKeFZEUnNTRVJCWlhkQlgzRXdkMlpzY1RRdFZHSm5abWhWVXpCQlVFNUhWelFpTENKMGVYQWlPaUpLVjFRaWZRLmV5SjJaWElpT2lJeExqQWlMQ0pwYzNNaU9pSm9kSFJ3Y3pvdkwyeHZaMmx1TG1WNGRISmhibVYwTG1keWRYQnZZbTkwYVdOaGNtbHZMbU52YlM1aWNpOHhaVFl6T1RKaVpDMDFNemMzTFRRNFpqQXRPV0U0WlMwME5qZG1OV0l6T0RGaU1UZ3Zkakl1TUM4aUxDSnpkV0lpT2lKbVpHTmpNVFEzTnkwMk1qSXhMVFJtTkRZdFlXWTBaUzFtWm1SaU5tUXlOelV3TldFaUxDSmhkV1FpT2lJMVl6QmpaV05oWVMweU56ZGpMVFEyWkdNdFlqSXpPQzAxT1dKak1XRTBOakU1TURjaUxDSmxlSEFpT2pFM01UVXpOakkzTlRZc0ltRmpjaUk2SW1JeVkxOHhZVjlxYVhSZmMybG5iblZ3YjNKemFXZHVhVzVmY0hKa0lpd2lhV0YwSWpveE56RTFNelU1TVRVMkxDSmhkWFJvWDNScGJXVWlPakUzTVRVek5Ua3hOVFlzSW1WdFlXbHNJam9pWjJ4aGRXSmxja0JsTFdKdmRHbGpZWEpwYnk1amIyMHVZbklpTENKdVlXMWxJam9pUjB4QlZVSkZVaUJIUlU1VVNVd2dRa1ZhUlZKU1FTQkVSU0JUVDFWYVFTSXNJbWRwZG1WdVgyNWhiV1VpT2lKSFRFRlZRa1ZTSWl3aVptRnRhV3g1WDI1aGJXVWlPaUpUVDFWYVFTSXNJbVY0ZEdWdWMybHZibDlEVUVZaU9pSXdNRGMzTnpFME1UUTROU0lzSW01aVppSTZNVGN4TlRNMU9URTFObjAuYk9yZnZ1ODIwOGFEcFV2aXloUVQyamJ1ZDJDSm11LS1fd0F3aC1PVmRZQVhvbm5ka21IRUVJQ3BPZnFQUVhCN2MxZ1VUTUluRk81alk4bThUQ2NXMW1DanRRYkNrUkZNNjFrTDBQb0pHZmJRcG9waVRFNWFPaUw3TGM0eE9kc0poMWN2a01tTjZlVDBxaVg3enUxNGh5bEhfenJfemhmRy05RG5lN1Y3UzFHY0lHbUlUcGNxWlQtSXp4QW5fTlJKelgyUVp0NjRVNDdzcERBWTZCQzV4cjAyQ1ZLWTl6VVRneExaSDNmVWgyTkdWb0lYYXJLMnRmVmo2Wl84aFRwTUhJN19QdGY1emE1UFoxdDl2eWR6cHFMQ2VGZTdZemtGUi1hQXNGc0ZiRkZ6ZHpJOWhiRXQtbkhHUDVjT2IxUXVRTDhmZTk3SVBKQVpyd1AyNmxaWklBIiwiY3BmIjoiMDA3NzcxNDE0ODUiLCJzdG9yZUlkcyI6Wzc0MjMsNzQyNCw3NDI1LDc0MjYsNzQyNyw3NDMwLDc0MzEsNzQzMiw3OTU3LDExNTgyLDExNTkxLDExNzc5LDExOTgzLDExOTkyLDEyMTc1LDEyNDg4LDEyNTE3LDEyNjQzLDEyNjQ3LDEzMjE0LDE0MDQ1LDE0MzI5LDE5NTk1LDE5NTk4LDE5NTk5LDE5NjAwLDE5NjAxLDE5NjAyLDE5NjAzLDIwMTU2LDIwNzYzLDIwODM2LDIwODU2LDIwOTIyLDIwOTIzLDIwOTI0LDIwOTI1LDIwOTMxLDIwOTMyLDIwOTMzLDIwOTM0LDIxMDI2LDIxMTIyLDIxMTIzLDIxMTI4LDIxMTI1LDIxMjMyLDIxMjcwLDIxMzE2LDIxMzYzLDIxMzY0LDIxMzY1LDIxMzc2LDIxNDExLDIxNDEyLDIxNDEzLDIxNDE0LDIxNDE1LDIxNDE2LDIxNDE3LDIxNDE4LDIxNDE5LDIxNDIwLDIxNDIxLDIxNDIyLDIxNDIzLDIxNDI0LDIxNDI1LDIxNDI2LDIxNDI3LDIxNDI4LDIxNDI5LDIxNDMwLDIxNDMxLDIxNDMyLDIxNTU5LDIxNTYwLDIxNTYxLDIxNzUwLDIxNzYxLDIxNzYyLDIxNzYzLDIxNzY0LDIxNzY1LDIxNzY2LDIyMDU0XSwicm9sZSI6Im1hbmFnZXIifSwiaWF0IjoxNzE1MzU5MTYzLCJleHAiOjE3MTUzODc5NjN9.C4eNrX5s8GA8Ao3HFq8cYVseb4Tf8F9rxvO2uU-au_o',
    'Content-Type': 'text/plain;charset=UTF-8',
    'path': '/graphql',
    'Origin': 'https://lojadigital.boticario.com.br',
    'Priority': 'u=1, i',
    'Referer': 'https://lojadigital.boticario.com.br/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
}

HEADER_FIRESTORE_SID = {
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate, br, zstd',
    'Accept-Language': 'pt-BR,pt;q=0.8,en-US;q=0.5,en;q=0.3',
    'Alt-Used': 'firestore.googleapis.com',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Host': 'firestore.googleapis.com',
    'Origin': 'https://lojadigital.boticario.com.br',
    'Referer': 'https://lojadigital.boticario.com.br/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'cross-site',
    'TE': 'trailers',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:126.0) Gecko/20100101 Firefox/126.0'
}
HEADER_FIRESTORE_GET ={
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate, br, zstd',
    'Accept-Language': 'pt-BR,pt;q=0.8,en-US;q=0.5,en;q=0.3',
    'Alt-Used': 'firestore.googleapis.com',
    'Connection': 'keep-alive',
    'Host': 'firestore.googleapis.com',
    'Origin': 'https://lojadigital.boticario.com.br',
    'Referer': 'https://lojadigital.boticario.com.br/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'cross-site',
    'TE': 'trailers',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:126.0) Gecko/20100101 Firefox/126.0'
}

PAYLOAD_FIRESTORE_REQUEST ={
    'count=6&ofs=0&req0___data__=%7B%22database%22%3A%22projects%2Floja-digital-344318%2Fdatabases%2F(default)%22%2C%22addTarget%22%3A%7B%22query%22%3A%7B%22structuredQuery%22%3A%7B%22from%22%3A%5B%7B%22collectionId%22%3A%22chats-sessions%22%7D%5D%2C%22where%22%3A%7B%22compositeFilter%22%3A%7B%22op%22%3A%22AND%22%2C%22filters%22%3A%5B%7B%22fieldFilter%22%3A%7B%22field%22%3A%7B%22fieldPath%22%3A%22businessUnit%22%7D%2C%22op%22%3A%22EQUAL%22%2C%22value%22%3A%7B%22stringValue%22%3A%22BOT%22%7D%7D%7D%2C%7B%22fieldFilter%22%3A%7B%22field%22%3A%7B%22fieldPath%22%3A%22status%22%7D%2C%22op%22%3A%22EQUAL%22%2C%22value%22%3A%7B%22stringValue%22%3A%22CONTACTED_USER%22%7D%7D%7D%2C%7B%22fieldFilter%22%3A%7B%22field%22%3A%7B%22fieldPath%22%3A%22teamId%22%7D%2C%22op%22%3A%22EQUAL%22%2C%22value%22%3A%7B%22stringValue%22%3A%22aCqILgwtzt%22%7D%7D%7D%5D%7D%7D%2C%22orderBy%22%3A%5B%7B%22field%22%3A%7B%22fieldPath%22%3A%22updatedAt%22%7D%2C%22direction%22%3A%22DESCENDING%22%7D%2C%7B%22field%22%3A%7B%22fieldPath%22%3A%22__name__%22%7D%2C%22direction%22%3A%22DESCENDING%22%7D%5D%2C%22limit%22%3A20%7D%2C%22parent%22%3A%22projects%2Floja-digital-344318%2Fdatabases%2F(default)%2Fdocuments%22%7D%2C%22targetId%22%3A4%2C%22resumeToken%22%3A%22CgkI48rIwaSchgM%3D%22%7D%7D&req1___data__=%7B%22database%22%3A%22projects%2Floja-digital-344318%2Fdatabases%2F(default)%22%2C%22addTarget%22%3A%7B%22query%22%3A%7B%22structuredQuery%22%3A%7B%22from%22%3A%5B%7B%22collectionId%22%3A%22chats-counters%22%7D%5D%2C%22where%22%3A%7B%22fieldFilter%22%3A%7B%22field%22%3A%7B%22fieldPath%22%3A%22teamId%22%7D%2C%22op%22%3A%22IN%22%2C%22value%22%3A%7B%22arrayValue%22%3A%7B%22values%22%3A%5B%7B%22stringValue%22%3A%22aCqILgwtzt%22%7D%2C%7B%22stringValue%22%3A%22XvzOaT8dUE%22%7D%2C%7B%22stringValue%22%3A%22SEA2mMksY2%22%7D%2C%7B%22stringValue%22%3A%22pTbot2SVbu%22%7D%2C%7B%22stringValue%22%3A%229c6a19c1-8cb8-4f07-97ea-f8031652acc6%22%7D%2C%7B%22stringValue%22%3A%2243EW2xGtPd%22%7D%2C%7B%22stringValue%22%3A%22nYiekCgNvH%22%7D%2C%7B%22stringValue%22%3A%229FvSFChGc1%22%7D%2C%7B%22stringValue%22%3A%22AJsPAUAhm4%22%7D%2C%7B%22stringValue%22%3A%22uPBoFosK8e%22%7D%5D%7D%7D%7D%7D%2C%22orderBy%22%3A%5B%7B%22field%22%3A%7B%22fieldPath%22%3A%22__name__%22%7D%2C%22direction%22%3A%22ASCENDING%22%7D%5D%7D%2C%22parent%22%3A%22projects%2Floja-digital-344318%2Fdatabases%2F(default)%2Fdocuments%22%7D%2C%22targetId%22%3A6%2C%22resumeToken%22%3A%22CgkI48rIwaSchgM%3D%22%7D%7D&req2___data__=%7B%22database%22%3A%22projects%2Floja-digital-344318%2Fdatabases%2F(default)%22%2C%22addTarget%22%3A%7B%22query%22%3A%7B%22structuredQuery%22%3A%7B%22from%22%3A%5B%7B%22collectionId%22%3A%22chats-counters%22%7D%5D%2C%22where%22%3A%7B%22fieldFilter%22%3A%7B%22field%22%3A%7B%22fieldPath%22%3A%22teamId%22%7D%2C%22op%22%3A%22IN%22%2C%22value%22%3A%7B%22arrayValue%22%3A%7B%22values%22%3A%5B%7B%22stringValue%22%3A%22jGqofaS7rR%22%7D%2C%7B%22stringValue%22%3A%22h1VHrYVD0T%22%7D%2C%7B%22stringValue%22%3A%22b986bb7f-1478-4918-bc80-fb0e11483949%22%7D%2C%7B%22stringValue%22%3A%22n0Wu9pnisA%22%7D%2C%7B%22stringValue%22%3A%22mI7lmmgK7u%22%7D%2C%7B%22stringValue%22%3A%22f4793141-f8f8-4b4d-9da1-a91d39e4f1fb%22%7D%2C%7B%22stringValue%22%3A%22eNRx6hTlrS%22%7D%2C%7B%22stringValue%22%3A%22ZkzVKj6GS1%22%7D%2C%7B%22stringValue%22%3A%22qpnkjromR1%22%7D%2C%7B%22stringValue%22%3A%22C8qAW4nPCA%22%7D%5D%7D%7D%7D%7D%2C%22orderBy%22%3A%5B%7B%22field%22%3A%7B%22fieldPath%22%3A%22__name__%22%7D%2C%22direction%22%3A%22ASCENDING%22%7D%5D%7D%2C%22parent%22%3A%22projects%2Floja-digital-344318%2Fdatabases%2F(default)%2Fdocuments%22%7D%2C%22targetId%22%3A8%2C%22resumeToken%22%3A%22CgkI48rIwaSchgM%3D%22%7D%7D&req3___data__=%7B%22database%22%3A%22projects%2Floja-digital-344318%2Fdatabases%2F(default)%22%2C%22addTarget%22%3A%7B%22query%22%3A%7B%22structuredQuery%22%3A%7B%22from%22%3A%5B%7B%22collectionId%22%3A%22chats-sessions%22%7D%5D%2C%22where%22%3A%7B%22compositeFilter%22%3A%7B%22op%22%3A%22AND%22%2C%22filters%22%3A%5B%7B%22fieldFilter%22%3A%7B%22field%22%3A%7B%22fieldPath%22%3A%22businessUnit%22%7D%2C%22op%22%3A%22EQUAL%22%2C%22value%22%3A%7B%22stringValue%22%3A%22BOT%22%7D%7D%7D%2C%7B%22fieldFilter%22%3A%7B%22field%22%3A%7B%22fieldPath%22%3A%22status%22%7D%2C%22op%22%3A%22EQUAL%22%2C%22value%22%3A%7B%22stringValue%22%3A%22WAITING%22%7D%7D%7D%2C%7B%22fieldFilter%22%3A%7B%22field%22%3A%7B%22fieldPath%22%3A%22teamId%22%7D%2C%22op%22%3A%22EQUAL%22%2C%22value%22%3A%7B%22stringValue%22%3A%22aCqILgwtzt%22%7D%7D%7D%5D%7D%7D%2C%22orderBy%22%3A%5B%7B%22field%22%3A%7B%22fieldPath%22%3A%22updatedAt%22%7D%2C%22direction%22%3A%22DESCENDING%22%7D%2C%7B%22field%22%3A%7B%22fieldPath%22%3A%22__name__%22%7D%2C%22direction%22%3A%22DESCENDING%22%7D%5D%2C%22limit%22%3A40%7D%2C%22parent%22%3A%22projects%2Floja-digital-344318%2Fdatabases%2F(default)%2Fdocuments%22%7D%2C%22targetId%22%3A16%2C%22resumeToken%22%3A%22CgkI48rIwaSchgM%3D%22%7D%7D&req4___data__=%7B%22database%22%3A%22projects%2Floja-digital-344318%2Fdatabases%2F(default)%22%2C%22addTarget%22%3A%7B%22query%22%3A%7B%22structuredQuery%22%3A%7B%22from%22%3A%5B%7B%22collectionId%22%3A%22chats-sessions%22%7D%5D%2C%22where%22%3A%7B%22compositeFilter%22%3A%7B%22op%22%3A%22AND%22%2C%22filters%22%3A%5B%7B%22fieldFilter%22%3A%7B%22field%22%3A%7B%22fieldPath%22%3A%22businessUnit%22%7D%2C%22op%22%3A%22EQUAL%22%2C%22value%22%3A%7B%22stringValue%22%3A%22BOT%22%7D%7D%7D%2C%7B%22fieldFilter%22%3A%7B%22field%22%3A%7B%22fieldPath%22%3A%22userId%22%7D%2C%22op%22%3A%22EQUAL%22%2C%22value%22%3A%7B%22stringValue%22%3A%22EbSjvaQRi1qptn1%22%7D%7D%7D%2C%7B%22fieldFilter%22%3A%7B%22field%22%3A%7B%22fieldPath%22%3A%22status%22%7D%2C%22op%22%3A%22EQUAL%22%2C%22value%22%3A%7B%22stringValue%22%3A%22CONTACTED_USER%22%7D%7D%7D%2C%7B%22fieldFilter%22%3A%7B%22field%22%3A%7B%22fieldPath%22%3A%22unreadMessages%22%7D%2C%22op%22%3A%22GREATER_THAN%22%2C%22value%22%3A%7B%22integerValue%22%3A%220%22%7D%7D%7D%5D%7D%7D%2C%22orderBy%22%3A%5B%7B%22field%22%3A%7B%22fieldPath%22%3A%22unreadMessages%22%7D%2C%22direction%22%3A%22ASCENDING%22%7D%2C%7B%22field%22%3A%7B%22fieldPath%22%3A%22__name__%22%7D%2C%22direction%22%3A%22ASCENDING%22%7D%5D%2C%22limit%22%3A1%7D%2C%22parent%22%3A%22projects%2Floja-digital-344318%2Fdatabases%2F(default)%2Fdocuments%22%7D%2C%22targetId%22%3A18%2C%22resumeToken%22%3A%22CgkI48rIwaSchgM%3D%22%7D%7D&req5___data__=%7B%22database%22%3A%22projects%2Floja-digital-344318%2Fdatabases%2F(default)%22%2C%22addTarget%22%3A%7B%22query%22%3A%7B%22structuredQuery%22%3A%7B%22from%22%3A%5B%7B%22collectionId%22%3A%22chats-sessions%22%7D%5D%2C%22where%22%3A%7B%22compositeFilter%22%3A%7B%22op%22%3A%22AND%22%2C%22filters%22%3A%5B%7B%22fieldFilter%22%3A%7B%22field%22%3A%7B%22fieldPath%22%3A%22businessUnit%22%7D%2C%22op%22%3A%22EQUAL%22%2C%22value%22%3A%7B%22stringValue%22%3A%22BOT%22%7D%7D%7D%2C%7B%22fieldFilter%22%3A%7B%22field%22%3A%7B%22fieldPath%22%3A%22status%22%7D%2C%22op%22%3A%22EQUAL%22%2C%22value%22%3A%7B%22stringValue%22%3A%22CONTACTED_USER%22%7D%7D%7D%2C%7B%22unaryFilter%22%3A%7B%22field%22%3A%7B%22fieldPath%22%3A%22teamId%22%7D%2C%22op%22%3A%22IS_NULL%22%7D%7D%5D%7D%7D%2C%22orderBy%22%3A%5B%7B%22field%22%3A%7B%22fieldPath%22%3A%22updatedAt%22%7D%2C%22direction%22%3A%22DESCENDING%22%7D%2C%7B%22field%22%3A%7B%22fieldPath%22%3A%22__name__%22%7D%2C%22direction%22%3A%22DESCENDING%22%7D%5D%2C%22limit%22%3A20%7D%2C%22parent%22%3A%22projects%2Floja-digital-344318%2Fdatabases%2F(default)%2Fdocuments%22%7D%2C%22targetId%22%3A20%2C%22resumeToken%22%3A%22CgkI48rIwaSchgM%3D%22%7D%7D'
}

PAYLOAD_FIRESORE_SID = {
    'count=1&ofs=7&req0___data__=%7B%22database%22%3A%22projects%2Floja-digital-344318%2Fdatabases%2F(default)%22%2C%22addTarget%22%3A%7B%22query%22%3A%7B%22structuredQuery%22%3A%7B%22from%22%3A%5B%7B%22collectionId%22%3A%22chats-sessions%22%7D%5D%2C%22where%22%3A%7B%22compositeFilter%22%3A%7B%22op%22%3A%22AND%22%2C%22filters%22%3A%5B%7B%22fieldFilter%22%3A%7B%22field%22%3A%7B%22fieldPath%22%3A%22businessUnit%22%7D%2C%22op%22%3A%22EQUAL%22%2C%22value%22%3A%7B%22stringValue%22%3A%22BOT%22%7D%7D%7D%2C%7B%22fieldFilter%22%3A%7B%22field%22%3A%7B%22fieldPath%22%3A%22status%22%7D%2C%22op%22%3A%22EQUAL%22%2C%22value%22%3A%7B%22stringValue%22%3A%22WAITING%22%7D%7D%7D%2C%7B%22fieldFilter%22%3A%7B%22field%22%3A%7B%22fieldPath%22%3A%22teamId%22%7D%2C%22op%22%3A%22EQUAL%22%2C%22value%22%3A%7B%22stringValue%22%3A%22f4793141-f8f8-4b4d-9da1-a91d39e4f1fb%22%7D%7D%7D%5D%7D%7D%2C%22orderBy%22%3A%5B%7B%22field%22%3A%7B%22fieldPath%22%3A%22updatedAt%22%7D%2C%22direction%22%3A%22DESCENDING%22%7D%2C%7B%22field%22%3A%7B%22fieldPath%22%3A%22__name__%22%7D%2C%22direction%22%3A%22DESCENDING%22%7D%5D%2C%22limit%22%3A40%7D%2C%22parent%22%3A%22projects%2Floja-digital-344318%2Fdatabases%2F(default)%2Fdocuments%22%7D%2C%22targetId%22%3A22%7D%7D'
}