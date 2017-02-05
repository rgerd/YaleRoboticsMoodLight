# This method turns an emotion (a tuple with a string and a double) into a color.
# For now, the only possible values for the string in emotion are "pos", "neg",
# and "neutral," with the double representing the magnitude of that emotion, from
# 0.0 (least intense) to 1.0 (most intense).
# For example:
#   emotionToColor(("pos", 0.5))
# Could return:
#   "yellow"
# Try to use both the label (pos/neg/neutral) as well as the magnitude to pick
# a color. Inspiration: http://www.w3schools.com/colors/colors_names.asp
def emotionToColor(emotion):

    #yellow = joy
    if emotion[0] == 'pos':
        color=0 #red

    #green=disgust
    if emotion[0] == 'negative':
        color=225 #blue

    else:
        color=60 #neutral or anything else: color will be yellow

    # 0 < mag < 1
    # 1 < lightness < .5
    lightness = 1 - .5(emotion[1]);

    import colorsys
    rgbval = colorsys.hls_to_rgb(color/360, lightness, 1.0)
