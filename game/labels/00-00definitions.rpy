label definitions:
    
    # quick thing deal with NVL mode issue of flickering empty box

    

    #transforms will be used to animate and position characters. Beecause we're using a gui with a limited window, there can only be a few positions. Left-front, center front, right front, and backs. 

    #we need to determine what types of transforms we need.  The hop from DDLC is nice and all, but ot doesn't really fit the tone. Valhalla's much closer, not a lot of transforms needed. 

    transform textFade(x = 640, y = 200, z = 1.0):
        on show:
            xcenter x ycenter y yoffset 0 ypos y zoom z*1.00 alpha 0.0 subpixel True
            alpha 1.00
        on replace:
            xcenter x ycenter y yoffset 0 ypos y zoom z*1.00 alpha 0.0 subpixel True
            alpha 1.00
        on hide:
            xcenter x yoffset 0 yanchor 1.0 ypos 1.00 zoom z*1.00 alpha 1.0 subpixel True
            alpha 0.00

    transform tfade(x = 640, z = 1.0):
        on show:
            xcenter x yoffset 0 yanchor 1.0 ypos 1.00 zoom z*1.00 alpha 0.0 subpixel True
            easein 1.0 alpha 1.00
        on hide:
            xcenter x yoffset 0 yanchor 1.0 ypos 1.00 zoom z*1.00 alpha 1.0 subpixel True
            linear .5 alpha 0.00

    transform sophfade(x = 0, y = 80, z = 0.9):
        on show:
            xpos x  ycenter y ypos y zoom z*1.00 alpha 0.0 subpixel True
            easein 1.0 alpha 1.00 
        on hide:
            xpos x  ycenter y ypos y zoom z*1.00 alpha 1.0 subpixel True
            linear .5 alpha 0.00 

    transform tFromLeft(x = 640, z = 1.0):
        on show:
            xcenter x xoffset -600 yanchor 1.0 ypos 1.00 zoom z*1.00 alpha 1.0 subpixel True
            easein 1.0 xoffset 0
        on hide:
            xcenter x xoffset 0 yanchor 1.0 ypos 1.00 zoom z*1.00 alpha 1.0 subpixel True
            easein 1.0 xoffset -600

    transform tFromRight(x = 640, z = 1.0):
        on show:
            xcenter x xoffset 1200 yanchor 1.0 ypos 1.00 zoom z*1.00 alpha 1.0 subpixel True
            easein 1.0 xoffset 0
        on hide:
            xcenter x xoffset 0 yanchor 1.0 ypos 1.00 zoom z*1.00 alpha 1.0 subpixel True
            easein 1.0 xoffset 1200

    transform moveTo(x = 640, z = 1.0):
        on replace:
            easein 0.5 xcenter x

    transform tdrop(x = 640, z = 1.0):
        on replace:
            easein 0.9 xcenter x yoffset 400

    transform kissZoom(x = 640):
        on show:
            xcenter x yoffset 0 yanchor 1.0 ypos 1.0
            easein 0.5 zoom 2.0 ypos 1.8
        on hide:
            xcenter x yoffset 0 yanchor 1.0 ypos 1.00 zoom 2.0 alpha 1.0
            easeout 1.0 zoom 1.0 alpha 0.0

    transform tzoom(x = 640):
        on show:
            alpha 0.0 zoom 1.0 xcenter 0 yanchor 1.0 subpixel True
            easein 0.5 zoom 3.0
        on replace:
            easein 0.8 zoom 3.0
        on hide:
            zoom 5.0 alpha 1.0
            easeout 1.0 zoom 1.0 alpha 0.0

    transform tInstant(x = 640, z = 1.0):
        on show:
            xcenter x yoffset 0 yanchor 1.0 ypos 1.00 zoom z*1.00 alpha 1.0 subpixel True
            
        on hide:
            xcenter x yoffset 0 yanchor 1.0 ypos 1.00 zoom z*1.00 alpha 0.0 subpixel True

    transform justFade():
        linear 0.8 alpha 0.00
            

    # quick zooms for speaking callbacks

    transform speakZoom:
        easein 0.5 zoom 1.05 

    transform speakNormal:
        easein 0.5 zoom 1.0 

    init python:

        

        spriteXLeft = 225
        spriteXCenter = 550
        spriteXRight = 825
        spriteBLeft = 500
        spriteBRight = 700
        spriteSophX = 10
        spriteSophY = 10
        
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

# TEST SOPHIE IMAGES

    image side s 1a = Image("chars/sca.png")
    image side s 1b = Image("chars/scb.png")
    image side s 1c = Image("chars/scc.png")
    image side s 1d = Image("chars/scd.png")
    image side s 1e = Image("chars/sce.png")
    image side s 1f = Image("chars/scf.png")
    image side s 1g = Image("chars/scg.png")
    image side s 1h = Image("chars/sch.png")
    image side s 1i = Image("chars/sci.png")
    image side s 1j = Image("chars/scj.png")
    image side s 1k = Image("chars/sck.png")
    image side s 1l = Image("chars/scl.png")
    image side s 1m = Image("chars/scm.png")
    image side s 1n = Image("chars/scn.png")
    image side s 1o = Image("chars/sco.png")
    image side s 1p = Image("chars/scp.png")
    image side s 1q = Image("chars/scq.png")
    image side s 1r = Image("chars/scr.png")
    image side s 1s = Image("chars/scs.png")
    image side s 1t = Image("chars/sct.png")
    image side s 1u = Image("chars/scu.png")


