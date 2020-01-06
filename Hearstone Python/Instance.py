class Instance:
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
    cardApiInfo = {}
    lastCardPlayed = ""