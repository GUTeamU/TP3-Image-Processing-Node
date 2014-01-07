from PIL import Image, ImageFilter

im = Image.open("Testface.jpg")
im = im.filter(ImageFilter.ModeFilter(6)).filter(ImageFilter.SMOOTH_MORE).filter(ImageFilter.FIND_EDGES).filter(ImageFilter.SMOOTH_MORE)
im = im.point()
im.save("convert.jpg")

#.filter(ImageFilter.ModeFilter(6))
#.filter(ImageFilter.FIND_EDGES)
#.filter(ImageFilter.Kernel( (3,3), (2,2,2,2,6,2,2,2,2) ))

# 1,1,1,1,1,
# 1,2,2,2,1,
# 1,2,0,2,1,
# 1,2,2,2,1,
# 1,1,1,1,1