#cassandra composite images

    image c 1a = im.Composite((371, 1004), (0, 240), "chars/c1.png", (135, 423), "chars/ca.png")
    image c 1b = im.Composite((371, 1004), (0, 240), "chars/c1.png", (135, 423), "chars/cb.png")
    image c 1c = im.Composite((371, 1004), (0, 240), "chars/c1.png", (135, 423), "chars/cc.png")
    image c 1d = im.Composite((371, 1004), (0, 240), "chars/c1.png", (135, 423), "chars/cd.png")
    image c 1e = im.Composite((371, 1004), (0, 240), "chars/c1.png", (135, 423), "chars/ce.png")
    image c 1f = im.Composite((371, 1004), (0, 240), "chars/c1.png", (135, 423), "chars/cf.png")
    image c 1g = im.Composite((371, 1004), (0, 240), "chars/c1.png", (135, 423), "chars/cg.png")
    image c 1h = im.Composite((371, 1004), (0, 240), "chars/c1.png", (135, 423), "chars/ch.png")
    image c 1i = im.Composite((371, 1004), (0, 240), "chars/c1.png", (135, 423), "chars/ci.png")
    image c 1j = im.Composite((371, 1004), (0, 240), "chars/c1.png", (135, 423), "chars/cj.png")
    image c 1k = im.Composite((371, 1004), (0, 240), "chars/c1.png", (135, 423), "chars/ck.png")
    image c 1l = im.Composite((371, 1004), (0, 240), "chars/c1.png", (135, 423), "chars/cl.png")
    image c 1m = im.Composite((371, 1004), (0, 240), "chars/c1.png", (135, 423), "chars/cm.png")
    image c 1n = im.Composite((371, 1004), (0, 240), "chars/c1.png", (135, 423), "chars/cn.png")
    image c 1o = im.Composite((371, 1004), (0, 240), "chars/c1.png", (135, 423), "chars/co.png")
    image c 1p = im.Composite((371, 1004), (0, 240), "chars/c1.png", (135, 423), "chars/cp.png")
    image c 1q = im.Composite((371, 1004), (0, 240), "chars/c1.png", (135, 423), "chars/cq.png")
    image c 1r = im.Composite((371, 1004), (0, 240), "chars/c1.png", (135, 423), "chars/cr.png")
    image c 1s = im.Composite((371, 1004), (0, 240), "chars/c1.png", (135, 423), "chars/cs.png")
    image c 1t = im.Composite((371, 1004), (0, 240), "chars/c1.png", (135, 423), "chars/ct.png")
    image c 1u = im.Composite((371, 1004), (0, 240), "chars/c1.png", (135, 423), "chars/cu.png")

    image c 1bleed = im.Composite((371, 1004), (0, 240), "chars/c1.png", (135, 423), "chars/cb.png", (0, 240), "img/cassBlood.png")
    image c 2bleed = im.Composite((371, 1004), (0, 240), "chars/c1.png", (135, 423), "chars/ch.png", (0, 240), "img/cassBlood.png")

    image c 2a = im.Composite((371, 1004), (0, 240), "chars/c1.png", (135, 423), "chars/ca.png")
    image c 2b = im.Composite((371, 1004), (0, 240), "chars/c1.png", (135, 423), "chars/cb.png")
    image c 2c = im.Composite((371, 1004), (0, 240), "chars/c1.png", (135, 423), "chars/cc.png")
    image c 2d = im.Composite((371, 1004), (0, 240), "chars/c1.png", (135, 423), "chars/cd.png")
    image c 2e = im.Composite((371, 1004), (0, 240), "chars/c1.png", (135, 423), "chars/ce.png")
    image c 2f = im.Composite((371, 1004), (0, 240), "chars/c1.png", (135, 423), "chars/cf.png")
    image c 2g = im.Composite((371, 1004), (0, 240), "chars/c1.png", (135, 423), "chars/cg.png")
    image c 2h = im.Composite((371, 1004), (0, 240), "chars/c1.png", (135, 423), "chars/ch.png")
    image c 2i = im.Composite((371, 1004), (0, 240), "chars/c1.png", (135, 423), "chars/ci.png")
    image c 2j = im.Composite((371, 1004), (0, 240), "chars/c1.png", (135, 423), "chars/cj.png")
    image c 2k = im.Composite((371, 1004), (0, 240), "chars/c1.png", (135, 423), "chars/ck.png")
    image c 2l = im.Composite((371, 1004), (0, 240), "chars/c1.png", (135, 423), "chars/cl.png")
    image c 2m = im.Composite((371, 1004), (0, 240), "chars/c1.png", (135, 423), "chars/cm.png")
    image c 2n = im.Composite((371, 1004), (0, 240), "chars/c1.png", (135, 423), "chars/cn.png")
    image c 2o = im.Composite((371, 1004), (0, 240), "chars/c1.png", (135, 423), "chars/co.png")
    image c 2p = im.Composite((371, 1004), (0, 240), "chars/c1.png", (135, 423), "chars/cp.png")
    image c 2q = im.Composite((371, 1004), (0, 240), "chars/c1.png", (135, 423), "chars/cq.png")
    image c 2r = im.Composite((371, 1004), (0, 240), "chars/c1.png", (135, 423), "chars/cr.png")
    image c 2s = im.Composite((371, 1004), (0, 240), "chars/c1.png", (135, 423), "chars/cs.png")
    image c 2t = im.Composite((371, 1004), (0, 240), "chars/c1.png", (135, 423), "chars/ct.png")
    image c 2u = im.Composite((371, 1004), (0, 240), "chars/c1.png", (135, 423), "chars/cu.png")

    #lichelle
    image l 1a = im.Composite((348, 942), (0, 210), "chars/lc1.png", (116, 342),  "chars/lca.png")
    image l 1b = im.Composite((348, 942), (0, 210), "chars/lc1.png", (116, 342),  "chars/lcb.png")
    image l 1c = im.Composite((348, 942), (0, 210), "chars/lc1.png", (116, 342),  "chars/lcc.png")
    image l 1d = im.Composite((348, 942), (0, 210), "chars/lc1.png", (116, 342),  "chars/lcd.png")
    image l 1e = im.Composite((348, 942), (0, 210), "chars/lc1.png", (116, 342),  "chars/lce.png")
    image l 1f = im.Composite((348, 942), (0, 210), "chars/lc1.png", (116, 342),  "chars/lcf.png")
    image l 1g = im.Composite((348, 942), (0, 210), "chars/lc1.png", (116, 342),  "chars/lcg.png")
    image l 1h = im.Composite((348, 942), (0, 210), "chars/lc1.png", (116, 342),  "chars/lch.png")
    image l 1i = im.Composite((348, 942), (0, 210), "chars/lc1.png", (116, 342),  "chars/lci.png")
    image l 1j = im.Composite((348, 942), (0, 210), "chars/lc1.png", (116, 342),  "chars/lcj.png")
    image l 1k = im.Composite((348, 942), (0, 210), "chars/lc1.png", (116, 342),  "chars/lck.png")
    image l 1l = im.Composite((348, 942), (0, 210), "chars/lc1.png", (116, 342),  "chars/lcl.png")
    image l 1m = im.Composite((348, 942), (0, 210), "chars/lc1.png", (116, 342),  "chars/lcm.png")
    image l 1n = im.Composite((348, 942), (0, 210), "chars/lc1.png", (116, 342),  "chars/lcn.png")
    image l 1o = im.Composite((348, 942), (0, 210), "chars/lc1.png", (116, 342),  "chars/lco.png")
    image l 1p = im.Composite((348, 942), (0, 210), "chars/lc1.png", (116, 342),  "chars/lcp.png")
    image l 1q = im.Composite((348, 942), (0, 210), "chars/lc1.png", (116, 342),  "chars/lcq.png")
    image l 1r = im.Composite((348, 942), (0, 210), "chars/lc1.png", (116, 342),  "chars/lcr.png")
    image l 1s = im.Composite((348, 942), (0, 210), "chars/lc1.png", (116, 342),  "chars/lcs.png")
    image l 1t = im.Composite((348, 942), (0, 210), "chars/lc1.png", (116, 342),  "chars/lct.png")
    image l 1u = im.Composite((348, 942), (0, 210), "chars/lc1.png", (116, 342),  "chars/lcu.png")

    image l 2a = im.Composite((348, 942), (0, 210), "chars/lc1.png", (116, 342),  "chars/lca.png")
    image l 2b = im.Composite((348, 942), (0, 210), "chars/lc1.png", (116, 342),  "chars/lcb.png")
    image l 2c = im.Composite((348, 942), (0, 210), "chars/lc1.png", (116, 342),  "chars/lcc.png")
    image l 2d = im.Composite((348, 942), (0, 210), "chars/lc1.png", (116, 342),  "chars/lcd.png")
    image l 2e = im.Composite((348, 942), (0, 210), "chars/lc1.png", (116, 342),  "chars/lce.png")
    image l 2f = im.Composite((348, 942), (0, 210), "chars/lc1.png", (116, 342),  "chars/lcf.png")
    image l 2g = im.Composite((348, 942), (0, 210), "chars/lc1.png", (116, 342),  "chars/lcg.png")
    image l 2h = im.Composite((348, 942), (0, 210), "chars/lc1.png", (116, 342),  "chars/lch.png")
    image l 2i = im.Composite((348, 942), (0, 210), "chars/lc1.png", (116, 342),  "chars/lci.png")
    image l 2j = im.Composite((348, 942), (0, 210), "chars/lc1.png", (116, 342),  "chars/lcj.png")
    image l 2k = im.Composite((348, 942), (0, 210), "chars/lc1.png", (116, 342),  "chars/lck.png")
    image l 2l = im.Composite((348, 942), (0, 210), "chars/lc1.png", (116, 342),  "chars/lcl.png")
    image l 2m = im.Composite((348, 942), (0, 210), "chars/lc1.png", (116, 342),  "chars/lcm.png")
    image l 2n = im.Composite((348, 942), (0, 210), "chars/lc1.png", (116, 342),  "chars/lcn.png")
    image l 2o = im.Composite((348, 942), (0, 210), "chars/lc1.png", (116, 342),  "chars/lco.png")
    image l 2p = im.Composite((348, 942), (0, 210), "chars/lc1.png", (116, 342),  "chars/lcp.png")
    image l 2q = im.Composite((348, 942), (0, 210), "chars/lc1.png", (116, 342),  "chars/lcq.png")
    image l 2r = im.Composite((348, 942), (0, 210), "chars/lc1.png", (116, 342),  "chars/lcr.png")
    image l 2s = im.Composite((348, 942), (0, 210), "chars/lc1.png", (116, 342),  "chars/lcs.png")
    image l 2t = im.Composite((348, 942), (0, 210), "chars/lc1.png", (116, 342),  "chars/lct.png")
    image l 2u = im.Composite((348, 942), (0, 210), "chars/lc1.png", (116, 342),  "chars/lcu.png")

