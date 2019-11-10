
# This is a smart calculator
# Code by Surya Prakash Giri

print('\n     ------------------------------------------------------------------')
print('     |                  Welcome to the mini calculator                |')
print('     |                                 Code By : SURYA                |')
print('     ------------------------------------------------------------------\n')

print("\nEnter the expression or type 'exit' to exit :",end=' ')
exp = input()
result = eval(exp)
print(result,end='')
res = result
while(True):
	x = input()
	if x=='exit':
		print('\nThank You for using....\n')
		exit(0)
	new_exp = str(res) + x
	res = eval(new_exp)
	print(res,end='')
