label definitions:
    # this is where we'll set up the image composites for each character.
    # remember, we'll do it like DDLC. each image will have three parts, right?
    # naming conventions
    #       char    pose/expression im.Composite((sprite size), (offset), (image), (offset) etc)
    # image sayori 1a = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/a.png")


    #Cassandra
    


    #transforms will be used to animate and position characters. Beecause we're using a gui with a limited window, there can only be a few positions. Left-front, center front, right front, and backs. 

    #we need to determine what types of transforms we need.  The hop from DDLC is nice and all, but ot doesn't really fit the tone. Valhalla's much closer, not a lot of transforms needed. 

    transform tfade(x = 640, z = 1.0):
        on show:
            xcenter x yoffset 0 yanchor 1.0 ypos 1.00 zoom z*1.00 alpha 0.0 subpixel True
            easein .5 alpha 1.00
        on hide:
            xcenter x yoffset 0 yanchor 1.0 ypos 1.00 zoom z*1.00 alpha 1.0 subpixel True
            easein .5 alpha 0.00

    transform tFromLeft(x = 640, z = 1.0):
        on show:
            xcenter x xoffset -600 yanchor 1.0 ypos 1.00 zoom z*1.00 alpha 1.0 subpixel True
            easein .5 xoffset 0
        on hide:
            xcenter x xoffset 0 yanchor 1.0 ypos 1.00 zoom z*1.00 alpha 1.0 subpixel True
            easein .5 xoffset -600

    transform tFromRight(x = 640, z = 1.0):
        on show:
            xcenter x xoffset 1200 yanchor 1.0 ypos 1.00 zoom z*1.00 alpha 1.0 subpixel True
            easein .5 xoffset 0
        on hide:
            xcenter x xoffset 0 yanchor 1.0 ypos 1.00 zoom z*1.00 alpha 1.0 subpixel True
            easein .5 xoffset 1200

    transform moveTo(x = 640, z = 1.0):
        on replace:
            easein 0.5 xcenter x

    # position with transform takes the first letter of the transform and applies it to a row and position. the argument is the x position. will have to work out what those are. only two can ever be back row.
    # note zorder can't be set with transform. gotta do it in script. shit.

    init python:
        spriteXLeft = 350
        spriteXCenter = 600
        spriteXRight = 850
        spriteBLeft = 500
        spriteBRight = 700
        #note default z is 0.8. trying to position chars behind each other.

    # fades
    transform f11:
        tfade(spriteXLeft)
    transform f12:
        tfade(spriteXCenter)
    transform f13:
        tfade(spriteXRight)
    transform f21:
        tfade(spriteBLeft)
    transform f22:
        tfade(spriteBRight)

    # from lefts
    transform fl11:
        tFromLeft(spriteXLeft)
    transform fl12:
        tFromLeft(spriteXCenter)
    transform fl13:
        tFromLeft(spriteXRight)
    transform fl21:
        tFromLeft(spriteBLeft)
    transform fl22:
        tFromLeft(spriteBRight)
    
    # place to place (move to position)
    transform mt3:
        moveTo(spriteXRight)
    transform mt2:
        moveTo(spriteXCenter)
    transform mt1:
        moveTo(spriteXLeft)


    # from rights
    transform fr11:
        tFromRight(spriteXLeft)
    transform fr12:
        tFromRight(spriteXCenter)
    transform fr13:
        tFromRight(spriteXRight)
    transform fr21:
        tFromRight(spriteBLeft)
    transform fr22:
        tFromRight(spriteBRight)



#------------------------------------------------------------------------------
# Image composites for sprites. They will be made up of a pose and a head. 1a = pose one, head a. temporarily just using placeholders

# image c 1a = im.Composite((960, 960), (0, 0), "charHead.png", (0, 0), "charBody.png")

# note only a few poses. maybe two.
#1 standard 2 arm crossed 3 major emotion

# heads list:
#     a normal
#     b sad
#     c heartbroken
#     d mad
#     e supermad
#     f sick
#     g disappointed
#     h suprised
#     i scared
#     j smug
#     k annoyed
#     l excited
#     m happy
#     n superhappy
#     o speak
#     p shy
#     q sheepish
#     r puzzled
#     s listening
#     t aroused? I guess?
#     u flirty/teasing


