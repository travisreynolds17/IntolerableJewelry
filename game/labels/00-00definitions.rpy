label definitions:
    


    #transforms will be used to animate and position characters. Beecause we're using a gui with a limited window, there can only be a few positions. Left-front, center front, right front, and backs. 

    #we need to determine what types of transforms we need.  The hop from DDLC is nice and all, but ot doesn't really fit the tone. Valhalla's much closer, not a lot of transforms needed. 

    transform textFade(x = 640, y = 200, z = 1.0):
        on show:
            xcenter x ycenter y yoffset 0 ypos y zoom z*1.00 alpha 0.0 subpixel True
            easein .5 alpha 1.00
        on replace:
            xcenter x ycenter y yoffset 0 ypos y zoom z*1.00 alpha 0.0 subpixel True
            easein .5 alpha 1.00
        on hide:
            xcenter x yoffset 0 yanchor 1.0 ypos 1.00 zoom z*1.00 alpha 1.0 subpixel True
            easein .5 alpha 0.00

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

    transform kissZoom(x = 640):
        on show:
            alpha 0.0 zoom 1.0 xcenter 0 yanchor 1.0 subpixel True
            easein 0.5 zoom 5.0
        on hide:
            zoom 5.0 alpha 1.0
            easeout 0.5 zoom 1.0 alpha 0.0

    transform tInstant(x = 640, z = 1.0):
        on show:
            xcenter x yoffset 0 yanchor 1.0 ypos 1.00 zoom z*1.00 alpha 1.0 subpixel True
            
        on hide:
            xcenter x yoffset 0 yanchor 1.0 ypos 1.00 zoom z*1.00 alpha 0.0 subpixel True
            

    # position with transform takes the first letter of the transform and applies it to a row and position. the argument is the x position. will have to work out what those are. only two can ever be back row.
    # note zorder can't be set with transform. gotta do it in script. shit.

    init python:
        spriteXLeft = 350
        spriteXCenter = 600
        spriteXRight = 850
        spriteBLeft = 500
        spriteBRight = 700
        
        #note argument z is used to control zoom, not zorder.

        #text xy is coordinates for floating text points, like Hisao's opening monologue in KS. to be used with transforms. calling it monoTextXY bc textXY is used somewhere else.

        monoTextSpacing = 150
        monoTextX = 250
        monoTextY = [
            100, 200, 300, 400, 500, 600
        ]
        yPosMax = len(monoTextY)

    default monoText1 = ""
    default monoText2 = ""
    default monoText3 = ""
    default monoText4 = ""
    default monoText5 = ""
    default monoText6 = ""
    default monoText7 = ""

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

    #instant
    transform i11:
        tInstant(spriteXLeft)
    transform i12:
        tInstant(spriteXCenter)
    transform i13:
        tInstant(spriteXRight)
    transform i21:
        tInstant(spriteBLeft)
    transform i22:
        tInstant(spriteBRight)

    # kiss zoom
    transform kiss12:
        kissZoom(spriteXCenter)

    
    



#------------------------------------------------------------------------------
# Image composites for sprites. They will be made up of a pose and a head. 1a = pose one, head a. temporarily just using placeholders

# image c 1a = im.Composite((371, 1004), (0, 215), "chars/charHead.png", (0, 500), "chars/charBody.png")

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


