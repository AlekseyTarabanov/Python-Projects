import requests
import json
import numpy as np 
import matplotlib.pyplot as plt
import main

def check_ip_adress():
	Ip_adress = open('in.txt')
	count = 0
	count_city = main.mydefaultdict(int)
	count_region = main.mydefaultdict(int)
	count_country = main.mydefaultdict(int)
	session = requests.Session()
	for ip in Ip_adress.readlines():
		count += 1
		
		Link = "https://ipinfo.io/"+ str.lstrip(ip) +"/json?token=4215dc1507280d"
		response = session.get(Link)
		data = response.json()
				
		if 'city' in data:
			city = data['city']
		if 'region' in data:
			region = data['region']
		if 'country' in data:	
			country = data['country']
			
		count_city[city] += 1
		count_region[region] += 1
		count_country[country] += 1
		
		print('Номер: ', count)
		print('Ip адресс: ', str.lstrip(ip))
		print('Город: ', city)
		print('Регион: ', region)
		print('Страна: ', country, '\n')
		print('-----------------------')
		
	fig = plt.figure()
	ax_country = fig.add_subplot(1,3,1)
	ax_city = fig.add_subplot(1,3,2)
	ax_region = fig.add_subplot(1,3,3)
	vals_country, name_country = [], []
	vals_city, name_city = [], []
	vals_region, name_region = [], []
	for k, v  in count_country.items():
		vals_country.append(v)
		name_country.append(k)
		
	for k, v  in count_city.items():
		vals_city.append(v)
		name_city.append(k)
		
	for k, v  in count_region.items():
		vals_region.append(v)
		name_region.append(k)
		
		
	ax_country.set(title = 'Страны')
	ax_country.pie(vals_country,
		shadow=False,
		startangle=90,)
		
	ax_city.set(title = 'Города')
	ax_city.pie(vals_city,
		shadow=False,
		startangle=90,)

	ax_region.set(title = 'Регионы')
	ax_region.pie(vals_region,
		shadow=False,
		startangle=90,)
			
	ax_country.legend(labels=name_country, title = 'Страны', loc = 'upper left', shadow = True, fontsize = 10, ncol = 1, bbox_to_anchor=(0.3, 0.1))
	ax_city.legend(labels=name_city, title = 'Города', loc = 'upper right', shadow = True, fontsize = 10, ncol = 3, bbox_to_anchor=(1.25, 0.1))
	ax_region.legend(labels=name_region,title = 'Регионы', loc = 'upper left', shadow = True, fontsize = 10, ncol = 2, bbox_to_anchor=(0.1, 0.1))
	plt.show()

if __name__ == '__main__':
	check_ip_adress()
