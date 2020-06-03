label definitions:
    
    # quick thing deal with NVL mode issue of flickering empty box

    

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

    transform tdrop(x = 640, z = 1.0):
        on replace:
            easein 0.9 xcenter x yoffset 400

    transform kissZoom(x = 640):
        on show:
            alpha 0.0 zoom 1.0 xcenter 0 yanchor 1.0 subpixel True
            easein 0.5 zoom 5.0
        on hide:
            zoom 5.0 alpha 1.0
            easeout 0.5 zoom 1.0 alpha 0.0

    transform tzoom(x = 640):
        on show:
            alpha 0.0 zoom 1.0 xcenter 0 yanchor 1.0 subpixel True
            easein 0.5 zoom 3.0
        on replace:
            easein 0.8 zoom 3.0
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

    #drop
    transform d11:
        tdrop(spriteXLeft)
    transform d12:
        tdrop(spriteXCenter)
    transform d13:
        tdrop(spriteXRight)
    transform d21:
        tdrop(spriteBLeft)
    transform d22:
        tdrop(spriteBRight)

    # zooms
    transform zoom11:
        tzoom(spriteXLeft)
    transform zoom12:
        tzoom(spriteXCenter)
    transform zoom13:
        tzoom(spriteXRight)
    transform zoom21:
        tzoom(spriteBLeft)
    transform zoom22:
        tzoom(spriteBRight)

    
    



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
#     f sick    #for robin, dead eyes, for Lichelle, hurt
#     g disappointed
#     h suprised
#     i scared
#     j smug
#     k annoyed
#     l excited
#     m happy
#     n superhappy
#     o speak - for fon, looks down at text
#     p shy
#     q sheepish
#     r puzzled
#     s listening for fon, looks at chat
#     t aroused? I guess?
#     u flirty/teasing
#     v nervous? Implement later


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

#elsa composite images

    image e 1a = im.Composite((371, 1004), (0, 215), "chars/ea.png", (0, 500), "chars/e1.png")
    image e 1b = im.Composite((371, 1004), (0, 215), "chars/eb.png", (0, 500), "chars/e1.png")
    image e 1c = im.Composite((371, 1004), (0, 215), "chars/ec.png", (0, 500), "chars/e1.png")
    image e 1d = im.Composite((371, 1004), (0, 215), "chars/ed.png", (0, 500), "chars/e1.png")
    image e 1e = im.Composite((371, 1004), (0, 215), "chars/ee.png", (0, 500), "chars/e1.png")
    image e 1f = im.Composite((371, 1004), (0, 215), "chars/ef.png", (0, 500), "chars/e1.png")
    image e 1g = im.Composite((371, 1004), (0, 215), "chars/eg.png", (0, 500), "chars/e1.png")
    image e 1h = im.Composite((371, 1004), (0, 215), "chars/eh.png", (0, 500), "chars/e1.png")
    image e 1i = im.Composite((371, 1004), (0, 215), "chars/ei.png", (0, 500), "chars/e1.png")
    image e 1j = im.Composite((371, 1004), (0, 215), "chars/ej.png", (0, 500), "chars/e1.png")
    image e 1k = im.Composite((371, 1004), (0, 215), "chars/ek.png", (0, 500), "chars/e1.png")
    image e 1l = im.Composite((371, 1004), (0, 215), "chars/el.png", (0, 500), "chars/e1.png")
    image e 1m = im.Composite((371, 1004), (0, 215), "chars/em.png", (0, 500), "chars/e1.png")
    image e 1n = im.Composite((371, 1004), (0, 215), "chars/en.png", (0, 500), "chars/e1.png")
    image e 1o = im.Composite((371, 1004), (0, 215), "chars/eo.png", (0, 500), "chars/e1.png")
    image e 1p = im.Composite((371, 1004), (0, 215), "chars/ep.png", (0, 500), "chars/e1.png")
    image e 1q = im.Composite((371, 1004), (0, 215), "chars/eq.png", (0, 500), "chars/e1.png")
    image e 1r = im.Composite((371, 1004), (0, 215), "chars/er.png", (0, 500), "chars/e1.png")
    image e 1s = im.Composite((371, 1004), (0, 215), "chars/es.png", (0, 500), "chars/e1.png")
    image e 1t = im.Composite((371, 1004), (0, 215), "chars/et.png", (0, 500), "chars/e1.png")
    image e 1u = im.Composite((371, 1004), (0, 215), "chars/eu.png", (0, 500), "chars/e1.png")


