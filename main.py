
import urllib.request
from bs4 import BeautifulSoup

print( '\n< 1달간 검색 >\n')
url_dic = {
  '내한':'https://search.naver.com/search.naver?sm=tab_opt&where=nexearch&query=%EB%82%B4%ED%95%9C&oquery=%EB%82%B4%ED%95%9C&tqi=UrZfzwp0JXVssu%2BA4rKssssstJw-178383&nso=so%3Ar%2Cp%3A1m%2Ca%3Aall'
  ,
  '박솔뫼': "https://search.naver.com/search.naver?sm=tab_opt&where=nexearch&query=%EB%B0%95%EC%86%94%EB%AB%BC&oquery=%EB%B0%95%EC%86%94%EB%AB%BC&tqi=UrZbisp0YiRssUCa%2FylssssstI8-139800&nso=so%3Ar%2Cp%3A1m%2Ca%3Aall"
  ,
  '김사과': "https://search.naver.com/search.naver?where=post&query=%EA%B9%80%EC%82%AC%EA%B3%BC&st=sim&sm=tab_opt&date_from=20030520&date_to=20200505&date_option=4&srchby=all&dup_remove=1&post_blogurl=&post_blogurl_without=&nso=so%3Ar%2Ca%3Aall%2Cp%3A1m"
  ,
  '황정은': "https://search.naver.com/search.naver?sm=tab_opt&where=nexearch&query=%ED%99%A9%EC%A0%95%EC%9D%80&oquery=%ED%99%A9%EC%A0%95%EC%9D%80&tqi=UrZZzwp0JXossZkeO5ossssssx4-334904&nso=so%3Ar%2Cp%3A1m%2Ca%3Aall"
  ,
  '장강명': "https://search.naver.com/search.naver?sm=tab_opt&where=nexearch&query=%EC%9E%A5%EA%B0%95%EB%AA%85&oquery=%EC%9E%A5%EA%B0%95%EB%AA%85&tqi=UrZb5sp0J14ssujm49NssssstGl-072842&nso=so%3Ar%2Cp%3A1m%2Ca%3Aall"
}
for ii in url_dic:
  print(ii)
# 1-month

for i_dic in url_dic:
  print("\n[키워드]: "+i_dic)
  url = url_dic.get(i_dic)
  html = urllib.request.urlopen(url).read()
  soup = BeautifulSoup(html, 'html.parser')
  
  #title = soup.find_all(class_ = 'sh_blog_title') # blog only
  title = soup.find_all(class_ = '_sp_each_title') # all data
  
  #print(soup)
  #date = soup.find_all(class_ ='txt_inline')
  #print(date)
  
  for j, j_t in enumerate(title):
    print(str(j+1)+'\n'+j_t.attrs['title']+'\n'+j_t.attrs['href'])