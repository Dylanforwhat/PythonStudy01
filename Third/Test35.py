import datetime as dt
def 累加月(riqi,yuefen):
    nian = yuefen // 12
    yue = riqi.month + yuefen % 12
    if yue != 12:
        nian = nian + yue // 12
        yue = yue % 12
    return dt.date(riqi.year + nian,yue,riqi.day)