#cassandra composite images

    image c 1a = im.Composite((371, 1004), (0, 215), "chars/ca.png", (0, 500), "chars/c1.png")
    image c 1b = im.Composite((371, 1004), (0, 215), "chars/cb.png", (0, 500), "chars/c1.png")
    image c 1c = im.Composite((371, 1004), (0, 215), "chars/cc.png", (0, 500), "chars/c1.png")
    image c 1d = im.Composite((371, 1004), (0, 215), "chars/cd.png", (0, 500), "chars/c1.png")
    image c 1e = im.Composite((371, 1004), (0, 215), "chars/ce.png", (0, 500), "chars/c1.png")
    image c 1f = im.Composite((371, 1004), (0, 215), "chars/cf.png", (0, 500), "chars/c1.png")
    image c 1g = im.Composite((371, 1004), (0, 215), "chars/cg.png", (0, 500), "chars/c1.png")
    image c 1h = im.Composite((371, 1004), (0, 215), "chars/ch.png", (0, 500), "chars/c1.png")
    image c 1i = im.Composite((371, 1004), (0, 215), "chars/ci.png", (0, 500), "chars/c1.png")
    image c 1j = im.Composite((371, 1004), (0, 215), "chars/cj.png", (0, 500), "chars/c1.png")
    image c 1k = im.Composite((371, 1004), (0, 215), "chars/ck.png", (0, 500), "chars/c1.png")
    image c 1l = im.Composite((371, 1004), (0, 215), "chars/cl.png", (0, 500), "chars/c1.png")
    image c 1m = im.Composite((371, 1004), (0, 215), "chars/cm.png", (0, 500), "chars/c1.png")
    image c 1n = im.Composite((371, 1004), (0, 215), "chars/cn.png", (0, 500), "chars/c1.png")
    image c 1o = im.Composite((371, 1004), (0, 215), "chars/co.png", (0, 500), "chars/c1.png")
    image c 1p = im.Composite((371, 1004), (0, 215), "chars/cp.png", (0, 500), "chars/c1.png")
    image c 1q = im.Composite((371, 1004), (0, 215), "chars/cq.png", (0, 500), "chars/c1.png")
    image c 1r = im.Composite((371, 1004), (0, 215), "chars/cr.png", (0, 500), "chars/c1.png")
    image c 1s = im.Composite((371, 1004), (0, 215), "chars/cs.png", (0, 500), "chars/c1.png")
    image c 1t = im.Composite((371, 1004), (0, 215), "chars/ct.png", (0, 500), "chars/c1.png")
    image c 1u = im.Composite((371, 1004), (0, 215), "chars/cu.png", (0, 500), "chars/c1.png")

# robin composite images

    image r 1a = im.Composite((371, 1004), (0, 215), "chars/rca.png", (0, 500), "chars/rc1.png")
    image r 1b = im.Composite((371, 1004), (0, 215), "chars/rcb.png", (0, 500), "chars/rc1.png")
    image r 1c = im.Composite((371, 1004), (0, 215), "chars/rcc.png", (0, 500), "chars/rc1.png")
    image r 1d = im.Composite((371, 1004), (0, 215), "chars/rcd.png", (0, 500), "chars/rc1.png")
    image r 1e = im.Composite((371, 1004), (0, 215), "chars/rce.png", (0, 500), "chars/rc1.png")
    image r 1f = im.Composite((371, 1004), (0, 215), "chars/rcf.png", (0, 500), "chars/rc1.png")
    image r 1g = im.Composite((371, 1004), (0, 215), "chars/rcg.png", (0, 500), "chars/rc1.png")
    image r 1h = im.Composite((371, 1004), (0, 215), "chars/rch.png", (0, 500), "chars/rc1.png")
    image r 1i = im.Composite((371, 1004), (0, 215), "chars/rci.png", (0, 500), "chars/rc1.png")
    image r 1j = im.Composite((371, 1004), (0, 215), "chars/rcj.png", (0, 500), "chars/rc1.png")
    image r 1k = im.Composite((371, 1004), (0, 215), "chars/rck.png", (0, 500), "chars/rc1.png")
    image r 1l = im.Composite((371, 1004), (0, 215), "chars/rcl.png", (0, 500), "chars/rc1.png")
    image r 1m = im.Composite((371, 1004), (0, 215), "chars/rcm.png", (0, 500), "chars/rc1.png")
    image r 1n = im.Composite((371, 1004), (0, 215), "chars/rcn.png", (0, 500), "chars/rc1.png")
    image r 1o = im.Composite((371, 1004), (0, 215), "chars/rco.png", (0, 500), "chars/rc1.png")
    image r 1p = im.Composite((371, 1004), (0, 215), "chars/rcp.png", (0, 500), "chars/rc1.png")
    image r 1q = im.Composite((371, 1004), (0, 215), "chars/rcq.png", (0, 500), "chars/rc1.png")
    image r 1r = im.Composite((371, 1004), (0, 215), "chars/rcr.png", (0, 500), "chars/rc1.png")
    image r 1s = im.Composite((371, 1004), (0, 215), "chars/rcs.png", (0, 500), "chars/rc1.png")
    image r 1t = im.Composite((371, 1004), (0, 215), "chars/rct.png", (0, 500), "chars/rc1.png")
    image r 1u = im.Composite((371, 1004), (0, 215), "chars/rcu.png", (0, 500), "chars/rc1.png")

