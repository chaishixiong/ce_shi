# Scrapy settings for amazon_spider project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'amazon_spider'

SPIDER_MODULES = ['amazon_spider.spiders']
NEWSPIDER_MODULE = 'amazon_spider.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'amazon_spider.middlewares.AmazonSpiderSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
   # 'amazon_spider.middlewares.ProxyMiddleware': 201,
   'amazon_spider.middlewares.UserAgentMiddleware': 203,
   'amazon_spider.middlewares.CookieMiddleware': 204,
   'amazon_spider.middlewares.DownloadMiddleware': 250,
}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   # 'amazon_spider.pipelines.AmazonPipeline': 300,
   'amazon_spider.pipelines.AmazonspiderPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'


proxy_pool = [
    "http://175.147.118.60:4350",
              ]
cookies_pool = [
    'ubid-main=135-3320295-7155055; skin=noskin; s_fid=58F79F01F0637333-1058AD352C38EF42; regStatus=pre-register; s_cc=true; session-id=141-6401734-9560133; sst-main=Sst1|PQGZ9GnsErHDummSgQt46kFQCRDpbJJhEt8N7Qeesy-riIWIcG5YMP6m3a2zCHxoOPFxrMvyVh330OaLRVu1sNV1iPm91GntQm8VsPnBjruG_fZa-gjqUe7UO9yKU2o1TZvV33hWqc4f0FoyP3AUDUFaDBgNFuhVeTHR_FhhPWpeY2MxRDhL8yACbxWyb2yzjj5izR_w5whHHfgwy0EZ_Gngf51mYE-MkbXWwvWWuZHAIJDyLBF5TSwtMu0Fmf9EqVhyqaR0IwbZ6qqu8tyXmn2Mx5Md5IAsWboSbEYDJgmSzKU; i18n-prefs=USD; s_vn=1643982728315%26vn%3D2; s_dslv=1612767318919; s_nr=1612767318921-Repeat; s_sq=%5B%5BB%5D%5D; aws_lang=cn; aws-target-data=%7B%22support%22%3A%221%22%7D; aws-target-visitor-id=1612767323708-922832.38_0; aws-mkto-trk=id%3A112-TZM-766%26token%3A_mch-aws.amazon.com-1612767337859-69796; session-token=DiN6686w9JDyP28GHos+tBb6fcwj5aMhAi2l9bguHyyKPT23xArKwWibBJyJj+Ure6gjVxRWuj0nV7i3vCN6KBOK9gHKfncV2n9GpFtR+R+Gn+VOHNC5UKn9k0opB8MxT473bh2BZYnUy0hyQFEbZ5yXbQO++qCgkDwjgx5lnzvfpCPJ3vG4hrEpizfHx9suNhpK4Mah23q3uUMG16AncJANDpPY6pu3BViN5Doklix1oYs8sQ0Dm4CNVVCUXUpU; session-id-time=2082787201l; lc-main=en_US; csm-hit=tb:s-AYWTEJXTVC2ZAN7CR066|1613717208684&t:1613717211312&adb:adblk_no',
    'session-id=132-5762587-8540731; session-id-time=2082787201l; i18n-prefs=USD; sp-cdn="L5Z9:HK"; ubid-main=134-7690691-4844300; ubid-acbus=134-7690691-4844300; s_pers=%20s_fid%3D71049A542F293B3A-075B5ED994695836%7C1769335850847%3B%20s_dl%3D1%7C1611571250848%3B%20gpv_page%3DUS%253ASD%253AFBA-main%7C1611571250850%3B%20s_ev15%3D%255B%255B%2527NSGoogle%2527%252C%25271611569450853%2527%255D%255D%7C1769335850853%3B; skin=noskin; session-id-eu=262-9734653-4678917; ubid-acbuk=262-3004603-9293057; session-id-time-eu=2243127287l; s_sess=%20c_m%3Dwww.google.comNatural%2520Search%3B%20s_ppvl%3DUS%25253ASD%25253AFBA-main%252C8%252C8%252C821%252C1440%252C821%252C1440%252C900%252C2%252CL%3B%20s_ppv%3DUS%25253ASD%25253AFBA-main%252C24%252C8%252C2523%252C1440%252C821%252C1440%252C900%252C2%252CL%3B%20s_cc%3Dtrue%3B%20s_sq%3D%3B%20ev1%3Dn/a%3B; session-token=3i/3FAHuMQDKu9VKIeEQarOjYIcfpsFBJgb6udWyCZfLnrMLCOkgxrIvGqW4XTGWeuXTTLkyQqbMt6IahTAqt+doHEWj4tFDgxkqGZv3nZL4RnGJos1qZThaZfO7BQfXpzgx3yp4zfcQ5PKvft/pOkhJLAzZ6YG12ih+mxWncFkEEgiR14G73MEb+6XoM/2Q; csm-hit=tb:SMDNERBEB54ZV83VH93S+s-SMDNERBEB54ZV83VH93S|1613717399207&t:1613717399207&adb:adblk_no',
    'session-id=134-8657303-5637206; ubid-main=131-4037381-9168129; x-main="tDkQoiRHYNLhVwcQiSe20WJEsIQpAXk5brTjU@bXe@G80ycd4j2bkWrOSBfVicP5"; at-main=Atza|IwEBIPgj9JNgwxJgUaLTK-c5-OqbjZAN6xRiVIOPqq7qqHE1oKotrIaGmcr5tSLVLEoacglD1SxD-vFynmYwvrkBTASzKm3uomQcTks3zFlup48aKYzI2tLnfciUwhBT44_G68357vKRv1vibkuCecS0n6iOnTgrI6KjFh3AqC3yOUop3FdBSE7S-XUjcodK7gWCd4f9plka7lIEk9giXg_adBKa; sess-at-main="bme/0WgnRW+byLjZVwzXJuc4zAxw6SJiEWDU+jUOuUE="; sst-main=Sst1|PQFOegtPseRNSp_LWxNC-B6BC1N2jGNFTKNNOq-jH--FRyydpzjiG3eqyDDhyORhTp4t5clhgXGZVT8okPcmGScHdyoGdkNgp_eWOkpyoq0l90kZRqOrfa7IREQspxxEd3stQeC8774Pz4szI8m8I7OYq4CRzZKWdYmyMUP5MD_v0KJUzYqfKuTmSCjgo-SiRa_KOoHaSjjJFPzrHaFFU4tzCd7xTxKSglJjVBayN9nKZ-y6xTJ1XeRCZbK93froyEzIuh-it50g8Xu8-7Ft3tH9DyKZgYfLEqs7A1_yeAGwDp2TzBr7P8G49fRTeGBDcTTQk-4coxbNyBBIed3RhFK_Tg; session-id-time=2082787201l; i18n-prefs=USD; sp-cdn="L5Z9:HK"; skin=noskin; lc-main=en_US; s_sess=%20s_cc%3Dtrue%3B%20s_sq%3D%3B%20ev1%3Dn/a%3B; session-token="wFs9uj0f/JzWavomm07Typ51UVpiVeMCGGDy0sAp8/MgttZQjdLDSpCTm7LItxi/+i99I6VSpoAtfn6yYd32ZEoSTPFBuknSBQAJvF7nxOreASPZEnTe9d4QKVmgwTFumak2d8wYsluP3U0j1Xy+0RYrrar3Kpkd10ut7qVZo/uhxDDvrEYJoklGp8MlCfeOgp9S9u2r4l33gvLmV/Ip1w=="; csm-hit=tb:s-W6H9RYMBH3Q23Y7SF53F|1613717427791&t:1613717428134&adb:adblk_no',
    'session-id=138-4907067-0043604; session-id-time=2082787201l; sp-cdn="L5Z9:HK"; ubid-main=131-1891987-4827855; lc-main=zh_CN; i18n-prefs=USD; session-token=sVwtW9Yur95HL9Sray7gthwsUEdfKuBijdzcw2Qy5YdCPsGrHvUSKAdynBZWcPfnJyz33gwuR3ZWMk5JjESTaggpIR0gmvWHsn4EFeWC1nyQoZkEg6sLo6RlF9dLRLBIeXggt9NXblAMOJMtGCl8yfQysWarvJG/m6jPSQcYvlYQG/2ZKVhGsPEfmzBCeaat; skin=noskin; csm-hit=tb:s-Q85B2M5M1SKM9CWKERXY|1613717642655&t:1613717642655&adb:adblk_no',
    'session-id=135-0606651-4029144; session-id-time=2082787201l; ubid-main=135-2920648-6633923; i18n-prefs=USD; sp-cdn="L5Z9:HK"; s_fid=34E8A5EF85F26E16-365219967A5C7A63; regStatus=pre-register; aws-target-data=%7B%22support%22%3A%221%22%7D; aws-target-visitor-id=1610783922455-15501.38_0; lc-main=en_US; session-token=bXzyI6Gr6vOEEECoHlVTpZvgh1YTrqpCr/5nX1RrEuZ8Ceo/ie2+HwY9wMvZnfcYTz4YOBElCab62i835BuVcS/7bSKYOP43voU5Rqf3j4rQb2sz6yTPUZ1uoPXOSTlbZ/bNHgSHwuG4faTPGZlbcoEizp7M+8vTyWLoiWZKog7Wu+WY7EB5r5EGBj3Z5FZf; skin=noskin; csm-hit=tb:s-R1C14AVA0BQQJXDNG5XW|1613717653870&t:1613717654009&adb:adblk_no',
    'session-id=144-7008120-2099004; session-id-time=2082787201l; i18n-prefs=USD; lc-main=zh_CN; sp-cdn="L5Z9:HK"; ubid-main=132-6546535-4852359; session-token=SwdJF1gCKkT6oebpiDWCSVFZ4fKPGfpumoM1r+igIDOnlP9n0f9nhIqdcZZ1cF4Bbd83jd15gs220ov5pp8MbdH4Z5RuISL91in09U1I11BbMHkT5MO4+6n2niAzX8dwaUhmzfZ7/K7XVWonAyp/kfByjiWMcRRRcDrIVA90qGveokLHqyCo6495jHlYiyv/; skin=noskin; csm-hit=tb:s-DD4H0GTCJW0NZ6T056VN|1613717656658&t:1613717657010&adb:adblk_no',
    'session-id=461-6612532-6110006; ubid-acbcn=459-1543297-9053728; session-token="d1qeWa4zh9u864bKfxPH1RT995RdBBQbpUBSFk5rRcxfr7wtfjC0z+4xIA6AbIrHanxAqo7AaMpsR3Fz7dj+UBHG4dZugZDhNPGuD4gwwNmum5UHbC6RDQjPAeXeRE77Tfi3slKVfXYGlnQwf5SWThK9sVihU1xpZmTWAq9uJV+gQlJeBQ37J8uf9fqm6/fG0GWAhDLU6ugTbPRtdsaRXd6ESNaX4pu60XXWBYRNEtGWoEIIjNsawL+JB6cKlIJWN3CPrxYb4RmWVy2o2kizyg=="; x-acbcn="XUpW7S8sMKs0JkW@1HMAu1SXcGBiJ4ISj5pqiP@ZW0iE5XvxXYAJuewXx3nIrrJn"; at-main=Atza|IwEBILYfebMO8ctae0eRTY5owNjoi7gyOkyTahdvg877TCuuFB1762lYFaGsCib6skIGRvuN3UFbPXQY6w6COcnEAqJWw70OO-uHH_myFDTAJVVKSCQpmbziNKR08y-xdQeXvVU363ze7wLwdK-GhTOh3hwOvJMliRIv3DmLst7M6Wz_yyOu-RL8n-SMXizevopJgFTTtneruk0bcFhu5hidHqOpTtUb7CF9P9PAVY0UjyutqA; sess-at-main="a6pj8ksxKWyIdAW+7aFDYk9Hi/ms1i4kKoHSZu8VNmk="; sst-main=Sst1|PQGy0tw65vz8QXFRpCH_itPvCVBTKfTc-DMxJ30gyq6hFfhIi63tK8-Cna9ek-TYqyfyogXdQWRK8Y_Vd_8v90C00TOwRjOJNxnwJMuHWl1P-QJdT1LoEMtqTgR9ywxn_bpDl0kSaqDl9FnuvYVoTTyPm0-4RNJIC3EBobMXNashrEtTC5_hdMe7cNQz68nJVZ6yBya-YgsJHj2FOv8mg3Lss7VHK48H5fBd9arwKPZdqC8RAB3YYphToH2paTfAkzo1fGWrNPYTfQTnWvVJjbx0S8R8ovgXILHfc9eBIiLaecw; lc-acbcn=zh_CN; i18n-prefs=CNY; csm-hit=tb:s-Y3Q1KD91AV3XG4Z1N37X|1613717622529&t:1613717622529&adb:adblk_no; session-id-time=2082729601l',
    'i18n-prefs=USD; ubid-main=135-9665041-0430418; aws-priv=eyJ2IjoxLCJldSI6MCwic3QiOjB9; aws-target-static-id=1570778777123-971599; aws-target-data={"support":"1"}; sid="QP5dTe+7YuXEMYbl1z0KEQ==|qtVe22zwnTFm++dmT4sC7d0h93crc5OgsZxh0i4NDdk="; sst-main=Sst1|PQFJXr7cvfV5vcAW7IPbY_avC_TD77kS4QYE3Y3sGlbNgetJh6CJlNPXWE1D6LKvF7pTEyxzdSSZurpnbIRwD_KoYXHoREM3h5WCG8CRBZCwcFlwD06-lCWCp3CnITB6rEbwPnv9tT0ZI6UER9IhKhapkn4wBlFsNrNbP_LWrHTpgzF5lNmsC-17oBr8rn7Hh-4L3nFLgoxM9nsspPFOXNlB0BXPthFRucqACvi-OxHCl-cBhZoN2j5JqOJOd_5g3dvgS3dO32iRDwFy_PcXjkRwp4o59WPFS4_SOjxZuIv_75JwxewsjPhwo05iCb_2YIAf552t_iHVWpjUkhkBb8lgJw; ubid-acbuk=258-6148986-0872627; aws-ubid-main=508-1538521-6584650; _mkto_trk=id:365-EFI-026&token:_mch-amazon.com-1574825158479-68846; s_vnum=2007269925428&vn=3; s_fid=0A0B6DBFD0C4C1DA-18AFEBE1A73DACF7; s_pers= s_fid=08FB2CC0DA10551B-1E39CB4F2E2D92C0|1638006116821; s_ev15=%5B%5B%27SCSPStriplogin%27%2C%271574249273195%27%5D%2C%5B%27Typed%2FBookmarked%27%2C%271574847716833%27%5D%5D|1732700516833; s_dl=1|1591706689490; gpv_page=US%3ASC%3A%20SellerCentralLogin|1591706689496;; aws-target-visitor-id=1570778777128-465564.38_0; AMCV_4A8581745834114C0A495E2B@AdobeOrg=-432600572|MCIDTS|18425|MCMID|80499345516731451323254846103818984868|MCOPTOUT-1591883850s|NONE|MCAID|NONE|vVersion|4.5.2|MCAAMLH-1592481450|11|MCAAMB-1592481450|j8Odv6LonN4r3an7LhD3WZrU1bUpAkFkkiY1ncBR96t2PTI; mbox=session#b2f301539b6b4374a3fcb0d8a77bb0b1#1591878510|PC#b2f301539b6b4374a3fcb0d8a77bb0b1.38_0#1655121451; s_lv=1591876650911; lc-main=en_US; session-id=134-1521345-1283516; sp-cdn="L5Z9:HK"; s_dslv_s=Less than 1 day; s_depth=2; s_dslv=1607325228644; s_vn=1638863841420&vn=3; regStatus=registered; s_nr=1607350740846-Repeat; aws-business-metrics-last-visit=1607350742113; session-id-time=2082787201l; aws-userInfo={"arn":"arn:aws:iam::052435105583:root","alias":"","username":"dingbo2020","keybase":"nJY4jZ8iD/Bh77fEahJfJApWK81PrQAW4oKwSqS0hyY\\u003d","issuer":"http://signin.aws.amazon.com/signin","signinType":"PUBLIC"}; aws-session-id=790-9696113-5387128; aws-analysis-id=790-9696113-5387128; aws-userInfo-signed=eyJ0eXAiOiJKV1MiLCJrZXlSZWdpb24iOiJ1cy1lYXN0LTEiLCJhbGciOiJFUzM4NCIsImtpZCI6ImYzZjk4MmNhLTlhNWUtNGY4OC1hMTc1LTVlNTYxMDMwNWQ4NSJ9.eyJzdWIiOiIiLCJzaWduaW5UeXBlIjoiUFVCTElDIiwiaXNzIjoiaHR0cDpcL1wvc2lnbmluLmF3cy5hbWF6b24uY29tXC9zaWduaW4iLCJrZXliYXNlIjoibkpZNGpaOGlEXC9CaDc3ZkVhaEpmSkFwV0s4MVByUUFXNG9Ld1NxUzBoeVk9IiwiYXJuIjoiYXJuOmF3czppYW06OjA1MjQzNTEwNTU4Mzpyb290IiwidXNlcm5hbWUiOiJkaW5nYm8yMDIwIn0.k339yuWenUrxlaKdZSmp4wCrC10vtLpHy-iAN157vDdldif8E6h-hdAV44g7GCa9rWgpc_Slpb_98wHzVPHIH2_giwtVM5dBmXt1Z_aV6BXrueD82kmvyjbG3kmWspPa; aws-session-id-time=1611480615l; session-token=GljyGYANu63nwh+LWtt2txOx7SY2bYmfQcNk3Gko9F4FnISxJ8i/vioSFvCA1uNaEHrqKYu5wBySUO+CGzzcm+0gCrOWWiH+BhPMVBEk2KGermpqP56Nmf6xrt8Z+ERGnIMjNl1RG0yTIgvWOTjcu2OgpQ+OTTq1+9alV7lVW5SsdkSWocYRD6Dh/Za45HXH; skin=noskin'


]

