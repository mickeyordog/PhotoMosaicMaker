from PIL import Image, ImageChops


output_length = 2048
output_size = (output_length, output_length)
pics_per_row = 128
pic_length = int(output_length / pics_per_row)

# img = Image.open('./images/img1.png')
img = Image.open('./images/oranges.jpg')
output = img.resize(output_size)


def find_average_color(image, x_pos, y_pos, size):
    sum_r = 0
    sum_g = 0
    sum_b = 0
    for x in range(size):
        for y in range(size):
            pixel = image.getpixel((x_pos + x, y_pos + y))
            sum_r += pixel[0]
            sum_g += pixel[1]
            sum_b += pixel[2]
    sq_size = size * size
    avg_color = (sum_r // sq_size, sum_g // sq_size, sum_b // sq_size)
    return avg_color


for i in range(pics_per_row):
    for j in range(pics_per_row):
        x = i * pic_length
        y = j * pic_length
        # img.paste(find_average_color(output, x, y, pic_length), (x, y, x + pic_length, y + pic_length))
        avg_color = find_average_color(output, x, y, pic_length)
        to_paste = img.resize((pic_length, pic_length)).convert('RGB')
        to_paste = ImageChops.multiply(to_paste, Image.new('RGB', to_paste.size, avg_color))
        output.paste(to_paste, (x, y, x + pic_length, y + pic_length))

output.show()