# lichelle composite images

    image l 1a = im.Composite((371, 1004), (0, 215), "chars/lca.png", (0, 500), "chars/lc1.png")
    image l 1b = im.Composite((371, 1004), (0, 215), "chars/lcb.png", (0, 500), "chars/lc1.png")
    image l 1c = im.Composite((371, 1004), (0, 215), "chars/lcc.png", (0, 500), "chars/lc1.png")
    image l 1d = im.Composite((371, 1004), (0, 215), "chars/lcd.png", (0, 500), "chars/lc1.png")
    image l 1e = im.Composite((371, 1004), (0, 215), "chars/lce.png", (0, 500), "chars/lc1.png")
    image l 1f = im.Composite((371, 1004), (0, 215), "chars/lcf.png", (0, 500), "chars/lc1.png")
    image l 1g = im.Composite((371, 1004), (0, 215), "chars/lcg.png", (0, 500), "chars/lc1.png")
    image l 1h = im.Composite((371, 1004), (0, 215), "chars/lch.png", (0, 500), "chars/lc1.png")
    image l 1i = im.Composite((371, 1004), (0, 215), "chars/lci.png", (0, 500), "chars/lc1.png")
    image l 1j = im.Composite((371, 1004), (0, 215), "chars/lcj.png", (0, 500), "chars/lc1.png")
    image l 1k = im.Composite((371, 1004), (0, 215), "chars/lck.png", (0, 500), "chars/lc1.png")
    image l 1l = im.Composite((371, 1004), (0, 215), "chars/lcl.png", (0, 500), "chars/lc1.png")
    image l 1m = im.Composite((371, 1004), (0, 215), "chars/lcm.png", (0, 500), "chars/lc1.png")
    image l 1n = im.Composite((371, 1004), (0, 215), "chars/lcn.png", (0, 500), "chars/lc1.png")
    image l 1o = im.Composite((371, 1004), (0, 215), "chars/lco.png", (0, 500), "chars/lc1.png")
    image l 1p = im.Composite((371, 1004), (0, 215), "chars/lcp.png", (0, 500), "chars/lc1.png")
    image l 1q = im.Composite((371, 1004), (0, 215), "chars/lcq.png", (0, 500), "chars/lc1.png")
    image l 1r = im.Composite((371, 1004), (0, 215), "chars/lcr.png", (0, 500), "chars/lc1.png")
    image l 1s = im.Composite((371, 1004), (0, 215), "chars/lcs.png", (0, 500), "chars/lc1.png")
    image l 1t = im.Composite((371, 1004), (0, 215), "chars/lct.png", (0, 500), "chars/lc1.png")
    image l 1u = im.Composite((371, 1004), (0, 215), "chars/lcu.png", (0, 500), "chars/lc1.png")