#elsa composite images

    image e 1a = im.Composite((371, 1004), (0, 250), "chars/tc1.png", (82, 358), "chars/eca.png")
    image e 1b = im.Composite((371, 1004), (0, 250), "chars/tc1.png", (82, 358), "chars/ecb.png")
    image e 1c = im.Composite((371, 1004), (0, 250), "chars/tc1.png", (82, 358), "chars/ecc.png")
    image e 1d = im.Composite((371, 1004), (0, 250), "chars/tc1.png", (82, 358), "chars/ecd.png")
    image e 1e = im.Composite((371, 1004), (0, 250), "chars/tc1.png", (82, 358), "chars/ece.png")
    image e 1f = im.Composite((371, 1004), (0, 250), "chars/tc1.png", (82, 358), "chars/ecf.png")
    image e 1g = im.Composite((371, 1004), (0, 250), "chars/tc1.png", (82, 358), "chars/ecg.png")
    image e 1h = im.Composite((371, 1004), (0, 250), "chars/tc1.png", (82, 358), "chars/ech.png")
    image e 1i = im.Composite((371, 1004), (0, 250), "chars/tc1.png", (82, 358), "chars/eci.png")
    image e 1j = im.Composite((371, 1004), (0, 250), "chars/tc1.png", (82, 358), "chars/ecj.png")
    image e 1k = im.Composite((371, 1004), (0, 250), "chars/tc1.png", (82, 358), "chars/eck.png")
    image e 1l = im.Composite((371, 1004), (0, 250), "chars/tc1.png", (82, 358), "chars/ecl.png")
    image e 1m = im.Composite((371, 1004), (0, 250), "chars/tc1.png", (82, 358), "chars/ecm.png")
    image e 1n = im.Composite((371, 1004), (0, 250), "chars/tc1.png", (82, 358), "chars/ecn.png")
    image e 1o = im.Composite((371, 1004), (0, 250), "chars/tc1.png", (82, 358), "chars/eco.png")
    image e 1p = im.Composite((371, 1004), (0, 250), "chars/tc1.png", (82, 358), "chars/ecp.png")
    image e 1q = im.Composite((371, 1004), (0, 250), "chars/tc1.png", (82, 358), "chars/ecq.png")
    image e 1r = im.Composite((371, 1004), (0, 250), "chars/tc1.png", (82, 358), "chars/ecr.png")
    image e 1s = im.Composite((371, 1004), (0, 250), "chars/tc1.png", (82, 358), "chars/ecs.png")
    image e 1t = im.Composite((371, 1004), (0, 250), "chars/tc1.png", (82, 358), "chars/ect.png")
    image e 1u = im.Composite((371, 1004), (0, 250), "chars/tc1.png", (82, 358), "chars/ecu.png")

