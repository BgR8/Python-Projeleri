def azalt(s):
    if len(s) < 1:
        return s
    else:
        print('özyineleme sürecine girerken:', s)
        azalt(s[1:])
        print('özyineleme sürecinden çıkarken:', s)

azalt('atölyemde')