# tania composite images

    image t 1a = im.Composite((371, 1004), (0, 215), "chars/tca.png", (0, 500), "chars/tc1.png")
    image t 1b = im.Composite((371, 1004), (0, 215), "chars/tcb.png", (0, 500), "chars/tc1.png")
    image t 1c = im.Composite((371, 1004), (0, 215), "chars/tcc.png", (0, 500), "chars/tc1.png")
    image t 1d = im.Composite((371, 1004), (0, 215), "chars/tcd.png", (0, 500), "chars/tc1.png")
    image t 1e = im.Composite((371, 1004), (0, 215), "chars/tce.png", (0, 500), "chars/tc1.png")
    image t 1f = im.Composite((371, 1004), (0, 215), "chars/tcf.png", (0, 500), "chars/tc1.png")
    image t 1g = im.Composite((371, 1004), (0, 215), "chars/tcg.png", (0, 500), "chars/tc1.png")
    image t 1h = im.Composite((371, 1004), (0, 215), "chars/tch.png", (0, 500), "chars/tc1.png")
    image t 1i = im.Composite((371, 1004), (0, 215), "chars/tci.png", (0, 500), "chars/tc1.png")
    image t 1j = im.Composite((371, 1004), (0, 215), "chars/tcj.png", (0, 500), "chars/tc1.png")
    image t 1k = im.Composite((371, 1004), (0, 215), "chars/tck.png", (0, 500), "chars/tc1.png")
    image t 1l = im.Composite((371, 1004), (0, 215), "chars/tcl.png", (0, 500), "chars/tc1.png")
    image t 1m = im.Composite((371, 1004), (0, 215), "chars/tcm.png", (0, 500), "chars/tc1.png")
    image t 1n = im.Composite((371, 1004), (0, 215), "chars/tcn.png", (0, 500), "chars/tc1.png")
    image t 1o = im.Composite((371, 1004), (0, 215), "chars/tco.png", (0, 500), "chars/tc1.png")
    image t 1p = im.Composite((371, 1004), (0, 215), "chars/tcp.png", (0, 500), "chars/tc1.png")
    image t 1q = im.Composite((371, 1004), (0, 215), "chars/tcq.png", (0, 500), "chars/tc1.png")
    image t 1r = im.Composite((371, 1004), (0, 215), "chars/tcr.png", (0, 500), "chars/tc1.png")
    image t 1s = im.Composite((371, 1004), (0, 215), "chars/tcs.png", (0, 500), "chars/tc1.png")
    image t 1t = im.Composite((371, 1004), (0, 215), "chars/tct.png", (0, 500), "chars/tc1.png")
    image t 1u = im.Composite((371, 1004), (0, 215), "chars/tcu.png", (0, 500), "chars/tc1.png")

# second poses

    #cassandra composite images

    image c 2a = im.Composite((371, 1004), (0, 215), "chars/ca.png", (0, 500), "chars/c1.png")
    image c 2b = im.Composite((371, 1004), (0, 215), "chars/cb.png", (0, 500), "chars/c1.png")
    image c 2c = im.Composite((371, 1004), (0, 215), "chars/cc.png", (0, 500), "chars/c1.png")
    image c 2d = im.Composite((371, 1004), (0, 215), "chars/cd.png", (0, 500), "chars/c1.png")
    image c 2e = im.Composite((371, 1004), (0, 215), "chars/ce.png", (0, 500), "chars/c1.png")
    image c 2f = im.Composite((371, 1004), (0, 215), "chars/cf.png", (0, 500), "chars/c1.png")
    image c 2g = im.Composite((371, 1004), (0, 215), "chars/cg.png", (0, 500), "chars/c1.png")
    image c 2h = im.Composite((371, 1004), (0, 215), "chars/ch.png", (0, 500), "chars/c1.png")
    image c 2i = im.Composite((371, 1004), (0, 215), "chars/ci.png", (0, 500), "chars/c1.png")
    image c 2j = im.Composite((371, 1004), (0, 215), "chars/cj.png", (0, 500), "chars/c1.png")
    image c 2k = im.Composite((371, 1004), (0, 215), "chars/ck.png", (0, 500), "chars/c1.png")
    image c 2l = im.Composite((371, 1004), (0, 215), "chars/cl.png", (0, 500), "chars/c1.png")
    image c 2m = im.Composite((371, 1004), (0, 215), "chars/cm.png", (0, 500), "chars/c1.png")
    image c 2n = im.Composite((371, 1004), (0, 215), "chars/cn.png", (0, 500), "chars/c1.png")
    image c 2o = im.Composite((371, 1004), (0, 215), "chars/co.png", (0, 500), "chars/c1.png")
    image c 2p = im.Composite((371, 1004), (0, 215), "chars/cp.png", (0, 500), "chars/c1.png")
    image c 2q = im.Composite((371, 1004), (0, 215), "chars/cq.png", (0, 500), "chars/c1.png")
    image c 2r = im.Composite((371, 1004), (0, 215), "chars/cr.png", (0, 500), "chars/c1.png")
    image c 2s = im.Composite((371, 1004), (0, 215), "chars/cs.png", (0, 500), "chars/c1.png")
    image c 2t = im.Composite((371, 1004), (0, 215), "chars/ct.png", (0, 500), "chars/c1.png")
    image c 2u = im.Composite((371, 1004), (0, 215), "chars/cu.png", (0, 500), "chars/c1.png")