# tania

    image t 1a = im.Composite((371, 1004), (0, 250), "chars/tc1.png", (82, 358), "chars/tca.png")
    image t 1b = im.Composite((371, 1004), (0, 250), "chars/tc1.png", (82, 358), "chars/tcb.png")
    image t 1c = im.Composite((371, 1004), (0, 250), "chars/tc1.png", (82, 358), "chars/tcc.png")
    image t 1d = im.Composite((371, 1004), (0, 250), "chars/tc1.png", (82, 358), "chars/tcd.png")
    image t 1e = im.Composite((371, 1004), (0, 250), "chars/tc1.png", (82, 358), "chars/tce.png")
    image t 1f = im.Composite((371, 1004), (0, 250), "chars/tc1.png", (82, 358), "chars/tcf.png")
    image t 1g = im.Composite((371, 1004), (0, 250), "chars/tc1.png", (82, 358), "chars/tcg.png")
    image t 1h = im.Composite((371, 1004), (0, 250), "chars/tc1.png", (82, 358), "chars/tch.png")
    image t 1i = im.Composite((371, 1004), (0, 250), "chars/tc1.png", (82, 358), "chars/tci.png")
    image t 1j = im.Composite((371, 1004), (0, 250), "chars/tc1.png", (82, 358), "chars/tcj.png")
    image t 1k = im.Composite((371, 1004), (0, 250), "chars/tc1.png", (82, 358), "chars/tck.png")
    image t 1l = im.Composite((371, 1004), (0, 250), "chars/tc1.png", (82, 358), "chars/tcl.png")
    image t 1m = im.Composite((371, 1004), (0, 250), "chars/tc1.png", (82, 358), "chars/tcm.png")
    image t 1n = im.Composite((371, 1004), (0, 250), "chars/tc1.png", (82, 358), "chars/tcn.png")
    image t 1o = im.Composite((371, 1004), (0, 250), "chars/tc1.png", (82, 358), "chars/tco.png")
    image t 1p = im.Composite((371, 1004), (0, 250), "chars/tc1.png", (82, 358), "chars/tcp.png")
    image t 1q = im.Composite((371, 1004), (0, 250), "chars/tc1.png", (82, 358), "chars/tcq.png")
    image t 1r = im.Composite((371, 1004), (0, 250), "chars/tc1.png", (82, 358), "chars/tcr.png")
    image t 1s = im.Composite((371, 1004), (0, 250), "chars/tc1.png", (82, 358), "chars/tcs.png")
    image t 1t = im.Composite((371, 1004), (0, 250), "chars/tc1.png", (82, 358), "chars/tct.png")
    image t 1u = im.Composite((371, 1004), (0, 250), "chars/tc1.png", (82, 358), "chars/tcu.png")

    # tania composite images

    image t 2a = im.Composite((371, 1004), (0, 250), "chars/tc1.png", (82, 358), "chars/tca.png")
    image t 2b = im.Composite((371, 1004), (0, 250), "chars/tc1.png", (82, 358), "chars/tcb.png")
    image t 2c = im.Composite((371, 1004), (0, 250), "chars/tc1.png", (82, 358), "chars/tcc.png")
    image t 2d = im.Composite((371, 1004), (0, 250), "chars/tc1.png", (82, 358), "chars/tcd.png")
    image t 2e = im.Composite((371, 1004), (0, 250), "chars/tc1.png", (82, 358), "chars/tce.png")
    image t 2f = im.Composite((371, 1004), (0, 250), "chars/tc1.png", (82, 358), "chars/tcf.png")
    image t 2g = im.Composite((371, 1004), (0, 250), "chars/tc1.png", (82, 358), "chars/tcg.png")
    image t 2h = im.Composite((371, 1004), (0, 250), "chars/tc1.png", (82, 358), "chars/tch.png")
    image t 2i = im.Composite((371, 1004), (0, 250), "chars/tc1.png", (82, 358), "chars/tci.png")
    image t 2j = im.Composite((371, 1004), (0, 250), "chars/tc1.png", (82, 358), "chars/tcj.png")
    image t 2k = im.Composite((371, 1004), (0, 250), "chars/tc1.png", (82, 358), "chars/tck.png")
    image t 2l = im.Composite((371, 1004), (0, 250), "chars/tc1.png", (82, 358), "chars/tcl.png")
    image t 2m = im.Composite((371, 1004), (0, 250), "chars/tc1.png", (82, 358), "chars/tcm.png")
    image t 2n = im.Composite((371, 1004), (0, 250), "chars/tc1.png", (82, 358), "chars/tcn.png")
    image t 2o = im.Composite((371, 1004), (0, 250), "chars/tc1.png", (82, 358), "chars/tco.png")
    image t 2p = im.Composite((371, 1004), (0, 250), "chars/tc1.png", (82, 358), "chars/tcp.png")
    image t 2q = im.Composite((371, 1004), (0, 250), "chars/tc1.png", (82, 358), "chars/tcq.png")
    image t 2r = im.Composite((371, 1004), (0, 250), "chars/tc1.png", (82, 358), "chars/tcr.png")
    image t 2s = im.Composite((371, 1004), (0, 250), "chars/tc1.png", (82, 358), "chars/tcs.png")
    image t 2t = im.Composite((371, 1004), (0, 250), "chars/tc1.png", (82, 358), "chars/tct.png")
    image t 2u = im.Composite((371, 1004), (0, 250), "chars/tc1.png", (82, 358), "chars/tcu.png")