# robin composite images

    image r 1a = im.Composite((540, 1004), (-103, 300), "chars/rc1.png", (137, 395), "chars/rca.png")
    image r 1b = im.Composite((540, 1004), (-103, 300), "chars/rc1.png", (137, 395), "chars/rcb.png")
    image r 1c = im.Composite((540, 1004), (-103, 300), "chars/rc1.png", (137, 395), "chars/rcc.png")
    image r 1d = im.Composite((540, 1004), (-103, 300), "chars/rc1.png", (137, 395), "chars/rcd.png")
    image r 1e = im.Composite((540, 1004), (-103, 300), "chars/rc1.png", (137, 395), "chars/rce.png")
    image r 1f = im.Composite((540, 1004), (-103, 300), "chars/rc1.png", (137, 395), "chars/rcf.png")
    image r 1g = im.Composite((540, 1004), (-103, 300), "chars/rc1.png", (137, 395), "chars/rcg.png")
    image r 1h = im.Composite((540, 1004), (-103, 300), "chars/rc1.png", (137, 395), "chars/rch.png")
    image r 1i = im.Composite((540, 1004), (-103, 300), "chars/rc1.png", (137, 395), "chars/rci.png")
    image r 1j = im.Composite((540, 1004), (-103, 300), "chars/rc1.png", (137, 395), "chars/rcj.png")
    image r 1k = im.Composite((540, 1004), (-103, 300), "chars/rc1.png", (137, 395), "chars/rck.png")
    image r 1l = im.Composite((540, 1004), (-103, 300), "chars/rc1.png", (137, 395), "chars/rcl.png")
    image r 1m = im.Composite((540, 1004), (-103, 300), "chars/rc1.png", (137, 395), "chars/rcm.png")
    image r 1n = im.Composite((540, 1004), (-103, 300), "chars/rc1.png", (137, 395), "chars/rcn.png")
    image r 1o = im.Composite((540, 1004), (-103, 300), "chars/rc1.png", (137, 395), "chars/rco.png")
    image r 1p = im.Composite((540, 1004), (-103, 300), "chars/rc1.png", (137, 395), "chars/rcp.png")
    image r 1q = im.Composite((540, 1004), (-103, 300), "chars/rc1.png", (137, 395), "chars/rcq.png")
    image r 1r = im.Composite((540, 1004), (-103, 300), "chars/rc1.png", (137, 395), "chars/rcr.png")
    image r 1s = im.Composite((540, 1004), (-103, 300), "chars/rc1.png", (137, 395), "chars/rcs.png")
    image r 1t = im.Composite((540, 1004), (-103, 300), "chars/rc1.png", (137, 395), "chars/rct.png")
    image r 1u = im.Composite((540, 1004), (-103, 300), "chars/rc1.png", (137, 395), "chars/rcu.png")

    # robin composite images

    image r 2a = im.Composite((540, 1004), (-50, 295), "chars/rc2.png", (153, 390), "chars/rca.png")
    image r 2b = im.Composite((540, 1004), (-50, 295), "chars/rc2.png", (153, 390), "chars/rcb.png")
    image r 2c = im.Composite((540, 1004), (-50, 295), "chars/rc2.png", (153, 390), "chars/rcc.png")
    image r 2d = im.Composite((540, 1004), (-50, 295), "chars/rc2.png", (153, 390), "chars/rcd.png")
    image r 2e = im.Composite((540, 1004), (-50, 295), "chars/rc2.png", (153, 390), "chars/rce.png")
    image r 2f = im.Composite((540, 1004), (-50, 295), "chars/rc2.png", (153, 390), "chars/rcf.png")
    image r 2g = im.Composite((540, 1004), (-50, 295), "chars/rc2.png", (153, 390), "chars/rcg.png")
    image r 2h = im.Composite((540, 1004), (-50, 295), "chars/rc2.png", (153, 390), "chars/rch.png")
    image r 2i = im.Composite((540, 1004), (-50, 295), "chars/rc2.png", (153, 390), "chars/rci.png")
    image r 2j = im.Composite((540, 1004), (-50, 295), "chars/rc2.png", (153, 390), "chars/rcj.png")
    image r 2k = im.Composite((540, 1004), (-50, 295), "chars/rc2.png", (153, 390), "chars/rck.png")
    image r 2l = im.Composite((540, 1004), (-50, 295), "chars/rc2.png", (153, 390), "chars/rcl.png")
    image r 2m = im.Composite((540, 1004), (-50, 295), "chars/rc2.png", (153, 390), "chars/rcm.png")
    image r 2n = im.Composite((540, 1004), (-50, 295), "chars/rc2.png", (153, 390), "chars/rcn.png")
    image r 2o = im.Composite((540, 1004), (-50, 295), "chars/rc2.png", (153, 390), "chars/rco.png")
    image r 2p = im.Composite((540, 1004), (-50, 295), "chars/rc2.png", (153, 390), "chars/rcp.png")
    image r 2q = im.Composite((540, 1004), (-50, 295), "chars/rc2.png", (153, 390), "chars/rcq.png")
    image r 2r = im.Composite((540, 1004), (-50, 295), "chars/rc2.png", (153, 390), "chars/rcr.png")
    image r 2s = im.Composite((540, 1004), (-50, 295), "chars/rc2.png", (153, 390), "chars/rcs.png")
    image r 2t = im.Composite((540, 1004), (-50, 295), "chars/rc2.png", (153, 390), "chars/rct.png")
    image r 2u = im.Composite((540, 1004), (-50, 295), "chars/rc2.png", (153, 390), "chars/rcu.png")

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

