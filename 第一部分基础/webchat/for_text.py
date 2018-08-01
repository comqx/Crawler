#!/usr/bin/env python
#-*- coding: utf-8 -*-
# writer:lqx
import requests,time,json


# for i in range(0,100):
# time.sleep(3)
cookies_1={
           'session':'.eJylVFtP4zgU_i-Rdp_YxbGd2EaqdmgptFDSQimXLqvK8SU1bZI2lzYF8d_HCVCWkeZhdvNg-Zzv3M_nvDiizDKVFLMyV5lz9OIcr1bHQqRlUpwueeQcgQOnkyYFF59yT3HZj6M32d3Lk2zpHDmHIjJ_hCY5jOOtCrdVc29ukSqMSJO_crVuIdfHHoIU_V7nTXisWt8kA5hhnwmNNfS5xB7U1PehED5hElEGgQcRZ0pj7krJdOhZNfNUCDXBNlS-ULvWN5HtVsVMY8q5DsOZ8hAilCjl-5JhpKFWLvCQlL5S0Bbh2PqNVP1kVRZtnu2bDIxYBLYu29Jl9ufAmo0e-okpDK-7bMSrkicjk7yJ1yrm2YfHXv7B50P5xXOsqmaMYxMlvCizOsBjyYgPHksfuu5jSXyK6zuWjyUF2p5YE12ftc0bykLsPZYeZKHVK2BtfILsqTUQH9F-at9E-2muf0VDAMC65CR_3z6xQmHHlhmVyGZwk7ovFzDkIuBSzyrsht_n8r93bHPfqszo3X5Pdyq8q0bLMjLJeGsKMbfa1wNnLVJZZ7ya3na6BZSbqNWyzvkuETNLk5rpnZrkzhE-cAYmt5e_X5yLGrGruK0X5lOCXUJcG-4dgV8Q6rl7BH1FMNsjLgDgHXQ9BKAPGYSv_9gS7WtYqGIm0nRhVF1QHM-WPLFtOc_zWSew5TbvZsbLYj57s7ZYp5-3u8M1SC67w7P0uB1lBFZ-d7vo9kMdn-TppKIevu6m3s19b3p-fDHpmfHEGz1dP0_icSkhO-8du9dV-9Ij8fkoWnogTntPF9WDvh-JXbUc9RFSUE8n6QkXoj2CkkYX8LCz6QYuztBKG5qsevf3g5PhduGi2960H-H-Khyuh7suSsepGvD58DDwET29bz9QPgqGT1ebNKatfUuSF_yzpWgs727G_SCQcrep9HR65-o0T8yHebkxlltOCO1nOelTF2ntcaU5JYQwH3MOfKEgs2UrD_OQIK…'}
data = {
    'to': '@4a732bced005fed407a71a79fe94fd5a8a632937228c82a21356cb9243a79200',
    'content': '123123123',
}
rets=requests.get(url='http://127.0.0.1:5000/send')
print(rets.cookies)
# ret=requests.post(
#     url='http://127.0.0.1:5000/send',
#     json=data,
#     headers={
#         'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36',
#         'Referer': 'http://127.0.0.1:5000/user_list',
#         'Host':'127.0.0.1:5000',
#         'Origin': 'http://127.0.0.1:5000'
#     },
#     cookies=bytes(json.dumps(cookies_1),encoding='utf-8')
# )
# print(ret.text)
