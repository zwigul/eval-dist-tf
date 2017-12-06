import restool.resplot as rp

exp_id = '00013'

rp.init(exp_id)
rp.load('dumbo010,dumbo011,dumbo014,dumbo017,dumbo019')
rp.plot('usr,used,recv,send')


rp.init('00015')
rp.load('dumbo010,dumbo011,dumbo014,dumbo017,dumbo019')
rp.plot('usr,used,recv,send')

# rp.init(exp_id)
# rp.load('dumbo010')
# rp.plot('usr,used,recv,send')
# 
# rp.init(exp_id)
# rp.load('dumbo011')
# rp.plot('usr,used,recv,send')
# 
# rp.init(exp_id)
# rp.load('dumbo014')
# rp.plot('usr,used,recv,send')
# 
# rp.init(exp_id)
# rp.load('dumbo017')
# rp.plot('usr,used,recv,send')
# 
# rp.init(exp_id)
# rp.load('dumbo019')
# rp.plot('usr,used,recv,send')

# rp.init('00013')
# rp.load()
# rp.plot('gpu1,gmem1')
# rp.load('dumbo010,dumbo011,dumbo014,dumbo017,dumbo019')
# rp.plot('usr,used,recv,send')
# 
# rp.init('00015')
# rp.load()
# rp.plot('gpu1,gmem1')
# rp.load('dumbo010,dumbo011,dumbo014,dumbo017,dumbo019')
# rp.plot('usr,used,recv,send')

rp.show()
