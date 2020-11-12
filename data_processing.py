from bs4 import BeautifulSoup
import json
def html_data_processing(html_data,number_of_data,counter):
    
    soup = BeautifulSoup(html_data,'lxml')
    outer_div_tag = soup.find("div", { "id" : "example_wrapper" })
    heading = outer_div_tag.find('thead').find("tr")
    heading_element_list = heading.find_all("th")
    head = [heading_element.text.strip() for heading_element in heading_element_list]
    head = head[:3]
    table_body=outer_div_tag.find('tbody')
    rows = table_body.find_all('tr')
    output = {}
    number_of_data-=len(rows)
    counter = counter
    
    for row in rows:
        cols=row.find_all('td')
        cols=[elements.text.strip() for elements in cols]
        cols = cols[:3]
        dicta = dict(zip(head,cols))
        output[counter] = dicta
        counter+=1
        
    if number_of_data<=0:
        return [output,number_of_data,False,counter]
    
    return [output,number_of_data,True,counter]
    