# robin composite images

    image r 1a = im.Composite((346, 934), (0, 220), "chars/rc1.png", (153, 281), "chars/rca.png")
    image r 1b = im.Composite((346, 934), (0, 220), "chars/rc1.png", (153, 281), "chars/rcb.png")
    image r 1c = im.Composite((346, 934), (0, 220), "chars/rc1.png", (153, 281), "chars/rcc.png")
    image r 1d = im.Composite((346, 934), (0, 220), "chars/rc1.png", (153, 281), "chars/rcd.png")
    image r 1e = im.Composite((346, 934), (0, 220), "chars/rc1.png", (153, 281), "chars/rce.png")
    image r 1f = im.Composite((346, 934), (0, 220), "chars/rc1.png", (153, 281), "chars/rcf.png")
    image r 1g = im.Composite((346, 934), (0, 220), "chars/rc1.png", (153, 281), "chars/rcg.png")
    image r 1h = im.Composite((346, 934), (0, 220), "chars/rc1.png", (153, 281), "chars/rch.png")
    image r 1i = im.Composite((346, 934), (0, 220), "chars/rc1.png", (153, 281), "chars/rci.png")
    image r 1j = im.Composite((346, 934), (0, 220), "chars/rc1.png", (153, 281), "chars/rcj.png")
    image r 1k = im.Composite((346, 934), (0, 220), "chars/rc1.png", (153, 281), "chars/rck.png")
    image r 1l = im.Composite((346, 934), (0, 220), "chars/rc1.png", (153, 281), "chars/rcl.png")
    image r 1m = im.Composite((346, 934), (0, 220), "chars/rc1.png", (153, 281), "chars/rcm.png")
    image r 1n = im.Composite((346, 934), (0, 220), "chars/rc1.png", (153, 281), "chars/rcn.png")
    image r 1o = im.Composite((346, 934), (0, 220), "chars/rc1.png", (153, 281), "chars/rco.png")
    image r 1p = im.Composite((346, 934), (0, 220), "chars/rc1.png", (153, 281), "chars/rcp.png")
    image r 1q = im.Composite((346, 934), (0, 220), "chars/rc1.png", (153, 281), "chars/rcq.png")
    image r 1r = im.Composite((346, 934), (0, 220), "chars/rc1.png", (153, 281), "chars/rcr.png")
    image r 1s = im.Composite((346, 934), (0, 220), "chars/rc1.png", (153, 281), "chars/rcs.png")
    image r 1t = im.Composite((346, 934), (0, 220), "chars/rc1.png", (153, 281), "chars/rct.png")
    image r 1u = im.Composite((346, 934), (0, 220), "chars/rc1.png", (153, 281), "chars/rcu.png")

    # robin composite images

    image r 2a = im.Composite((346, 934), (0, 220), "chars/rc2.png", (130, 281), "chars/rca.png")
    image r 2b = im.Composite((346, 934), (0, 220), "chars/rc2.png", (130, 281), "chars/rcb.png")
    image r 2c = im.Composite((346, 934), (0, 220), "chars/rc2.png", (130, 281), "chars/rcc.png")
    image r 2d = im.Composite((346, 934), (0, 220), "chars/rc2.png", (130, 281), "chars/rcd.png")
    image r 2e = im.Composite((346, 934), (0, 220), "chars/rc2.png", (130, 281), "chars/rce.png")
    image r 2f = im.Composite((346, 934), (0, 220), "chars/rc2.png", (130, 281), "chars/rcf.png")
    image r 2g = im.Composite((346, 934), (0, 220), "chars/rc2.png", (130, 281), "chars/rcg.png")
    image r 2h = im.Composite((346, 934), (0, 220), "chars/rc2.png", (130, 281), "chars/rch.png")
    image r 2i = im.Composite((346, 934), (0, 220), "chars/rc2.png", (130, 281), "chars/rci.png")
    image r 2j = im.Composite((346, 934), (0, 220), "chars/rc2.png", (130, 281), "chars/rcj.png")
    image r 2k = im.Composite((346, 934), (0, 220), "chars/rc2.png", (130, 281), "chars/rck.png")
    image r 2l = im.Composite((346, 934), (0, 220), "chars/rc2.png", (130, 281), "chars/rcl.png")
    image r 2m = im.Composite((346, 934), (0, 220), "chars/rc2.png", (130, 281), "chars/rcm.png")
    image r 2n = im.Composite((346, 934), (0, 220), "chars/rc2.png", (130, 281), "chars/rcn.png")
    image r 2o = im.Composite((346, 934), (0, 220), "chars/rc2.png", (130, 281), "chars/rco.png")
    image r 2p = im.Composite((346, 934), (0, 220), "chars/rc2.png", (130, 281), "chars/rcp.png")
    image r 2q = im.Composite((346, 934), (0, 220), "chars/rc2.png", (130, 281), "chars/rcq.png")
    image r 2r = im.Composite((346, 934), (0, 220), "chars/rc2.png", (130, 281), "chars/rcr.png")
    image r 2s = im.Composite((346, 934), (0, 220), "chars/rc2.png", (130, 281), "chars/rcs.png")
    image r 2t = im.Composite((346, 934), (0, 220), "chars/rc2.png", (130, 281), "chars/rct.png")
    image r 2u = im.Composite((346, 934), (0, 220), "chars/rc2.png", (130, 281), "chars/rcu.png")


