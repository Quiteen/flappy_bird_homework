# -*- coding: utf-8 -*-
from cocos.actions import *
from atlas import *
import common

spriteScores = {}
BestScores = {}
scoreLayer = None

#开始游戏后显示当前得分
def createScoreLayer(gameLayer):
    global scoreLayer
    scoreLayer = gameLayer
    setSpriteScores(0)

def setSpriteScores(score):
    global scoreLayer
    for k in spriteScores:
        try:
            scoreLayer.remove(spriteScores[k])
            spriteScores[k] = None
        except:
            pass

    scoreStr = str(score)
    i = 0
    for d in scoreStr:
        s = createAtlasSprite("number_score_0"+d)
        s.position = common.visibleSize["width"]/2 + 18 * i, common.visibleSize["height"]*4/5
        scoreLayer.add(s, z=50)
        spriteScores[i] = s
        i = i + 1

def setPanelScores(score):
    global scoreLayer
    for k in spriteScores:
        try:
            scoreLayer.remove(spriteScores[k])
            spriteScores[k] = None
        except:
            pass

    scoreStr = str(score)
    i = 0
    for d in scoreStr:
        s = createAtlasSprite("number_score_0"+d)
        s.position = common.visibleSize["width"] *39/50 + 36 - 18 * len(scoreStr) + 18*i, common.visibleSize["height"]* 38/66
        scoreLayer.add(s, z=52)
        spriteScores[i] = s
        i = i + 1

def setBestScores(score):
    global scoreLayer
    for k in BestScores:
        try:
            scoreLayer.remove(BestScores[k])
            BestScores[k] = None
        except:
            pass

    scoreStr = str(score)
    i = 0
    for d in scoreStr:
        s = createAtlasSprite("number_score_0"+d)
        s.position = common.visibleSize["width"] *39/50 + 36 - 18 * len(scoreStr) + 18*i, common.visibleSize["height"]* 33/66
        scoreLayer.add(s, z=52)
        BestScores[i] = s
        i = i + 1
