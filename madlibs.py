
def main():
	# attempt to validate using function
	'''	def string_validation(input):
			while True:
				try:
					str(input)
				except ValueError:
					print('That doesn\t work!')
				else:
					break

		def emotion():
			value = str(input('Enter an Emotion: '))
			return value

		string_validation(emotion())'''


	emotion = str(input('Enter an Emotion: '))
	food = str(input('Enter your favorite food: '))
	family = str(input('Enter a family members\' name: '))
	time = int(input('Enter a number from 0 to 24: '))

	print(f'\n I woke up feeling {emotion}, i went to the kitchen to eat some leftover {food}')
	if time < 18 and time >= 4:
		print(f'when {family} looked at me with shock. I then relized that it was {time} o\'clock, and I had eaten before futoor ')
	elif time >= 18 or time < 4:
		print(f'when I looked at the time and realized it was {time} o\'clock and I had slept all day long')

if __name__ == '__main__':
	main()