from PIL import Image, ImageFilter, ImageOps

def pixel(i):
	if(i<=20):
		print "lowers"
		return 0
	else:
		print "highers"
		return 256


im = Image.open("Testface.jpg")
im = im.filter(ImageFilter.ModeFilter(8))
im = im.filter(ImageFilter.GaussianBlur(2))
# im = im.point(lambda i: i*3)
# im = im.filter(ImageFilter.GaussianBlur(3))
# im = im.filter(ImageFilter.UnsharpMask(150,2,30))
# im = im.filter(ImageFilter.SMOOTH_MORE)
im = im.filter(ImageFilter.FIND_EDGES)
# im = im.filter(ImageFilter.SMOOTH_MORE)
# im = im.filter(ImageFilter.GaussianBlur(2))

# im = im.filter(ImageFilter.SHARPEN)
im = ImageOps.grayscale(im)
im = im.point(lambda i: i*3)
# im = im.filter(ImageFilter.Kernel( (3,3), (1,1,1,1,0,1,1,1,1) ))
# im = im.filter(ImageFilter.Kernel( (5,5), (1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1) ))
# im = im.filter(ImageFilter.Kernel( (5,5), (1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1) ))
# im = im.point(lambda i: i*2)
# im = im.filter(ImageFilter.Kernel( (5,5), (1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1) ))
# im = im.filter(ImageFilter.FIND_EDGES)
# im = im.filter(ImageFilter.GaussianBlur(2))
# im = im.filter(ImageFilter.SHARPEN)
# im = im.filter(ImageFilter.UnsharpMask(150,2,30))

#im = im.
#im = im.point(pixel)
im.save("convert2.jpg")

#.filter(ImageFilter.ModeFilter(6))
#.filter(ImageFilter.FIND_EDGES)
#.filter(ImageFilter.Kernel( (3,3), (2,2,2,2,6,2,2,2,2) ))
#ImageFilter.GaussianBlur()

# 1,1,1,1,1,
# 1,1,1,1,1,
# 1,1,0,1,1,
# 1,1,1,1,1,
# 1,1,1,1,1