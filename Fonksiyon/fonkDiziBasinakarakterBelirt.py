def bas(*args, start='', **kwargs):
    for öğe in args:
        print(start+öğe, **kwargs)

bas('öğe1', 'öğe2', 'öğe3', start="#.")
