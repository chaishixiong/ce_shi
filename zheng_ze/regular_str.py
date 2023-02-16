import re

tb_str = '''<li class="shop-service-info-item">
                        <span class="title">描述</span>
                        <span class="rateinfo">
                                        <em>4.8</em>
                                        <i class="rate-icon higher"></i>
                                    </span>'''


aa = re.findall('>描述</span>([\s\S]*?)<span class="rateinfo">([\s\S]*?)<em>(.*?)</em>',tb_str)
print(aa)





