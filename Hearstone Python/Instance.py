class Instance:
    programRunning = True
    #
    # MyLogParser
    #
    logLength = 0
    optionList = []

    #
    # GameState
    #
    # preMulligan = False
    # preMulliganList = []
    mulliganInProgress = False
    mulliganComplete = False
    #Contains full card info
    mulliganList = []
    handCards = dict()
    prevHandCards = dict()
    lastCardPlayed = "None"
    cardApiInfo = {}
    friendlyMinions = []
    enemyMinions = []
    lastCardPlayedID = -1
    playerName = ""