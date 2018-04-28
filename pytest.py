ary = {}
dpid = 1
ary.setdefault(dpid, {})
a = [1:10,2:20]
ary[dpid][a] = 10


if 1 in ary[dpid]:
    print('???')