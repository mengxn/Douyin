import re
import requests

from DataExtractor import Extractor
from Parameter import XBogus, Headers


class Douyin(object):
    detail_url = 'https://www.douyin.com/aweme/v1/web/aweme/detail/'
    share_url = ''

    def get_location(self):
        resp = requests.get(url=self.share_url, allow_redirects=False)
        return resp.headers.get('Location')

    def get_detail(self, vid):
        cookies = {
            'IsDouyinActive': 'true',
            'home_can_add_dy_2_desktop': '%220%22',
            'stream_recommend_feed_params': '%22%7B%5C%22cookie_enabled%5C%22%3Atrue%2C%5C%22screen_width%5C%22%3A1792%2C%5C%22screen_height%5C%22%3A1120%2C%5C%22browser_online%5C%22%3Atrue%2C%5C%22cpu_core_num%5C%22%3A8%2C%5C%22device_memory%5C%22%3A0%2C%5C%22downlink%5C%22%3A%5C%22%5C%22%2C%5C%22effective_type%5C%22%3A%5C%22%5C%22%2C%5C%22round_trip_time%5C%22%3A0%7D%22',
            'dy_sheight': '1120',
            'dy_swidth': '1792',
            'ttwid': '1%7C2vfSdBcN_f4CyjRlZ_YpKAU0Na0rzFmDCJDGSXWkxdM%7C1703137743%7Cda2380ed694035a59bfbf3860c51699829cc08dff39faac5ab100ab0b64e57f0',
            'msToken': 'x62pRPrepX2bAEReBXmD9PsHg7Xjay1ZLyVl55ot5FdFWQKAIXneeq1yGgS2aYroVmmVl_Fo_FG8FwDXA2etmFvTB2fr10CVEsU41oihaVa0AXMl759esQhJMLNz',
            'msToken': 'Y7AqatTqcOtOcT6-ldXzD7HPpAzAY1BI1R7s12GFyTqwHK_x5iyaOfEbPX9bpxAHVSBWFJgKSwaQClSqOqJpENhy-6WaBKGwhOFZ3ACR4eTLnuwsBbhzmdfWcbte',
            'download_guide': '%221%2F20231222%2F0%22',
            'tt_scid': 'YUBDlbeSw4OYLAZBlSH2d3y3VAFW2f8ohqaNKavp6NUm2Z8rJXvFJOhL6r-ZmmAD06c1',
            'bd_ticket_guard_client_data': 'eyJiZC10aWNrZXQtZ3VhcmQtdmVyc2lvbiI6MiwiYmQtdGlja2V0LWd1YXJkLWl0ZXJhdGlvbi12ZXJzaW9uIjoxLCJiZC10aWNrZXQtZ3VhcmQtcmVlLXB1YmxpYy1rZXkiOiJCSEVvb2lVemRoU05ValJaVmxLUTB5aGZvVWRZcWJJMFRQK21iWmFLWVRoYWRsaFpBVENxcXpJS3hWbisvNlFaRHU0YjI2aXR0R3h1RWpqdmpqZ25PUFU9IiwiYmQtdGlja2V0LWd1YXJkLXdlYi12ZXJzaW9uIjoxfQ%3D%3D',
            'bd_ticket_guard_client_web_domain': '2',
            'FORCE_LOGIN': '%7B%22videoConsumedRemainSeconds%22%3A180%7D',
            'csrf_session_id': '65d238a9d9485b9a517fef6b5214fb24',
            'ttcid': '3cca60c7cb9741f893a4e4a5a52b8ce421',
            'volume_info': '%7B%22isUserMute%22%3Afalse%2C%22isMute%22%3Afalse%2C%22volume%22%3A0.6%7D',
            'strategyABtestKey': '%221703210052.001%22',
            's_v_web_id': 'verify_lqfzaf2n_XzQSYTdM_ji23_40uL_9J9q_6UgzGL7lvtV5',
            '__ac_nonce': '06584ec4000bdc252bb30',
            '__ac_signature': '_02B4Z6wo00f01hOsl7QAAIDDrOM4bh5OZLoTnJMAAOF91b',
            'passport_csrf_token': '2e1f8c230fb239e41212a1c2c95806e0',
            'passport_csrf_token_default': '2e1f8c230fb239e41212a1c2c95806e0',
        }
        headers = {
            'Sec-Fetch-Site': 'same-origin',
            # 'Cookie': 'IsDouyinActive=true; home_can_add_dy_2_desktop=%220%22; stream_recommend_feed_params=%22%7B%5C%22cookie_enabled%5C%22%3Atrue%2C%5C%22screen_width%5C%22%3A1792%2C%5C%22screen_height%5C%22%3A1120%2C%5C%22browser_online%5C%22%3Atrue%2C%5C%22cpu_core_num%5C%22%3A8%2C%5C%22device_memory%5C%22%3A0%2C%5C%22downlink%5C%22%3A%5C%22%5C%22%2C%5C%22effective_type%5C%22%3A%5C%22%5C%22%2C%5C%22round_trip_time%5C%22%3A0%7D%22; dy_sheight=1120; dy_swidth=1792; ttwid=1%7C2vfSdBcN_f4CyjRlZ_YpKAU0Na0rzFmDCJDGSXWkxdM%7C1703137743%7Cda2380ed694035a59bfbf3860c51699829cc08dff39faac5ab100ab0b64e57f0; msToken=x62pRPrepX2bAEReBXmD9PsHg7Xjay1ZLyVl55ot5FdFWQKAIXneeq1yGgS2aYroVmmVl_Fo_FG8FwDXA2etmFvTB2fr10CVEsU41oihaVa0AXMl759esQhJMLNz; msToken=Y7AqatTqcOtOcT6-ldXzD7HPpAzAY1BI1R7s12GFyTqwHK_x5iyaOfEbPX9bpxAHVSBWFJgKSwaQClSqOqJpENhy-6WaBKGwhOFZ3ACR4eTLnuwsBbhzmdfWcbte; download_guide=%221%2F20231222%2F0%22; tt_scid=YUBDlbeSw4OYLAZBlSH2d3y3VAFW2f8ohqaNKavp6NUm2Z8rJXvFJOhL6r-ZmmAD06c1; bd_ticket_guard_client_data=eyJiZC10aWNrZXQtZ3VhcmQtdmVyc2lvbiI6MiwiYmQtdGlja2V0LWd1YXJkLWl0ZXJhdGlvbi12ZXJzaW9uIjoxLCJiZC10aWNrZXQtZ3VhcmQtcmVlLXB1YmxpYy1rZXkiOiJCSEVvb2lVemRoU05ValJaVmxLUTB5aGZvVWRZcWJJMFRQK21iWmFLWVRoYWRsaFpBVENxcXpJS3hWbisvNlFaRHU0YjI2aXR0R3h1RWpqdmpqZ25PUFU9IiwiYmQtdGlja2V0LWd1YXJkLXdlYi12ZXJzaW9uIjoxfQ%3D%3D; bd_ticket_guard_client_web_domain=2; FORCE_LOGIN=%7B%22videoConsumedRemainSeconds%22%3A180%7D; csrf_session_id=65d238a9d9485b9a517fef6b5214fb24; ttcid=3cca60c7cb9741f893a4e4a5a52b8ce421; volume_info=%7B%22isUserMute%22%3Afalse%2C%22isMute%22%3Afalse%2C%22volume%22%3A0.6%7D; strategyABtestKey=%221703210052.001%22; s_v_web_id=verify_lqfzaf2n_XzQSYTdM_ji23_40uL_9J9q_6UgzGL7lvtV5; __ac_nonce=06584ec4000bdc252bb30; __ac_signature=_02B4Z6wo00f01hOsl7QAAIDDrOM4bh5OZLoTnJMAAOF91b; passport_csrf_token=2e1f8c230fb239e41212a1c2c95806e0; passport_csrf_token_default=2e1f8c230fb239e41212a1c2c95806e0',
            'Connection': 'keep-alive',
            'Sec-Fetch-Mode': 'cors',
            'Accept': 'application/json, text/plain, */*',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.1 Safari/605.1.15',
            'Referer': 'https://www.douyin.com/video/7315207091856084259',
            'Sec-Fetch-Dest': 'empty',
            'Accept-Language': 'zh-CN,zh-Hans;q=0.9',
        }
        params = {
            'device_platform': 'webapp',
            'aid': '6383',
            'channel': 'channel_pc_web',
            'aweme_id': '7315207091856084259',
            'pc_client_type': '1',
            'version_code': '190500',
            'version_name': '19.5.0',
            'cookie_enabled': 'true',
            'screen_width': '1792',
            'screen_height': '1120',
            'browser_language': 'zh-CN',
            'browser_platform': 'MacIntel',
            'browser_name': 'Safari',
            'browser_version': '17.1',
            'browser_online': 'true',
            'engine_name': 'WebKit',
            'engine_version': '605.1.15',
            'os_name': 'Mac OS',
            'os_version': '10.15.7',
            'cpu_core_num': '8',
            'device_memory': '',
            'platform': 'PC',
            'webid': '7314920853232633398',
            'msToken': 'Y7AqatTqcOtOcT6-ldXzD7HPpAzAY1BI1R7s12GFyTqwHK_x5iyaOfEbPX9bpxAHVSBWFJgKSwaQClSqOqJpENhy-6WaBKGwhOFZ3ACR4eTLnuwsBbhzmdfWcbte',
            'X-Bogus': 'DFSzswVYQ8xANC6itNDOMPsMDyTK',
        }
        params['aweme_id'] = vid
        # 'Referer': 'https://www.douyin.com/video/7315207091856084259',
        headers['Referer'] = 'https://www.douyin.com/video/%s' % vid
        resp = requests.get(self.detail_url, params=params, cookies=cookies, headers=headers)
        if resp.status_code == 200:
            return resp.json()
        return None

    def get_account_data(self, sid):
        post_api = "https://www.douyin.com/aweme/v1/web/aweme/post/"
        all_data_list = []
        finished = False
        cursor = 0
        sec_user_id = 'MS4wLjABAAAAKL4v2QTbBix0Pc2ploOoEaW_dXFDTijZ2CnIZyShFtQ'
        cookies = {
            'ttwid': '1%7Czxk5nlYOrg-mvN8w93ZgcqAIGFNV9F9GDMcwiGhy3ac%7C1700193322%7Ca169e31b0eead3612767d516ecdaa5284dc59cda49cb2dd8e83eb6cb29268f5e',
            'webcast_local_quality': 'null',
            'csrf_session_id': '7100a0200a99f4494d25b8a2d3ac5fa6',
            'bd_ticket_guard_client_web_domain': '2',
            '__ac_nonce': '065ab39f40008b259aa49',
            '__ac_signature': '_02B4Z6wo00f01PDOGSgAAIDAImcw1ZAe19zw7h2AAFmeyWZYahdgrvQ9J.xfJCblTIuDVy878MkAopI-RMry7cs4o9JESrUgVqIpVd-roRhuaTytH0n4qOk2DDfi2gPogfA2J23izlCqHqknc7',
            'dy_swidth': '1792',
            'dy_sheight': '1120',
            'stream_recommend_feed_params': '%22%7B%5C%22cookie_enabled%5C%22%3Atrue%2C%5C%22screen_width%5C%22%3A1792%2C%5C%22screen_height%5C%22%3A1120%2C%5C%22browser_online%5C%22%3Atrue%2C%5C%22cpu_core_num%5C%22%3A12%2C%5C%22device_memory%5C%22%3A8%2C%5C%22downlink%5C%22%3A10%2C%5C%22effective_type%5C%22%3A%5C%224g%5C%22%2C%5C%22round_trip_time%5C%22%3A50%7D%22',
            'FORCE_LOGIN': '%7B%22videoConsumedRemainSeconds%22%3A180%7D',
            'strategyABtestKey': '%221705720312.475%22',
            'passport_csrf_token': '22923f34a64aa228ea65aad087c12cb5',
            'passport_csrf_token_default': '22923f34a64aa228ea65aad087c12cb5',
            'bd_ticket_guard_client_data': 'eyJiZC10aWNrZXQtZ3VhcmQtdmVyc2lvbiI6MiwiYmQtdGlja2V0LWd1YXJkLWl0ZXJhdGlvbi12ZXJzaW9uIjoxLCJiZC10aWNrZXQtZ3VhcmQtcmVlLXB1YmxpYy1rZXkiOiJCSE81LzdyTFI5VWRLaG8rVXhKVmxQOXRtR3l5MjE5azh1bjRCYXRrcXliekxRVUR0L0RaY0NtSVRKMmoxTUllQi8xUWxINjVzbmFhKzE5Tm5MSlVVQjQ9IiwiYmQtdGlja2V0LWd1YXJkLXdlYi12ZXJzaW9uIjoxfQ%3D%3D',
            'msToken': '8uliUXgOEy3oe-hzAsknoVTY12sqIP905GZ-UwDBFufe3z647odniJ-DXNr-XwitNBZ0C-2r6_yBnMLD-mBd7eYmUDHhq9QknoM0OwBo-pQ8vmuFUQ==',
            'tt_scid': '3GTPHASGobZ6vZkTqftR6WS0JhXLMi9kRp4szRNNvASaFHt7vTyWec9Yr3lXsEsn9b17',
            'IsDouyinActive': 'true',
            'home_can_add_dy_2_desktop': '%220%22',
        }
        xb = XBogus()
        user_agent, ua_code = Headers().generate_user_agent()
        headers = {
            'User-Agent': user_agent,
            'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'keep-alive',
            'Referer': 'https://www.douyin.com/'
        }
        while not finished:
            params = {
                "device_platform": "webapp",
                "aid": "6383",
                "channel": "channel_pc_web",
                "sec_user_id": sid,
                "max_cursor": cursor,
                "locate_query": "false",
                "show_live_replay_strategy": "1",
                "need_time_list": "0" if cursor else "1",
                "time_list_query": "0",
                "whale_cut_token": "",
                "cut_version": "1",
                "count": "18",
                "publish_video_strategy_type": "2",
                "pc_client_type": "1",
                "version_code": "170400",
                "version_name": "17.4.0",
                "cookie_enabled": "true",
                "platform": "PC",
                "downlink": "10",
                'msToken': 'Ft1Ag0Rft7b3GPjtkYhiesKj3TYBesHIXfPa-Q-z0rsuXMLNI9B1FPmuK-lslAQm_aP6iCkG4dYnk8Mvc0nO7cTU2R6cyJDIsJHarKJLhSm1FuZLjQ==',
            }
            params['X-Bogus'] = xb.get_x_bogus(params, ua_code, 23)
            resp = requests.get(post_api, params=params, headers=headers, cookies=cookies)
            try:
                if resp.status_code == 200:
                    data = resp.json()
                    if (data_list := data["aweme_list"]) is None:
                        print("该账号为私密账号，需要使用登录后的 Cookie，且登录的账号需要关注该私密账号")
                        finished = True
                    else:
                        cursor = data['max_cursor']
                        all_data_list.extend(data_list)
                        finished = not data["has_more"]
            except Exception as e:
                print(f"error: {e}")
                finished = True
        return all_data_list

    def run(self, share_url):
        self.share_url = share_url
        location = self.get_location()
        if not location:
            print('location not found')
            return
        vid = re.findall(r'/share/video/(\d*)', location)
        if vid:
            detail = self.get_detail(vid[0])
            if detail:
                return detail
        sids = re.findall(r'/user/(\w*)', location)
        if sids:
            detail = self.get_account_data(sids[0])
            return {
                "data": detail,
                "status_code": 0 if detail else -1,
            }
        return None
