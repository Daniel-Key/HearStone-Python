class Instance:
    #
    # LogParser
    #
    logLength = 0
    optionList = []

    #
    # GameState
    #
    mulliganInProgress = False
    mulliganComplete = False
    #Contains full card info
    mulliganList = []
    handCards = dict()
    cardApiInfo = {}