# fontaine composite images

    image f 1a = im.Composite((371, 1004), (0, 310), "chars/fc1.png", (121, 410), "chars/fca.png")
    image f 1b = im.Composite((371, 1004), (0, 310), "chars/fc1.png", (121, 410), "chars/fcb.png")
    image f 1c = im.Composite((371, 1004), (0, 310), "chars/fc1.png", (121, 410), "chars/fcc.png")
    image f 1d = im.Composite((371, 1004), (0, 310), "chars/fc1.png", (121, 410), "chars/fcd.png")
    image f 1e = im.Composite((371, 1004), (0, 310), "chars/fc1.png", (121, 410), "chars/fce.png")
    image f 1f = im.Composite((371, 1004), (0, 310), "chars/fc1.png", (121, 410), "chars/fcf.png")
    image f 1g = im.Composite((371, 1004), (0, 310), "chars/fc1.png", (121, 410), "chars/fcg.png")
    image f 1h = im.Composite((371, 1004), (0, 310), "chars/fc1.png", (121, 410), "chars/fch.png")
    image f 1i = im.Composite((371, 1004), (0, 310), "chars/fc1.png", (121, 410), "chars/fci.png")
    image f 1j = im.Composite((371, 1004), (0, 310), "chars/fc1.png", (121, 410), "chars/fcj.png")
    image f 1k = im.Composite((371, 1004), (0, 310), "chars/fc1.png", (121, 410), "chars/fck.png")
    image f 1l = im.Composite((371, 1004), (0, 310), "chars/fc1.png", (121, 410), "chars/fcl.png")
    image f 1m = im.Composite((371, 1004), (0, 310), "chars/fc1.png", (121, 410), "chars/fcm.png")
    image f 1n = im.Composite((371, 1004), (0, 310), "chars/fc1.png", (121, 410), "chars/fcn.png")
    image f 1o = im.Composite((371, 1004), (0, 310), "chars/fc1.png", (121, 410), "chars/fco.png")
    image f 1p = im.Composite((371, 1004), (0, 310), "chars/fc1.png", (121, 410), "chars/fcp.png")
    image f 1q = im.Composite((371, 1004), (0, 310), "chars/fc1.png", (121, 410), "chars/fcq.png")
    image f 1r = im.Composite((371, 1004), (0, 310), "chars/fc1.png", (121, 410), "chars/fcr.png")
    image f 1s = im.Composite((371, 1004), (0, 310), "chars/fc1.png", (121, 410), "chars/fcs.png")
    image f 1t = im.Composite((371, 1004), (0, 310), "chars/fc1.png", (121, 410), "chars/fct.png")
    image f 1u = im.Composite((371, 1004), (0, 310), "chars/fc1.png", (121, 410), "chars/fcu.png")

