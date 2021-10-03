import help

Test = help.test()

def domain_name(url):
    return url.split('/')[2].replace('www.','').split('.')[0] if url.startswith('http') else url.replace('www.','').split('.')[0]

Test.assert_equals(domain_name("http://google.com"), "google")
Test.assert_equals(domain_name("http://google.co.jp"), "google")
Test.assert_equals(domain_name("www.xakep.ru"), "xakep")
Test.assert_equals(domain_name("https://youtube.com"), "youtube")