# fontaine composite images

    image f 1a = im.Composite((371, 1004), (0, 215), "chars/fca.png", (0, 500), "chars/fc1.png")
    image f 1b = im.Composite((371, 1004), (0, 215), "chars/fcb.png", (0, 500), "chars/fc1.png")
    image f 1c = im.Composite((371, 1004), (0, 215), "chars/fcc.png", (0, 500), "chars/fc1.png")
    image f 1d = im.Composite((371, 1004), (0, 215), "chars/fcd.png", (0, 500), "chars/fc1.png")
    image f 1e = im.Composite((371, 1004), (0, 215), "chars/fce.png", (0, 500), "chars/fc1.png")
    image f 1f = im.Composite((371, 1004), (0, 215), "chars/fcf.png", (0, 500), "chars/fc1.png")
    image f 1g = im.Composite((371, 1004), (0, 215), "chars/fcg.png", (0, 500), "chars/fc1.png")
    image f 1h = im.Composite((371, 1004), (0, 215), "chars/fch.png", (0, 500), "chars/fc1.png")
    image f 1i = im.Composite((371, 1004), (0, 215), "chars/fci.png", (0, 500), "chars/fc1.png")
    image f 1j = im.Composite((371, 1004), (0, 215), "chars/fcj.png", (0, 500), "chars/fc1.png")
    image f 1k = im.Composite((371, 1004), (0, 215), "chars/fck.png", (0, 500), "chars/fc1.png")
    image f 1l = im.Composite((371, 1004), (0, 215), "chars/fcl.png", (0, 500), "chars/fc1.png")
    image f 1m = im.Composite((371, 1004), (0, 215), "chars/fcm.png", (0, 500), "chars/fc1.png")
    image f 1n = im.Composite((371, 1004), (0, 215), "chars/fcn.png", (0, 500), "chars/fc1.png")
    image f 1o = im.Composite((371, 1004), (0, 215), "chars/fco.png", (0, 500), "chars/fc1.png")
    image f 1p = im.Composite((371, 1004), (0, 215), "chars/fcp.png", (0, 500), "chars/fc1.png")
    image f 1q = im.Composite((371, 1004), (0, 215), "chars/fcq.png", (0, 500), "chars/fc1.png")
    image f 1r = im.Composite((371, 1004), (0, 215), "chars/fcr.png", (0, 500), "chars/fc1.png")
    image f 1s = im.Composite((371, 1004), (0, 215), "chars/fcs.png", (0, 500), "chars/fc1.png")
    image f 1t = im.Composite((371, 1004), (0, 215), "chars/fct.png", (0, 500), "chars/fc1.png")
    image f 1u = im.Composite((371, 1004), (0, 215), "chars/fcu.png", (0, 500), "chars/fc1.png")