# fontaine composite images (doctor coat)

    image f 2a = im.Composite((500, 1004), (0, 310), "chars/fc2.png", (121, 410), "chars/fca.png")
    image f 2b = im.Composite((371, 1004), (0, 310), "chars/fc2.png", (121, 410), "chars/fcb.png")
    image f 2c = im.Composite((371, 1004), (0, 310), "chars/fc2.png", (121, 410), "chars/fcc.png")
    image f 2d = im.Composite((371, 1004), (0, 310), "chars/fc2.png", (121, 410), "chars/fcd.png")
    image f 2e = im.Composite((371, 1004), (0, 310), "chars/fc2.png", (121, 410), "chars/fce.png")
    image f 2f = im.Composite((371, 1004), (0, 310), "chars/fc2.png", (121, 410), "chars/fcf.png")
    image f 2g = im.Composite((371, 1004), (0, 310), "chars/fc2.png", (121, 410), "chars/fcg.png")
    image f 2h = im.Composite((371, 1004), (0, 310), "chars/fc2.png", (121, 410), "chars/fch.png")
    image f 2i = im.Composite((371, 1004), (0, 310), "chars/fc2.png", (121, 410), "chars/fci.png")
    image f 2j = im.Composite((371, 1004), (0, 310), "chars/fc2.png", (121, 410), "chars/fcj.png")
    image f 2k = im.Composite((371, 1004), (0, 310), "chars/fc2.png", (121, 410), "chars/fck.png")
    image f 2l = im.Composite((371, 1004), (0, 310), "chars/fc2.png", (121, 410), "chars/fcl.png")
    image f 2m = im.Composite((371, 1004), (0, 310), "chars/fc2.png", (121, 410), "chars/fcm.png")
    image f 2n = im.Composite((371, 1004), (0, 310), "chars/fc2.png", (121, 410), "chars/fcn.png")
    image f 2o = im.Composite((371, 1004), (0, 310), "chars/fc2.png", (121, 410), "chars/fco.png")
    image f 2p = im.Composite((371, 1004), (0, 310), "chars/fc2.png", (121, 410), "chars/fcp.png")
    image f 2q = im.Composite((371, 1004), (0, 310), "chars/fc2.png", (121, 410), "chars/fcq.png")
    image f 2r = im.Composite((371, 1004), (0, 310), "chars/fc2.png", (121, 410), "chars/fcr.png")
    image f 2s = im.Composite((371, 1004), (0, 310), "chars/fc2.png", (121, 410), "chars/fcs.png")
    image f 2t = im.Composite((371, 1004), (0, 310), "chars/fc2.png", (121, 410), "chars/fct.png")
    image f 2u = im.Composite((371, 1004), (0, 310), "chars/fc2.png", (121, 410), "chars/fcu.png")


# kylie composite images

    image k 1a = im.Composite((371, 1004), (0, 240), "chars/kc1.png", (86, 394), "chars/kca.png")
    image k 1b = im.Composite((371, 1004), (0, 240), "chars/kc1.png", (86, 394), "chars/kcb.png")
    image k 1c = im.Composite((371, 1004), (0, 240), "chars/kc1.png", (86, 394), "chars/kcc.png")
    image k 1d = im.Composite((371, 1004), (0, 240), "chars/kc1.png", (86, 394), "chars/kcd.png")
    image k 1e = im.Composite((371, 1004), (0, 240), "chars/kc1.png", (86, 394), "chars/kce.png")
    image k 1f = im.Composite((371, 1004), (0, 240), "chars/kc1.png", (86, 394), "chars/kcf.png")
    image k 1g = im.Composite((371, 1004), (0, 240), "chars/kc1.png", (86, 394), "chars/kcg.png")
    image k 1h = im.Composite((371, 1004), (0, 240), "chars/kc1.png", (86, 394), "chars/kch.png")
    image k 1i = im.Composite((371, 1004), (0, 240), "chars/kc1.png", (86, 394), "chars/kci.png")
    image k 1j = im.Composite((371, 1004), (0, 240), "chars/kc1.png", (86, 394), "chars/kcj.png")
    image k 1k = im.Composite((371, 1004), (0, 240), "chars/kc1.png", (86, 394), "chars/kck.png")
    image k 1l = im.Composite((371, 1004), (0, 240), "chars/kc1.png", (86, 394), "chars/kcl.png")
    image k 1m = im.Composite((371, 1004), (0, 240), "chars/kc1.png", (86, 394), "chars/kcm.png")
    image k 1n = im.Composite((371, 1004), (0, 240), "chars/kc1.png", (86, 394), "chars/kcn.png")
    image k 1o = im.Composite((371, 1004), (0, 240), "chars/kc1.png", (86, 394), "chars/kco.png")
    image k 1p = im.Composite((371, 1004), (0, 240), "chars/kc1.png", (86, 394), "chars/kcp.png")
    image k 1q = im.Composite((371, 1004), (0, 240), "chars/kc1.png", (86, 394), "chars/kcq.png")
    image k 1r = im.Composite((371, 1004), (0, 240), "chars/kc1.png", (86, 394), "chars/kcr.png")
    image k 1s = im.Composite((371, 1004), (0, 240), "chars/kc1.png", (86, 394), "chars/kcs.png")
    image k 1t = im.Composite((371, 1004), (0, 240), "chars/kc1.png", (86, 394), "chars/kct.png")
    image k 1u = im.Composite((371, 1004), (0, 240), "chars/kc1.png", (86, 394), "chars/kcu.png")

