import re

www_single = r"(?P<client_ip>[\d.]+) - - \[(?P<timestamp>.*?)\] \"(?P<request_method>\w+) (?P<request_uri>.*?) (?P<protocol>.*?) (?P<protocol_version>.*?)\" (?P<status>\d+) (?P<response_size>\d+|-) \"(?P<referrer>.*?)\" \"(?P<user_agent>.*?)\""
