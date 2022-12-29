import re


def extract_date(url):
    return re.findall(r'(\d{4})-(\d{1,2})-(\d{1,2})', url)


url1 = url = 'https://www.vrbo.com/el-gr/%CE%B5%CE%BD%CE%BF%CE%B9%CE%BA%CE%B9%CE%AC%CF%83%CE%B5%CE%B9%CF%82-%CE%B5%CE%BE%CE%BF%CF%87%CE%B9%CE%BA%CF%8E%CE%BD-%CE%BA%CE%B1%CF%84%CE%BF%CE%B9%CE%BA%CE%B9%CF%8E%CE%BD/p436144?adultsCount=2&arrival=2021-05-08&departure=2021-05-16'
print(extract_date(url1))