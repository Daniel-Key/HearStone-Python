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
    lastCardPlayedID = 24
    cardApiInfo = {}
    friendlyMinions = []
    enemyMinions = []
    friendlyWeapons = []
    friendlyWeaponsInPlay = []
    enemyWeapons = []
    playerName = ""
    logFileGameStart = 0


    def reset(self):
        self.optionList = []
        self.mulliganInProgress = False
        self.mulliganComplete = False
        #Contains full card info
        self.mulliganList = []
        self.handCards = []
        self.prevHandCards = []
        self.lastCardPlayed = "None"
        self.lastCardPlayedID = -1
        self.cardApiInfo = {}
        self.friendlyMinions = []
        self.enemyMinions = []
        self.friendlyWeapons = []
        self.friendlyWeaponsInPlay = []
        self.enemyWeapons = []
        self.playerName = ""