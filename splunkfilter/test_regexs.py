import re
from datetime import datetime

import pytest

from .regexs import www_single


@pytest.fixture
def web_server_lines():
    return (
        '209.160.24.63 - - [28/Mar/2023:18:22:16] "GET /product.screen?productId=WC-SH-A02&JSESSIONID=SD0SL6FF7ADFF4953 HTTP 1.1" 200 3878 "http://www.google.com" "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.46 Safari/536.5" 349\n'
        '209.160.24.63 - - [28/Mar/2023:18:22:16] "POST /oldlink?itemId=EST-6&JSESSIONID=SD0SL6FF7ADFF4953 HTTP 1.1" 200 1748 "http://www.buttercupgames.com/oldlink?itemId=EST-6" "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.46 Safari/536.5" 731\n'
    )


def test_web_server_regex(web_server_lines):
    matches = re.finditer(www_single, web_server_lines)

    for matchNum, match in enumerate(matches, start=1):
        if matchNum == 1:
            assert match["client_ip"] == "209.160.24.63"

            datetime_str = match["timestamp"]
            date_format = "%d/%b/%Y:%H:%M:%S"
            datetime_object = datetime.strptime(datetime_str, date_format)
            assert datetime_object

            assert match["request_method"] == "GET"
            assert (
                match["request_uri"]
                == "/product.screen?productId=WC-SH-A02&JSESSIONID=SD0SL6FF7ADFF4953"
            )
            assert match["protocol"] == "HTTP"
            assert match["protocol_version"] == "1.1"
            assert match["status"] == "200"
            assert match["response_size"] == "3878"
            assert match["referrer"] == "http://www.google.com"
            assert (
                match["user_agent"]
                == "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.46 Safari/536.5"
            )