# robin composite images

    image r 2a = im.Composite((371, 1004), (0, 215), "chars/rca.png", (0, 500), "chars/rc1.png")
    image r 2b = im.Composite((371, 1004), (0, 215), "chars/rcb.png", (0, 500), "chars/rc1.png")
    image r 2c = im.Composite((371, 1004), (0, 215), "chars/rcc.png", (0, 500), "chars/rc1.png")
    image r 2d = im.Composite((371, 1004), (0, 215), "chars/rcd.png", (0, 500), "chars/rc1.png")
    image r 2e = im.Composite((371, 1004), (0, 215), "chars/rce.png", (0, 500), "chars/rc1.png")
    image r 2f = im.Composite((371, 1004), (0, 215), "chars/rcf.png", (0, 500), "chars/rc1.png")
    image r 2g = im.Composite((371, 1004), (0, 215), "chars/rcg.png", (0, 500), "chars/rc1.png")
    image r 2h = im.Composite((371, 1004), (0, 215), "chars/rch.png", (0, 500), "chars/rc1.png")
    image r 2i = im.Composite((371, 1004), (0, 215), "chars/rci.png", (0, 500), "chars/rc1.png")
    image r 2j = im.Composite((371, 1004), (0, 215), "chars/rcj.png", (0, 500), "chars/rc1.png")
    image r 2k = im.Composite((371, 1004), (0, 215), "chars/rck.png", (0, 500), "chars/rc1.png")
    image r 2l = im.Composite((371, 1004), (0, 215), "chars/rcl.png", (0, 500), "chars/rc1.png")
    image r 2m = im.Composite((371, 1004), (0, 215), "chars/rcm.png", (0, 500), "chars/rc1.png")
    image r 2n = im.Composite((371, 1004), (0, 215), "chars/rcn.png", (0, 500), "chars/rc1.png")
    image r 2o = im.Composite((371, 1004), (0, 215), "chars/rco.png", (0, 500), "chars/rc1.png")
    image r 2p = im.Composite((371, 1004), (0, 215), "chars/rcp.png", (0, 500), "chars/rc1.png")
    image r 2q = im.Composite((371, 1004), (0, 215), "chars/rcq.png", (0, 500), "chars/rc1.png")
    image r 2r = im.Composite((371, 1004), (0, 215), "chars/rcr.png", (0, 500), "chars/rc1.png")
    image r 2s = im.Composite((371, 1004), (0, 215), "chars/rcs.png", (0, 500), "chars/rc1.png")
    image r 2t = im.Composite((371, 1004), (0, 215), "chars/rct.png", (0, 500), "chars/rc1.png")
    image r 2u = im.Composite((371, 1004), (0, 215), "chars/rcu.png", (0, 500), "chars/rc1.png")

