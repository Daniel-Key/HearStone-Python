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
    handCards = []
    prevHandCards = []
    lastCardPlayed = "None"
    lastCardPlayedID = -1
    cardApiInfo = {}
    friendlyMinions = []
    enemyMinions = []
    playerName = ""