# fontaine composite images (doctor coat)

    image f 2a = im.Composite((371, 1004), (0, 215), "chars/fca.png", (0, 500), "chars/fc2.png")
    image f 2b = im.Composite((371, 1004), (0, 215), "chars/fcb.png", (0, 500), "chars/fc2.png")
    image f 2c = im.Composite((371, 1004), (0, 215), "chars/fcc.png", (0, 500), "chars/fc2.png")
    image f 2d = im.Composite((371, 1004), (0, 215), "chars/fcd.png", (0, 500), "chars/fc2.png")
    image f 2e = im.Composite((371, 1004), (0, 215), "chars/fce.png", (0, 500), "chars/fc2.png")
    image f 2f = im.Composite((371, 1004), (0, 215), "chars/fcf.png", (0, 500), "chars/fc2.png")
    image f 2g = im.Composite((371, 1004), (0, 215), "chars/fcg.png", (0, 500), "chars/fc2.png")
    image f 2h = im.Composite((371, 1004), (0, 215), "chars/fch.png", (0, 500), "chars/fc2.png")
    image f 2i = im.Composite((371, 1004), (0, 215), "chars/fci.png", (0, 500), "chars/fc2.png")
    image f 2j = im.Composite((371, 1004), (0, 215), "chars/fcj.png", (0, 500), "chars/fc2.png")
    image f 2k = im.Composite((371, 1004), (0, 215), "chars/fck.png", (0, 500), "chars/fc2.png")
    image f 2l = im.Composite((371, 1004), (0, 215), "chars/fcl.png", (0, 500), "chars/fc2.png")
    image f 2m = im.Composite((371, 1004), (0, 215), "chars/fcm.png", (0, 500), "chars/fc2.png")
    image f 2n = im.Composite((371, 1004), (0, 215), "chars/fcn.png", (0, 500), "chars/fc2.png")
    image f 2o = im.Composite((371, 1004), (0, 215), "chars/fco.png", (0, 500), "chars/fc2.png")
    image f 2p = im.Composite((371, 1004), (0, 215), "chars/fcp.png", (0, 500), "chars/fc2.png")
    image f 2q = im.Composite((371, 1004), (0, 215), "chars/fcq.png", (0, 500), "chars/fc2.png")
    image f 2r = im.Composite((371, 1004), (0, 215), "chars/fcr.png", (0, 500), "chars/fc2.png")
    image f 2s = im.Composite((371, 1004), (0, 215), "chars/fcs.png", (0, 500), "chars/fc2.png")
    image f 2t = im.Composite((371, 1004), (0, 215), "chars/fct.png", (0, 500), "chars/fc2.png")
    image f 2u = im.Composite((371, 1004), (0, 215), "chars/fcu.png", (0, 500), "chars/fc2.png")


