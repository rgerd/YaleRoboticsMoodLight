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
    if emotion[0] = 'pos':
        color=60 #yellow

    #white = neutral
    if emotion[0] = 'neutral':
        color=0 #white

    #green=disgust
    if emotion[0] = 'negative':
        color=120 #green
        
    else:
        color=0
    
    return {"hue": color, "saturation": 1.0, "lightness": emotion[1]}