# lichelle composite images

    image l 2a = im.Composite((371, 1004), (0, 215), "chars/lca.png", (0, 500), "chars/lc1.png")
    image l 2b = im.Composite((371, 1004), (0, 215), "chars/lcb.png", (0, 500), "chars/lc1.png")
    image l 2c = im.Composite((371, 1004), (0, 215), "chars/lcc.png", (0, 500), "chars/lc1.png")
    image l 2d = im.Composite((371, 1004), (0, 215), "chars/lcd.png", (0, 500), "chars/lc1.png")
    image l 2e = im.Composite((371, 1004), (0, 215), "chars/lce.png", (0, 500), "chars/lc1.png")
    image l 2f = im.Composite((371, 1004), (0, 215), "chars/lcf.png", (0, 500), "chars/lc1.png")
    image l 2g = im.Composite((371, 1004), (0, 215), "chars/lcg.png", (0, 500), "chars/lc1.png")
    image l 2h = im.Composite((371, 1004), (0, 215), "chars/lch.png", (0, 500), "chars/lc1.png")
    image l 2i = im.Composite((371, 1004), (0, 215), "chars/lci.png", (0, 500), "chars/lc1.png")
    image l 2j = im.Composite((371, 1004), (0, 215), "chars/lcj.png", (0, 500), "chars/lc1.png")
    image l 2k = im.Composite((371, 1004), (0, 215), "chars/lck.png", (0, 500), "chars/lc1.png")
    image l 2l = im.Composite((371, 1004), (0, 215), "chars/lcl.png", (0, 500), "chars/lc1.png")
    image l 2m = im.Composite((371, 1004), (0, 215), "chars/lcm.png", (0, 500), "chars/lc1.png")
    image l 2n = im.Composite((371, 1004), (0, 215), "chars/lcn.png", (0, 500), "chars/lc1.png")
    image l 2o = im.Composite((371, 1004), (0, 215), "chars/lco.png", (0, 500), "chars/lc1.png")
    image l 2p = im.Composite((371, 1004), (0, 215), "chars/lcp.png", (0, 500), "chars/lc1.png")
    image l 2q = im.Composite((371, 1004), (0, 215), "chars/lcq.png", (0, 500), "chars/lc1.png")
    image l 2r = im.Composite((371, 1004), (0, 215), "chars/lcr.png", (0, 500), "chars/lc1.png")
    image l 2s = im.Composite((371, 1004), (0, 215), "chars/lcs.png", (0, 500), "chars/lc1.png")
    image l 2t = im.Composite((371, 1004), (0, 215), "chars/lct.png", (0, 500), "chars/lc1.png")
    image l 2u = im.Composite((371, 1004), (0, 215), "chars/lcu.png", (0, 500), "chars/lc1.png")

# tania composite images

    image t 2a = im.Composite((371, 1004), (0, 215), "chars/tca.png", (0, 500), "chars/tc1.png")
    image t 2b = im.Composite((371, 1004), (0, 215), "chars/tcb.png", (0, 500), "chars/tc1.png")
    image t 2c = im.Composite((371, 1004), (0, 215), "chars/tcc.png", (0, 500), "chars/tc1.png")
    image t 2d = im.Composite((371, 1004), (0, 215), "chars/tcd.png", (0, 500), "chars/tc1.png")
    image t 2e = im.Composite((371, 1004), (0, 215), "chars/tce.png", (0, 500), "chars/tc1.png")
    image t 2f = im.Composite((371, 1004), (0, 215), "chars/tcf.png", (0, 500), "chars/tc1.png")
    image t 2g = im.Composite((371, 1004), (0, 215), "chars/tcg.png", (0, 500), "chars/tc1.png")
    image t 2h = im.Composite((371, 1004), (0, 215), "chars/tch.png", (0, 500), "chars/tc1.png")
    image t 2i = im.Composite((371, 1004), (0, 215), "chars/tci.png", (0, 500), "chars/tc1.png")
    image t 2j = im.Composite((371, 1004), (0, 215), "chars/tcj.png", (0, 500), "chars/tc1.png")
    image t 2k = im.Composite((371, 1004), (0, 215), "chars/tck.png", (0, 500), "chars/tc1.png")
    image t 2l = im.Composite((371, 1004), (0, 215), "chars/tcl.png", (0, 500), "chars/tc1.png")
    image t 2m = im.Composite((371, 1004), (0, 215), "chars/tcm.png", (0, 500), "chars/tc1.png")
    image t 2n = im.Composite((371, 1004), (0, 215), "chars/tcn.png", (0, 500), "chars/tc1.png")
    image t 2o = im.Composite((371, 1004), (0, 215), "chars/tco.png", (0, 500), "chars/tc1.png")
    image t 2p = im.Composite((371, 1004), (0, 215), "chars/tcp.png", (0, 500), "chars/tc1.png")
    image t 2q = im.Composite((371, 1004), (0, 215), "chars/tcq.png", (0, 500), "chars/tc1.png")
    image t 2r = im.Composite((371, 1004), (0, 215), "chars/tcr.png", (0, 500), "chars/tc1.png")
    image t 2s = im.Composite((371, 1004), (0, 215), "chars/tcs.png", (0, 500), "chars/tc1.png")
    image t 2t = im.Composite((371, 1004), (0, 215), "chars/tct.png", (0, 500), "chars/tc1.png")
    image t 2u = im.Composite((371, 1004), (0, 215), "chars/tcu.png", (0, 500), "chars/tc1.png")