# kylie composite images

    image k 1a = im.Composite((371, 1004), (0, 215), "chars/kca.png", (0, 500), "chars/kc1.png")
    image k 1b = im.Composite((371, 1004), (0, 215), "chars/kcb.png", (0, 500), "chars/kc1.png")
    image k 1c = im.Composite((371, 1004), (0, 215), "chars/kcc.png", (0, 500), "chars/kc1.png")
    image k 1d = im.Composite((371, 1004), (0, 215), "chars/kcd.png", (0, 500), "chars/kc1.png")
    image k 1e = im.Composite((371, 1004), (0, 215), "chars/kce.png", (0, 500), "chars/kc1.png")
    image k 1f = im.Composite((371, 1004), (0, 215), "chars/kcf.png", (0, 500), "chars/kc1.png")
    image k 1g = im.Composite((371, 1004), (0, 215), "chars/kcg.png", (0, 500), "chars/kc1.png")
    image k 1h = im.Composite((371, 1004), (0, 215), "chars/kch.png", (0, 500), "chars/kc1.png")
    image k 1i = im.Composite((371, 1004), (0, 215), "chars/kci.png", (0, 500), "chars/kc1.png")
    image k 1j = im.Composite((371, 1004), (0, 215), "chars/kcj.png", (0, 500), "chars/kc1.png")
    image k 1k = im.Composite((371, 1004), (0, 215), "chars/kck.png", (0, 500), "chars/kc1.png")
    image k 1l = im.Composite((371, 1004), (0, 215), "chars/kcl.png", (0, 500), "chars/kc1.png")
    image k 1m = im.Composite((371, 1004), (0, 215), "chars/kcm.png", (0, 500), "chars/kc1.png")
    image k 1n = im.Composite((371, 1004), (0, 215), "chars/kcn.png", (0, 500), "chars/kc1.png")
    image k 1o = im.Composite((371, 1004), (0, 215), "chars/kco.png", (0, 500), "chars/kc1.png")
    image k 1p = im.Composite((371, 1004), (0, 215), "chars/kcp.png", (0, 500), "chars/kc1.png")
    image k 1q = im.Composite((371, 1004), (0, 215), "chars/kcq.png", (0, 500), "chars/kc1.png")
    image k 1r = im.Composite((371, 1004), (0, 215), "chars/kcr.png", (0, 500), "chars/kc1.png")
    image k 1s = im.Composite((371, 1004), (0, 215), "chars/kcs.png", (0, 500), "chars/kc1.png")
    image k 1t = im.Composite((371, 1004), (0, 215), "chars/kct.png", (0, 500), "chars/kc1.png")
    image k 1u = im.Composite((371, 1004), (0, 215), "chars/kcu.png", (0, 500), "chars/kc1.png")

    #david composite images

    image d 1a = im.Composite((371, 1004), (0, 215), "chars/da.png", (0, 500), "chars/d1.png")
    image d 1b = im.Composite((371, 1004), (0, 215), "chars/db.png", (0, 500), "chars/d1.png")
    image d 1c = im.Composite((371, 1004), (0, 215), "chars/dc.png", (0, 500), "chars/d1.png")
    image d 1d = im.Composite((371, 1004), (0, 215), "chars/dd.png", (0, 500), "chars/d1.png")
    image d 1e = im.Composite((371, 1004), (0, 215), "chars/de.png", (0, 500), "chars/d1.png")
    image d 1f = im.Composite((371, 1004), (0, 215), "chars/df.png", (0, 500), "chars/d1.png")
    image d 1g = im.Composite((371, 1004), (0, 215), "chars/dg.png", (0, 500), "chars/d1.png")
    image d 1h = im.Composite((371, 1004), (0, 215), "chars/dh.png", (0, 500), "chars/d1.png")
    image d 1i = im.Composite((371, 1004), (0, 215), "chars/di.png", (0, 500), "chars/d1.png")
    image d 1j = im.Composite((371, 1004), (0, 215), "chars/dj.png", (0, 500), "chars/d1.png")
    image d 1k = im.Composite((371, 1004), (0, 215), "chars/dk.png", (0, 500), "chars/d1.png")
    image d 1l = im.Composite((371, 1004), (0, 215), "chars/dl.png", (0, 500), "chars/d1.png")
    image d 1m = im.Composite((371, 1004), (0, 215), "chars/dm.png", (0, 500), "chars/d1.png")
    image d 1n = im.Composite((371, 1004), (0, 215), "chars/dn.png", (0, 500), "chars/d1.png")
    image d 1o = im.Composite((371, 1004), (0, 215), "chars/do.png", (0, 500), "chars/d1.png")
    image d 1p = im.Composite((371, 1004), (0, 215), "chars/dp.png", (0, 500), "chars/d1.png")
    image d 1q = im.Composite((371, 1004), (0, 215), "chars/dq.png", (0, 500), "chars/d1.png")
    image d 1r = im.Composite((371, 1004), (0, 215), "chars/dr.png", (0, 500), "chars/d1.png")
    image d 1s = im.Composite((371, 1004), (0, 215), "chars/ds.png", (0, 500), "chars/d1.png")
    image d 1t = im.Composite((371, 1004), (0, 215), "chars/dt.png", (0, 500), "chars/d1.png")
    image d 1u = im.Composite((371, 1004), (0, 215), "chars/du.png", (0, 500), "chars/d1.png")


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

    #askTania Faces

    default askTa = Image("img/askTania7.png")
    define askTb = Image("img/askTania8.png")
    define askTc = Image("img/askTania5.png")
    define askTd = Image("img/askTania1.png")

    define askTe = Image("img/askTania2.png")
    define askTf = Image("img/askTania3.png")
    define askTg = Image("img/askTania4.png")
    define askTh = Image("img/askTania6.png")

    define askTi = Image("img/askTania9.png")
    define askTj = Image("img/askTania10.png")
    define askTk = Image("img/askTania11.png")
