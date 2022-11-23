def visitors():
	counter_read_file = open("count.txt", "r")
	visitors_count = int(counter_read_file.read())
	counter_read_file.close()

	visitors_count = visitors_count + 1


	counter_write_file = open("count.txt", "w")
	counter_write_file.write(str(visitors_count))
	counter_write_file.close()

	print('Total visitors : ', visitors_count)

    visitors()


def covid_stats():

	country_code = input('Enter country name:')

	corona_data = 'https://covid-api-262.herokuapp.com/?country='+country_code
	print(corona_data)

covid_stats()