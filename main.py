from PIL import Image, ImageDraw
import hashlib


user_name = input('[>] User name: ')
name_md5 = hashlib.md5(user_name.encode()).hexdigest()
raw_rgb = [name_md5[i:i+10] for i in range(0, 30, 10)]
main_color = tuple([int(i, base=16) % 255 for i in raw_rgb])
background_color = '#808080'

avatar_matrix = []
bits = list(bin(int(name_md5, base=16))[2:])
cnt = 0
for i in range(12):
	avatar_matrix.append([])
	for j in range(6):
		avatar_matrix[i].append(bits[cnt])
		cnt += 1
	avatar_matrix[i].extend(avatar_matrix[i][::-1])


for i in avatar_matrix:
	i.insert(0, '0')
	i.append('0')
avatar_matrix.insert(0, ['0']*14)
avatar_matrix.append(['0']*14)


im = Image.new('RGB', (14, 14), background_color)
draw = ImageDraw.Draw(im)

for i in range(14):
	for j in range(14):
		if int(avatar_matrix[i][j]):
			draw.point((j,i), main_color)

im.save(f'{user_name}.png', quality=100)