#david composite images

    image d 1a = im.Composite((371, 1004), (0, 260), "chars/d1.png", (112, 297), "chars/da.png")
    image d 1b = im.Composite((371, 1004), (0, 260), "chars/d1.png", (112, 297), "chars/db.png")
    image d 1c = im.Composite((371, 1004), (0, 260), "chars/d1.png", (112, 297), "chars/dc.png")
    image d 1d = im.Composite((371, 1004), (0, 260), "chars/d1.png", (112, 297), "chars/dd.png")
    image d 1e = im.Composite((371, 1004), (0, 260), "chars/d1.png", (112, 297), "chars/de.png")
    image d 1f = im.Composite((371, 1004), (0, 260), "chars/d1.png", (112, 297), "chars/df.png")
    image d 1g = im.Composite((371, 1004), (0, 260), "chars/d1.png", (112, 297), "chars/dg.png")
    image d 1h = im.Composite((371, 1004), (0, 260), "chars/d1.png", (112, 297), "chars/dh.png")
    image d 1i = im.Composite((371, 1004), (0, 260), "chars/d1.png", (112, 297), "chars/di.png")
    image d 1j = im.Composite((371, 1004), (0, 260), "chars/d1.png", (112, 297), "chars/dj.png")
    image d 1k = im.Composite((371, 1004), (0, 260), "chars/d1.png", (112, 297), "chars/dk.png")
    image d 1l = im.Composite((371, 1004), (0, 260), "chars/d1.png", (112, 297), "chars/dl.png")
    image d 1m = im.Composite((371, 1004), (0, 260), "chars/d1.png", (112, 297), "chars/dm.png")
    image d 1n = im.Composite((371, 1004), (0, 260), "chars/d1.png", (112, 297), "chars/dn.png")
    image d 1o = im.Composite((371, 1004), (0, 260), "chars/d1.png", (112, 297), "chars/do.png")
    image d 1p = im.Composite((371, 1004), (0, 260), "chars/d1.png", (112, 297), "chars/dp.png")
    image d 1q = im.Composite((371, 1004), (0, 260), "chars/d1.png", (112, 297), "chars/dq.png")
    image d 1r = im.Composite((371, 1004), (0, 260), "chars/d1.png", (112, 297), "chars/dr.png")
    image d 1s = im.Composite((371, 1004), (0, 260), "chars/d1.png", (112, 297), "chars/ds.png")
    image d 1t = im.Composite((371, 1004), (0, 260), "chars/d1.png", (112, 297), "chars/dt.png")
    image d 1u = im.Composite((371, 1004), (0, 260), "chars/d1.png", (112, 297), "chars/du.png")

#mortimer
#he works a litte differently. ma is lit screen, mb is blank screen. the 2 series is tania faces.
    image m 1a = im.Composite((260, 1004), (0, 350), "chars/m1.png")
    image m 1b = im.Composite((260, 1004), (0, 350), "chars/m1.png")
    image m 1c = im.Composite((260, 1004), (0, 350), "chars/m2.png")
    image m 1d = im.Composite((260, 1004), (0, 350), "chars/m2.png")

    image m 2a = im.Composite((260, 1004), (0, 350), "chars/ma.png")
    image m 2b = im.Composite((260, 1004), (0, 350), "chars/mb.png")
    image m 2c = im.Composite((260, 1004), (0, 350), "chars/mc.png")
    image m 2d = im.Composite((260, 1004), (0, 350), "chars/md.png")
    image m 2e = im.Composite((260, 1004), (0, 350), "chars/me.png")
    image m 2f = im.Composite((260, 1004), (0, 350), "chars/mf.png")
    image m 2g = im.Composite((260, 1004), (0, 350), "chars/mg.png")
    image m 2h = im.Composite((260, 1004), (0, 350), "chars/mh.png")
    image m 2i = im.Composite((260, 1004), (0, 350), "chars/mi.png")
    image m 2j = im.Composite((260, 1004), (0, 350), "chars/mj.png")
    image m 2k = im.Composite((260, 1004), (0, 350), "chars/mk.png")
    image m 2l = im.Composite((260, 1004), (0, 350), "chars/ml.png")
    image m 2m = im.Composite((260, 1004), (0, 350), "chars/mm.png")
    image m 2n = im.Composite((260, 1004), (0, 350), "chars/mn.png")
    image m 2o = im.Composite((260, 1004), (0, 350), "chars/mo.png")
    image m 2p = im.Composite((260, 1004), (0, 350), "chars/mp.png")
    image m 2q = im.Composite((260, 1004), (0, 350), "chars/mq.png")
    image m 2r = im.Composite((260, 1004), (0, 350), "chars/mr.png")
    image m 2s = im.Composite((260, 1004), (0, 350), "chars/ms.png")
    image m 2t = im.Composite((260, 1004), (0, 350), "chars/mt.png")
    image m 2u = im.Composite((260, 1004), (0, 350), "chars/mu.png")
# second poses

    #cassandra splash images

    default splashCass1 = Image("chars/splashCass1.png")
    default splashCass2 = Image("chars/splashCass2.png")
    default splashCass3 = Image("chars/splashCass3.png")
    default splashCass4 = Image("chars/splashCass4.png")
    default splashCass5 = Image("chars/splashCass5.png")
    default splashCass6 = Image("chars/splashCass6.png")
    default cassBlood = Image("img/cassBlood.png")


    transform cassBooth():
        on show:
            xpos 320 yoffset 0 yanchor 1.0 ypos 0.73 zoom 1.00 alpha 0.0 subpixel True
            easein 1.0 alpha 1.00
        on hide:
            xpos 320 yoffset 0 yanchor 1.0 ypos 0.73 zoom 1.00 alpha 1.0 subpixel True
            linear .5 alpha 0.00


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


    # buttons

    define btnAskTania = Image("img/iconBtnAskTania.png")
    define btnChatHistory = Image("img/iconBtnChatHistory.png")
    define btnSever = Image("img/iconSever.png")
