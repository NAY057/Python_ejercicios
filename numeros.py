
def main():
	with open('escribir_num.txt', 'w') as f:
		for i in range(1000000001):
			
			f.write(str(i) + ' ')


if __name__ == '__main__':
	main()